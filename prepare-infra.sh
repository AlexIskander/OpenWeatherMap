#!/bin/bash

set -e

cd $WORKSPACE/terraform
terraform init
terraform plan --out myplan
terraform apply "myplan"
terraform show
