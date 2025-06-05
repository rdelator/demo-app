FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Explicitly ensure templates directory is copied (defensive)
RUN ls /app/templates && cat /app/templates/index.html

EXPOSE 8080

CMD ["python", "app.py"]
