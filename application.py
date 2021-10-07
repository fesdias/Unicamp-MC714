#!/usr/bin/python
# -*- coding: utf-8 -*-

#Amazon flask application
#https://docs.aws.amazon.com/pt_br/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

import socket
from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    ip = socket.gethostbyname(socket.gethostname())
    return render_template("Acervo.html", ip = ip)

if __name__ == "__main__":
    application.run()
