# Docker Networking: от localhost к именам сервисов
## Главная идея

**localhost не универсален. Всё зависит от того, где выполняется код.**

---

## 1. Локальный запуск (127.0.0.1 работает)

Когда сервисы запущены прямо на компьютере (без Docker):

```bash
# Все сервисы запущены на хосте
curl http://127.0.0.1:8001/health  # Product Service
curl http://127.0.0.1:8003/health  # Discount Service
curl http://127.0.0.1:8002/health  # Order Service
```

**Почему работает:** Все процессы на одной машине, 127.0.0.1 указывает на эту же машину.

---

## 2. Ошибка: localhost внутри контейнера
Если код бежит внутри контейнера, а обращается к 127.0.0.1:

```bash
PRODUCT_SERVICE_URL = "http://127.0.0.1:8001"  # не работает в контейнере
```

**Почему не работает:** Внутри контейнера 127.0.0.1 означает сам контейнер, а не хост и не другой контейнер.

---

## 3. Правильно: имена сервисов в Docker сети
Когда контейнеры запущены в одной Docker-сети, они видят друг друга по имени:

```yaml
# docker-compose.yml
services:
  product-service:   # имя становится hostname внутри сети
    build: ./product_service
    
  order-service:
    environment:
      PRODUCT_SERVICE_URL: http://product-service:8001  # обращение по имени
```

**Почему работает:** Docker создаёт внутренний DNS, который превращает product-service в IP-адрес контейнера.

---

## 4. Специальный случай: host.docker.internal
Если контейнеру нужно обратиться к сервису на хосте:

```bash
DATABASE_URL = "postgresql://user:pass@host.docker.internal:5432/db"
```
Работает только на Docker Desktop (Windows/Mac).

---

## Практический вывод
В коде **не хардкодим адреса**. Используем переменные окружения:

```bash
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://127.0.0.1:8001")
``` 
Это позволяет:
- Локально: использовать 127.0.0.1
- В Docker: передать http://product-service:8001

Один образ - для любых окружений.