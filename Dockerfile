# Use the official Python image as the base image
FROM python

# Set the working directory in the container
WORKDIR /

# Copy the application files into the working directory
COPY . /app

# Install the application dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]
