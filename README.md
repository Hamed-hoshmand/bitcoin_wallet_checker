# Bitcoin Wallet Checker

## توضیحات پروژه

این پروژه یک زیرساخت مقیاس‌پذیر و امن برای بررسی و مدیریت کیف‌پول‌های بیت‌کوین است. با استفاده از Seed Phrase‌ها، می‌توان کیف‌پول‌های مرتبط را بازیابی و اطلاعات آن‌ها را استخراج کرد.

## پیش‌نیازها

- Docker و Docker Compose
- Python 3.8+
- Git

## راه‌اندازی محلی

1. کلون کردن مخزن:

    ```bash
    git clone https://github.com/Hamed-hoshmand/bitcoin_wallet_checker.git
    cd bitcoin_wallet_checker
    ```

2. ایجاد و فعال‌سازی محیط مجازی:

    ```bash
    python3 -m venv venv
    venv\Scripts\activate  # برای ویندوز
    # source venv/bin/activate  # برای macOS/Linux
    ```

3. نصب وابستگی‌ها:

    ```bash
    pip install -r requirements.txt
    ```

4. ساخت و اجرای کانتینرها با Docker Compose:

    ```bash
    docker-compose up --build
    ```

5. تست API:

    - اضافه کردن Seed Phrase‌ها:

        ```bash
        curl -X POST http://localhost:5000/enqueue \
             -H "Content-Type: application/json" \
             -d '{"seed_phrases": ["seed phrase 1", "seed phrase 2"]}'
        ```

    - دریافت اطلاعات کیف‌پول:

        ```bash
        curl http://localhost:5000/wallet/seed%20phrase%201
        ```

## استقرار در Kubernetes

1. ساخت ایمیج‌های Docker و ارسال به Docker Hub:

    ```bash
    docker build -t your-dockerhub-username/bitcoin_wallet_checker_web:latest -f docker/Dockerfile .
    docker build -t your-dockerhub-username/bitcoin_wallet_checker_celery:latest -f docker/celery.Dockerfile .
    docker push your-dockerhub-username/bitcoin_wallet_checker_web:latest
    docker push your-dockerhub-username/bitcoin_wallet_checker_celery:latest
    ```

2. اعمال پیکربندی‌ها به Kubernetes:

    ```bash
    kubectl apply -f k8s/
    ```

## امنیت

- **رمزنگاری داده‌ها:** Seed Phrase‌ها به صورت رمزنگاری شده ذخیره می‌شوند.
- **احراز هویت:** استفاده از JWT برای دسترسی به API‌ها.
- **TLS/SSL:** استفاده از HTTPS برای ارتباطات امن.

## مانیتورینگ

- **Prometheus:** جمع‌آوری متریک‌های سیستم.
- **Grafana:** نمایش داشبوردهای گرافیکی.

## تست

برای اجرای تست‌ها:

```bash
pytest
