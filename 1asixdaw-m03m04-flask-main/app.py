##!/usr/bin/env python3

import logging
from flask import Flask, request, redirect, abort, render_template, url_for, flash
from mydb2.query import Consultes
from mydb2.manipulation import CreacioyEliminacio 
app = Flask(__name__)

# Defineix el nivell per defecte de log
app.logger.setLevel(logging.INFO)

#SECRET_KEY: clau d'encriptació de la cookie
app.config.update(
    SECRET_KEY='secret_xxx'
)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # Get value from URL
    return render_template('hello.html', name=name)

@app.route('/hello2')
def hello2():
    # Get value from URL query param
    # /hello2?alias=xxx
    param = request.args.get('alias')
    return render_template('hello.html', alias=param)






@app.route("/contacte", methods = ["GET", "POST"])
def contacte():
    if request.method == 'GET':
        # Show form
        return render_template('contacte.html')
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        email = data.get("email-contacte") 

        app.logger.info(f"Comentaris de {email}")
        # TODO: Add more logs 

        # Flash message to inform the user
        flash(f"En breu rebreu resposta a {email}")
        return redirect(url_for('thanks'))

@app.route("/thanks-for-your-comments") # default is GET
def thanks():
    return render_template('contacte-thanks.html')

# Run this application in debug mode ap port 5001
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)




#COMENCEM
##################################################################
##################################################################
##################################################################
#Llistem la clientela
@app.route('/clientela/list')
def resource_list():
    # TODO Get data (database select)
    data = Consultes.mostrar_clientes()
    # Show data
    return render_template('clientela/list.html',results=data)



#Llistem cadacun dels recursos
@app.route('/clientela/read/<int:id>')
def resource_read(id):
    # TODO Get data (database select)
    data = Consultes.mostrar_clientes_individual(id)
    # Show data
    return render_template('clientela/read.html',resource=data)

@app.route('/clientela/create', methods=["GET", "POST"])
def resource_create():
    if request.method == 'GET':
        # Show form
        return render_template('clientela/create.html')
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        
        # TODO Save data (database insert)

        saved_id = CreacioyEliminacio.crear_client2(data)
        # Redirect to show page
        return redirect(url_for('resource_read', id=saved_id))
    else:
        # Not found response
        abort(404)

#Eliminar
@app.route('/clientela/delete/<int:id>', methods=["GET", "POST"])
def resource_delete(id):
    if request.method == 'GET':
        # Show form
        
        return render_template('clientela/delete.html',id=id)
    elif request.method == 'POST':
        # Get POST data
        # TODO Save data (database insert)
        
        if request.form.get("confirmacio",False):
            print("SDFSF")
            CreacioyEliminacio.eliminar_pagina2(id)
        else:
            print("sdfsdfds")
        # Redirect to show page
        return redirect('/clientela/list')
    else:
        # Not found response
        abort(404)

#UPDATE
@app.route('/clientela/update/<int:id>', methods=["GET", "POST"])
def Actualitzacio_clients(id):
    if request.method == 'GET':
        # Show form
        data=Consultes.mostrar_clientes_individual(id)
        return render_template('clientela/update.html',data=data, id=id)
    
    elif request.method == 'POST':
        # Get POST data
        # TODO Save data (database insert)
        data = request.form
        CreacioyEliminacio.Actualitzacio(data,id)
        return redirect('/clientela/list')
    else:
        # Not found response
        abort(404)