FROM ubuntu:latest

RUN mkdir -p /app/config

COPY flask_api.py /app/flask_api.py
COPY requirements.txt /app/config

RUN apt update -y
RUN apt install python3 -y
RUN apt install python3-pip -y

WORKDIR /app/

RUN pip3 install -r /app/config/requirements.txt

ENV FLASK_APP /app/flask_api.py

#CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["gunicorn", "flask_api:app", "-b" "0.0.0.0:5000"]
