from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')

def inicio():
    lista = ['Jogo 1', 'Jogo 2', 'Jogo 3']
    return render_template('lista.html',titulo='Jogos', jogos=lista)

app.run(host='0.0.0.0', port=8080)