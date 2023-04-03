FROM python:3.9

WORKDIR /python_app

COPY requirements.txt /python_app

RUN pip install -r requirements.txt

COPY . /python_app


CMD python event_api.py