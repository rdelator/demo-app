FROM python:3.11-slim

WORKDIR /app

# Add this line first to cache dependencies properly
COPY requirements.txt .

RUN pip install -r requirements.txt

# Then copy everything else (this will trigger rebuild on changes)
COPY . .

EXPOSE 8080
CMD ["python", "app.py"]
