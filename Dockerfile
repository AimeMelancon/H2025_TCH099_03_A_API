# Use an official Python image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the database folder exists
RUN mkdir -p db

# Expose Flask port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]