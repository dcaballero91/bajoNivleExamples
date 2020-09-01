# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:11:32 2020

@author: dcaballe
"""
#!/usr/bin/env python
# -*- Coding: utf-8 -*-

from flask import Flask, jsonify, request
from Template import Template
from comparar import comparar
app = Flask(__name__) 

##servicios rest
app.register_blueprint(Template)
app.register_blueprint(comparar)
@app.route('/', methods=['GET'])
def hello():
    return 'Unida 2020!'


if __name__ == "__main__":
    ##app.run(host = '127.0.0.1', debug = True, port = 5000)
    app.run(host = '0.0.0.0', debug = True, port = 5001)
    app.run(debug = True)