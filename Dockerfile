FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY home.py /app

COPY /templates /app/templates

ENV FLASK_APP=home.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]