#!/bin/sh
gunicorn --workers 1 --bind 0.0.0.0:8081 img_server:app