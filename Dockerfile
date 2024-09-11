FROM python:3.10.0-slim

WORKDIR /flask_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["gunicorn", "-b", "0.0.0.0:8080", "flask_app.app:app"]
