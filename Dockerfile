FROM python:3

WORKDIR /data

RUN pip install django

RUN pip install requests

RUN pip install mysqlclient

COPY . .

RUN python manage.py migrate

EXPOSE 8002

CMD ["python","manage.py","runserver","0.0.0.0:8002"]
