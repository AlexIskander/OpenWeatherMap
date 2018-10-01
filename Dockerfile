FROM alpine:3.7

COPY ./  /opt/OpenWeatherMap


RUN  apk add --no-cache python \
     python-dev \
     py-pip \
     build-base \
     git \
     && pip install -r /opt/OpenWeatherMap/requirements.txt \
     && python /opt/OpenWeatherMap/manage.py migrate 


EXPOSE 8888 
CMD python /opt/OpenWeatherMap/manage.py runserver 0.0.0.0:8888

