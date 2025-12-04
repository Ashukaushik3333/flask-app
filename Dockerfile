FROM python:3.11-slim

WORKDIR /app

# Copy everything INCLUDING templates and static
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app/app.py"]

