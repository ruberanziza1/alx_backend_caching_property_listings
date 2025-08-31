# Use Python base image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Port and default run command
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
