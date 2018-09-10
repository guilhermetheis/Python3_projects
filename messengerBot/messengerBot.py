#!/usr/bin/env python3

"""
Author: Guilherme Theis

License: MIT

Email: guilhermetheis15@gmail.com

Github: https://github.com/guilhermetheis
"""

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def receive_message():
	return "Hello World!"

if __name__ = '__main__':
	app.run()