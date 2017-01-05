#!/usr/bin/env bash

sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/
sudo /etc/init.d/nginx restart
sudo ln -s /home/box/web/etc/hello.py  /etc/gunicorn.d/
sudo /etc/init.d/gunicorn restart

