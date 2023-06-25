FROM python:3.12.0b3-alpine3.18
RUN mkdir /home/src
COPY ./src/ /home/src/
RUN python3 -m pip install fastapi==0.96.1 uvicorn==0.22.0 mysql-connector-python
ENTRYPOINT cd /home/src && uvicorn main:app --proxy-headers --host 0.0.0.0 --port 8000