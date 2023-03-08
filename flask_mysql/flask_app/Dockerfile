FROM python:3.9

RUN pip install flask
RUN pip install flask_mysqldb

ADD app.py /app/app.py

ENTRYPOINT python3 /app/app.py
