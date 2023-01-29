FROM python:3.8.12

COPY . /python_app 

WORKDIR /python_app

RUN pip3 install -r requirements.txt

CMD ["python3", "src/main.py"]