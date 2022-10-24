from flask import redirect, render_template, request, flash, session
from flask_crud import app
from flask_crud.models.pintura import Pintura



@app.route("/panel")
def index():

    if 'usuario' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')
    
    return render_template("panel.html")

