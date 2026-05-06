from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Discount Service")


class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    price: float
    promocode: Optional[str] = None


class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str


@app.get("/health")
def health():
    return {"status": "ok", "service": "discount-service"}


@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest):
    discount = 0.0
    reason = "No discount applied"
    
    if request.promocode == "STUDENT10":
        discount = 10.0
        reason = "Student discount applied (STUDENT10)"
    
    elif request.quantity >= 10:
        discount = 5.0
        reason = f"Bulk discount applied for quantity {request.quantity}"
    
    elif request.promocode == "WELCOME5":
        discount = 5.0
        reason = "Welcome discount applied (WELCOME5)"
    
    elif request.quantity >= 5:
        discount = 3.0
        reason = f"Small order discount for quantity {request.quantity}"
    
    return DiscountResponse(discount_percent=discount, reason=reason)