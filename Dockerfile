FROM python:3.8-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY home.py /app

ENV FLASK_APP=home.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]