# Python and Linux version
FROM python:3.8.7-alpine3.12

COPY requirements.txt /app/requirements.txt

# Configure server
RUN set -ex \
    && pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Working directory
WORKDIR /app

ADD . .

RUN python manage.py collectstatic \
    && python manage.py makemigrations \
    && python manage.py migrate

## for local test
# EXPOSE 8000
# CMD ["gunicorn", "--bind", ":8000", "--workers", "1", "urmart_hw.wsgi:application"]

CMD gunicorn urmart_hw.wsgi:application --bind 0.0.0.0:$PORT