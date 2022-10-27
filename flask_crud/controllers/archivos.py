from flask_crud.utils.utils import download_file
from flask import redirect, render_template, request, flash, session,url_for,jsonify
from flask_crud.__init__ import app
from werkzeug.utils import secure_filename
from flask_crud.utils.utils import allowed_file
import os
from flask_crud.models import archivo
import csv

@app.route("/panel")
def panel():
    if 'usuario_nombre' not in session:
        flash('Primero tienes que logearte', 'error')
        return redirect('/login')
    return render_template("panel.html")

@app.route('/file/process',methods=['GET','POST'])
def upload_file():
    if request.method == 'GET':
        return flash('Something went wrong','error')
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No hay archivos','error')
            return redirect('/panel')
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No hay archivos seleccionados','error')
            return redirect('/panel')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("Record was successfully added",'success')
            data = {}
            col = []
            file = url_for('download_file',name=filename)
            with open(file) as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    col.append(row)
                    line_count += 1
            data = {
                "header": col[0],
                "body": col[1:]
            }
            return jsonify(data)
        
    flash('Hasta aca llega la funcion upload','info')
    return redirect('panel')

@app.route('/building/graphics')
def building_graphics():
    return render_template('grafico.html')
        
@app.route('/graphics/<filename>')
def graphics(filename):
    data = {}
    col = []
    file = url_for('download_file',name=filename)
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            col.append(row)
            line_count += 1
    data = {
        "header": col[0],
        "body": col[1:]
    }
    #archivo.File.save_file(saving_data)
    #datos_grafico = archivo.File.get_file_by_name(file)
    return jsonify(data)



