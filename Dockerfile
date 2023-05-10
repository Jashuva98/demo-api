FROM python:3.11.2-slim-buster
WORKDIR /app
ENV FLASK_APP =main.py
ENV FLASK-RUN_HOST = 0.0.0.0
ENV FLASK_ENV = development
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]