# Use a smaller base image
FROM python:3.13

# Set working directory
WORKDIR /app

# Copy only necessary files
COPY requirements.txt /app/

# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire app
COPY . /app

# Set non-root user for better security
# RUN adduser --disabled-password myuser
# USER myuser

# Run the application
CMD ["python", "app.py"]