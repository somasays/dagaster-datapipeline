#!/bin/bash

# Purpose: EMR bootstrap script
# Author:  Gary A. Stafford (2021-04-05)

SET -e

# update and install some useful yum packages
sudo yum install -y jq

# set region for boto3
aws configure set region \
  "$(curl http://169.254.169.254/latest/dynamic/instance-identity/document | jq -r .region)"

sudo python3 -m pip install --upgrade pip

sudo python3 -m pip install --upgrade setuptools

# install some useful python packages
sudo python3 -m pip install \
  boto3 \
  ec2-metadata \
  dagster \
  dagster_aws \
  dagster_pyspark


