FROM python:3.7
COPY . /app
WORKDIR /app

RUN apt-get update -y
RUN apt-get -y install curl wget


RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
