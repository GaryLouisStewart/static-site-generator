# Use a lightweight Python 3 image
FROM python:3.10-slim
LABEL authors="garylouisstewart"

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8000 if your app runs on this port (change if needed)
EXPOSE 8000

# Command to run the static site generator
CMD ["python", "main.py"]
