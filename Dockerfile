# Dockerfile for app service

FROM python:3.9

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /home/app

WORKDIR /home/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 9090

COPY . .

CMD ["python", "scrape.py"]

# # Use the official Python image from the Docker Hub
# FROM python:3.9

# # Set the working directory in the container
# WORKDIR /usr/app

# # Copy the requirements file into the container
# COPY requirements.txt ./

# # Install the required packages
# RUN pip install --no-cache-dir -r requirements.txt

# # Expose port number
# EXPOSE 9090

# # Copy the rest of the application code into the container
# COPY . .

# # Run the script
# CMD [ "python", "patan.py" ]
