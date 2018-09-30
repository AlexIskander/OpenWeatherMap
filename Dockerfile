FROM ubuntu:16.04

COPY ./  /opt/OpenWeatherMap


RUN apt-get update; apt-get -qy install python-pip; \
    useradd -M -s /bin/bash userapp ; \
    pip install -r /opt/OpenWeatherMap/requirements.txt; \
    python /opt/OpenWeatherMap/manage.py migrate; \
    chown -R userapp: /opt/OpenWeatherMap


USER userapp
 
CMD /opt/OpenWeatherMap/run.sh

