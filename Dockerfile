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
                # Pillow dependencies
                jpeg-dev \
                zlib-dev \
                freetype-dev \
                lcms2-dev \
                openjpeg-dev \
                tiff-dev \
                tk-dev \
                tcl-dev \
                harfbuzz-dev \
                fribidi-dev \
        ;
RUN pip install -r requirements.txt
CMD ["python", "main.py"]