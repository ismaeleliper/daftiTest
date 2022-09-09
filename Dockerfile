# pull official base image
FROM python:3.8.6-alpine

# set work directory
WORKDIR /usr/src/web/zee

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY web .