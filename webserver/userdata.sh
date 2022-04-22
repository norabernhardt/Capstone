#!/bin/bash
sudo yum update -y
chkconfig httpd on
service httpd start