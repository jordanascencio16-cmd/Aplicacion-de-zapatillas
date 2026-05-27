from flask import Flask,render_template,request

app=Flask(__name__)

reservas = []

@app.route('/')
def inicio():
    return render_template('inicio.html',reservas=reservas)

@app.route('/reservar',methods=['POST'])
def reservar():
    nombre=request.form['nombre']
    correo=request.form['correo']
    telefono=request.form['telefono']
    marca=request.form['marca']
    modelo=request.form['modelo']
    talla=request.form['talla']
    precio=request.form['precio']

    reserva=[nombre,correo,telefono,marca,modelo,talla,precio]
    reservas.append(reserva)

    return render_template('confirmacion.html', nombre=nombre,marca=marca,modelo=modelo,talla=talla,precio=precio,reservas=reservas)

app.run(debug=True)