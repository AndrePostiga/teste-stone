FROM python:3.7-alpine 
MAINTAINER Andre Postiga

COPY app /var/www
WORKDIR /var/www

RUN pip install --upgrade pip
RUN pip install virtualenv
CMD ["venv/scripts/activate"]
RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;

RUN pip install -r requirements.txt
CMD ["python", "main.py"]