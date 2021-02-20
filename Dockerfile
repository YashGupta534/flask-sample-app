FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8080

# CMD ["python", "app.py"]
CMD ["gunicorn", "app:app", "--workers", "2", "-b", "0.0.0.0:8080"]