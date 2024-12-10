#!/bin/bash
python3 manage.py migrate
gunicorn ticket.wsgi --bind 0.0.0.0:3000
