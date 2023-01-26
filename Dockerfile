# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy environment variables into the container
COPY .env /app/

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install NodeJS and npm
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs

# Copy the rest of the application code into the container
COPY . /app

# Expose port 8000 for the application
EXPOSE 8000

# Change to the frontend directory and install npm dependencies
WORKDIR /app/frontend
RUN npm install

# Build the frontend code
RUN npm run build

# Change back to the root directory
WORKDIR /app

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
