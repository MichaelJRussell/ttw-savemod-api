FROM python:3.10.5-alpine3.16

ENV FLASK_APP ttwl_savemod_api
WORKDIR /app
RUN apk update
RUN apk add git

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./ttwl_savemod_api ./ttwl_savemod_api/

CMD ["flask", "run", "--host=0.0.0.0"]
