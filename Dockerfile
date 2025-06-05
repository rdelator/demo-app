FROM public.ecr.aws/docker/library/python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Make sure everything including templates/ is copied into /app
COPY . .

# Defensive: confirm file is in the image
RUN cat /app/templates/index.html

EXPOSE 8080
CMD ["python", "app.py"]
