#!/bin/bash

set -e

cd $WORKSPACE/terraform
/home/vagrant/terraform init
/home/vagrant/terraform plan --out myplan
/home/vagrant/terraform apply "myplan"
/home/vagrant/terraform show
