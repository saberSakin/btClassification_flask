# Use the official Python 3.11 image from Docker Hub
FROM python:3.11

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy your application code into the container
COPY . .

# Expose the port on which your Flask app will run
EXPOSE 5000

# Define the command to run your Flask application
CMD ["python", "app.py"]
