FROM python:3.9.6-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev freetype-dev gdal-dev
# RUN apt-get install bin-utils libproj-dev gdal-bin

RUN pip install --upgrade pip
COPY requirements.txt /

RUN pip install -r requirements.txt

WORKDIR /usr/src/app

#copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh


COPY . .

EXPOSE 80

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
