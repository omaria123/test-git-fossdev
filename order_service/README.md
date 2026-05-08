# Order Service

Сервис заказов. Координирует работу Product Service и Discount Service.

## API

| Метод | Эндпоинт | Описание |
|-------|----------|----------|
| GET | `/health` | Проверка здоровья |
| POST | `/orders` | Создать заказ |

## Запуск

```bash
make run
```

Сервис запустится на порту 8002.

## Пример запроса
```bash
curl -X POST http://localhost:8002/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id": "pencil", "quantity": 2, "promocode": "STUDENT10"}'
```
## Переменные окружения
|Переменная | По умолчанию |
|-----------|--------------|
|PRODUCT_SERVICE_URL |	http://127.0.0.1:8001 |
|DISCOUNT_SERVICE_URL |	http://127.0.0.1:8003 |