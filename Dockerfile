FROM python:3.6-buster

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]

CMD ["python3", "./manage.py", "runserver"]