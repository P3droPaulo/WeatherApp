FROM python:3.6.1-alpine
COPY . /app
RUN pip install flask
RUN pip install request
WORKDIR /app
CMD python app.py
