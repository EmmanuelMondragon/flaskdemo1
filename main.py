from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/catalogos')
def index():
    return jsonify({"proyectos": "Aqui se mostrara todos los proyectos disponibles"})



@app.route('/alta/proyecto')
def index():
    return jsonify({"proyecto": "Aqui dara de alta un proyecto"})


@app.route('/editar/proyecto')
def index():
    return jsonify({"proyecto": "Aqui se editaras un proyecto"})



if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
