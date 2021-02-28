FROM python:3.8-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["flask","run","-h", "0.0.0.0"]
