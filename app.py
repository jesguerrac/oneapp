from flask import Flask
from routes import getRoutes

app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecretkey'  # Clave secreta para manejar formularios
#coments
getRoutes(app)

if __name__ == '__main__':
    app.run(debug=True)
