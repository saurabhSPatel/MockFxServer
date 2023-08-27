# Use the official Python image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project files to the container
COPY . /app/

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
