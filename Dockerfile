FROM python:3.11

WORKDIR /flask_app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python", "flask_app/app.py"]
