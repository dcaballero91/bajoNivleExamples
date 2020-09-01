# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:44:26 2020

@author: dcaballe
Ej. llamada:
http://localhost:5001/Template?tipo=jg
"""
from flask import Blueprint, request, jsonify


Template = Blueprint('Template', __name__)

@Template.route('/Template', methods=['GET'])
def llamarServicioSet():
    global tipo,tiporet
    ##try:
    if 'tipo' in request.args:
        tipo = str(request.args['tipo'])
        inicializarVariables(tipo)
    else:
        return "Error: No mod tipo provmoded. Please specify an tipo."

    salida = {'codRes': codRes, 'menRes': menRes,'tipo':tiporet}
    return jsonify({'ParmOut':salida})


def inicializarVariables(tipo):
    global codRes, menRes, tiporet
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accesoSet(tipo)
    


def accesoSet(tipo):
    global menRes,codRes,tiporet
    

    try:
        if tipo == 'jg' or tipo == 'JG':
            print("JG")
            tiporet="jg"
            
        elif tipo =='jl' or tipo =='JL':
            print("JL")
            tiporet="jl"
        elif tipo == 'je' or tipo =='JE':
            print("JE")
            tiporet="je"
        elif tipo == 'jge' or tipo == 'JGE':
            print("JGE")
            tiporet="jge"
        else:
            print("No definido")
            tiporet="JG,JL,JE,JGE"
            codRes = 'ERROR'
            menRes = 'Valores Adminitidos'
        return tiporet
       
    except Exception as e:
        print("Error en manipular datos",str(e))