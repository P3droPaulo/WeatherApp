# Use the official Python image as the base image
FROM python:3.8

# Install the application dependencies
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

# Define the entry point for the container
CMD ["flask", "run", "--host=0.0.0.0"]
