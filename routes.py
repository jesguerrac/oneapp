from flask import render_template, request, jsonify
from utils import construir_objeto

def getRoutes(app):
    @app.route('/', methods=['GET', 'POST'])
    def home():
        if request.method == 'POST':
            texto = request.form['texto']
            # Usar la función para construir el objeto
            resultado = construir_objeto(texto)
            return jsonify(resultado)
        return render_template('index.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
