FROM python:3.9

WORKDIR /python_api

COPY requirements.txt /python_api

RUN pip install -r requirements.txt

COPY . /python_api

CMD python event_api.py