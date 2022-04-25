#!/bin/bash

exec > >(tee /var/log/user-data.log|logger -t user-data -s 2>/dev/console) 2>&1
yum update -y

cd /home/ec2-user/
wget https://flask-bucket-2022-04-27.s3.us-west-2.amazonaws.com/flaskproject.zip

unzip flaskproject.zip
rm flaskproject.zip
chown -R ec2-user .
pip3 install Flask
pip3 install boto3
cd flaskproject
cd flaskr
export AWS_DEFAULT_REGION=us-west-2
python3 __init__.py