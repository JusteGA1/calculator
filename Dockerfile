FROM python:3.8-buster

WORKDIR /usr/src/app

RUN pip install git+https://github.com/JusteGA1/calculator

COPY ./docker/app.py ./

CMD ["python", "app.py"]
