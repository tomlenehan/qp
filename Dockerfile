# Use an official Python runtime as the base image
FROM python:3.11

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install NodeJS
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get install -y nodejs

# Copy the rest of the application code into the container
COPY . /app

# Set environment variables for the application
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV POSTGRES_DB=${POSTGRES_DB}

# Expose port 8000 for the application
EXPOSE 8000

# Install frontend dependencies and build
RUN cd /app/frontend && npm install && npm run build

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "0.0.0:8000"]
