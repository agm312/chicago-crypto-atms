FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Generate the static files
RUN python process_data.py

# Expose the port the app runs on
EXPOSE 8084

# Command to run the application
CMD ["python", "server.py"] 