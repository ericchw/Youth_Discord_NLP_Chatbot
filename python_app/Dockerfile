FROM python:3.9

WORKDIR /python_app

COPY requirements.txt /python_app

RUN pip install -r requirements.txt

RUN pip install psycopg2-binary

COPY . /python_app

CMD python dischatbot.py