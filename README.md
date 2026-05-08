# Микросервисная система заказов

## О проекте

Система из трёх микросервисов для обработки заказов с расчётом скидок.  
Демонстрирует взаимодействие сервисов как локально, так и в Docker-контейнерах.

### Архитектура

Пользователь -> Order Service (порт 8002) ->
Product Service (порт 8001) -> получает цену товара ->
Discount Service (порт 8003) -> рассчитывает скидку ->
Возвращает итоговую сумму


### Сервисы

Product Service - Информация о товарах 
Discount Service - Расчёт скидок
Order Service - Создание заказов 

### Правила скидок

Промокод `STUDENT10` - 10% 
Количество ≥ 10 - 5%
Промокод `WELCOME5` - 5% 
Количество ≥ 5 - 3% 

---

## Быстрый старт

### Локальный запуск (без Docker)

```bash
# Терминал 1
cd product_service && make run

# Терминал 2
cd discount_service && make run

# Терминал 3
cd order_service && make run
```

### Запуск через Docker Compose
```bash
make docker-up
```

### Остановка
```bash
make docker-down
```

## Примеры запросов
```bash
# Заказ со скидкой по промокоду
curl -X POST http://localhost:8002/orders \
  -H "Content-Type: application/json" \
  -d '{"product_id": "pencil", "quantity": 2, "promocode": "STUDENT10"}'

# Ответ
{
  "product_id": "pencil",
  "quantity": 2,
  "unit_price": 1.5,
  "total_before_discount": 3.0,
  "discount_percent": 10.0,
  "discount_amount": 0.3,
  "total": 2.7
}
```
---

## Makefile команды

make install-all - Установить зависимости
make docker-up - Запустить через Docker Compose
make docker-down - Остановить Docker
make clean-all - Очистить кэш

### Переменные окружения

PRODUCT_SERVICE_URL - http://127.0.0.1:8001
DISCOUNT_SERVICE_URL - http://127.0.0.1:8003
### Документация API
После запуска открой в браузере: http://localhost:8002/docs

---

#### Подробнее

NETWORKING_NOTES.md — объяснение работы сетей в Docker

product_service/README.md

discount_service/README.md

order_service/README.md

#### Технологии
Python 3.12
FastAPI
Docker / Docker Compose
Poetry / pip