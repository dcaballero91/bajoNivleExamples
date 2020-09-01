# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 20:13:24 2020

@author: dcaballe
Ej. llamada:
http://localhost:5001/comparar?tipo=jg&a=1&b=3

"""
from flask import Blueprint, request, jsonify


comparar = Blueprint('comparar', __name__)

@comparar.route('/comparar', methods=['GET'])
def llamarServicioSet():
    global tipo,tiporet,a,b,cretrun
    ##try:
    if 'tipo' in request.args and 'a' in request.args and 'b' in request.args:
        tipo = str(request.args['tipo'])
        a=str(request.args['a'])
        b=str(request.args['b'])
        inicializarVariables(tipo,a,b)
    else:
        return "Error: No mod tipo,a,b provmoded. Please specify an tipo,a,b"
    

    salida = {'codRes': codRes, 'menRes': menRes,'tipo':tiporet,'cretrun':cretrun,'a':a,'b':b}
    return jsonify({'ParmOut':salida})


def inicializarVariables(tipo,a,b):
    global codRes, menRes, cretrun,tiporet
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    accesoSet(tipo,a,b)
    


def accesoSet(tipo,a,b):
    global menRes,codRes,cretrun,tiporet
    

    try:
        print(tipo)
        if tipo == 'jg' or tipo == 'JG':
            print("JG")
            tiporet="jg"
            if a >= b:
                cretrun="Es mayor"
                print(cretrun)
            else:
                cretrun="No es mayor"
                print(cretrun)
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
            
        return tiporet,cretrun,a,b
       
    except Exception as e:
        print("Error en manipular datos",str(e))
        