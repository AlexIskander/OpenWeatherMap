#!/bin/bash

SOURCE=/opt/OpenWeatherMap/

function runapp {
   cd ${SOURCE};
   python manage.py runserver 0.0.0.0:8888
}

runapp
