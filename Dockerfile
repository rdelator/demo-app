FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy app code
COPY . .

# (Optional) Print directory contents for debugging
# RUN ls -la /app/templates

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]
