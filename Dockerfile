FROM python:3.6-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "migrate"]

CMD ["python3", "manage.py", "runserver", "--host", "0.0.0.0", "--port", "80"]