FROM python:alpine

EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY flaskapp.py /app
CMD python flaskapp.py
