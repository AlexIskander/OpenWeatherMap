#!/bin/bash

set -e

cd $WORKSPACE/terraform

/home/alex/softserve/docker_work/terraform init
/home/alex/softserve/docker_work/terraform plan --out myplan
/home/alex/softserve/docker_work/terraform aplly 'myplan'
