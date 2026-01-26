FROM python:3.11-slim

WORKDIR /app

# 1. Устанавливаем системные штуки (инструменты для сборки)
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# 2. Создаем виртуальное окружение
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# 3. Сначала копируем список библиотек и УСТАНАВЛИВАЕМ их
# Это важно сделать ДО копирования кода, чтобы Docker кэшировал слои
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Теперь копируем твой код
COPY django_test/ .

# 5. Теперь Django установлен, и мы можем собрать статику
RUN python manage.py collectstatic --noinput

# 6. Запускаем!
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "django_test.wsgi:application"]