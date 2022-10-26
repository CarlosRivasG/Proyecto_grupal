from flask_crud.__init__ import app
from flask_crud.controllers import  usuarios,archivos

if __name__ == "__main__":
    app.run(debug=True)