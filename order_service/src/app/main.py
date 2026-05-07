import os

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from datetime import datetime
from contextlib import asynccontextmanager

from .database import get_order, init_db, save_order
from .settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(
    title="Order Service",
    lifespan=lifespan,
)


PRODUCT_SERVICE_URL = os.getenv(
    "PRODUCT_SERVICE_URL",
    "http://127.0.0.1:8001",
)

DISCOUNT_SERVICE_URL = os.getenv(
    "DISCOUNT_SERVICE_URL",
    "http://127.0.0.1:8003",
)

class OrderRequest(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)
    promocode: str | None = None


class OrderResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: float
    total_before_discount: float
    discount_percent: float
    discount_amount: float
    total: float


class StoredOrderResponse(BaseModel):
    id: int
    product_id: str
    quantity: int
    unit_price: float
    total: float
    created_at: datetime


class ProductFromService(BaseModel):
    id: str
    name: str
    price: float
    available: bool

class DiscountFromService(BaseModel):
    discount_percent: float
    reason: str

@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "order-service"}


@app.post("/orders", response_model=OrderResponse)
async def create_order(order: OrderRequest) -> OrderResponse:
    product = await fetch_product(order.product_id)

    if not product.available:
        raise HTTPException(
            status_code=400,
            detail=f"Product '{order.product_id}' is not available",
        )
    
    total_before = product.price * order.quantity
    discount_info = await fetch_discount(
        product_id=order.product_id,
        quantity=order.quantity,
        price=product.price,
        promocode=order.promocode
    )

    discount_percent = discount_info.discount_percent
    discount_amount = total_before * (discount_percent / 100)
    total = total_before - discount_amount

    order_id = save_order(
        {
            "product_id": product.id,
            "quantity": order.quantity,
            "unit_price": product.price,
            "total_before_discount": total_before,
            "discount_percent": discount_percent,
            "discount_amount": discount_amount,
            "total": total,
        }
    )

    return OrderResponse(
        product_id=product.id,
        quantity=order.quantity,
        unit_price=product.price,
        total_before_discount=round(total_before, 2),
        discount_percent=discount_percent,
        discount_amount=round(discount_amount, 2),
        total=round(total, 2),
    )

@app.get("/orders/{order_id}", response_model=StoredOrderResponse)
def read_order(order_id: int) -> StoredOrderResponse:
    saved_order = get_order(order_id)

    if saved_order is None:
        raise HTTPException(
            status_code=404,
            detail=f"Order '{order_id}' was not found",
        )

    return StoredOrderResponse(
        id=saved_order["id"],
        product_id=saved_order["product_id"],
        quantity=saved_order["quantity"],
        unit_price=float(saved_order["unit_price"]),
        total=float(saved_order["total"]),
        created_at=saved_order["created_at"],
    )



async def fetch_product(product_id: str) -> ProductFromService:
    url = f"{PRODUCT_SERVICE_URL}/products/{product_id}"

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.get(url)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Product service is unavailable: {exc}",
        ) from exc

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail=f"Product '{product_id}' was not found",
        )

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Product service returned an unexpected error",
        )

    return ProductFromService.model_validate(response.json())

async def fetch_discount(product_id: str, quantity: int, price: float, promocode: str | None) -> DiscountFromService:
    url = f"{DISCOUNT_SERVICE_URL}/discounts/calculate"
    payload = {
        "product_id": product_id,
        "quantity": quantity,
        "price": price,
        "promocode": promocode,
    }

    try:
        async with httpx.AsyncClient(timeout=3.0) as client:
            response = await client.post(url, json=payload)

    except httpx.RequestError as exc:
        raise HTTPException(
            status_code=503,
            detail=f"Discount service is unavailable: {exc}",
        ) from exc

    if response.status_code >= 400:
        raise HTTPException(
            status_code=502,
            detail="Discount service returned an unexpected error",
        )

    return DiscountFromService.model_validate(response.json())