from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Estrutura para armazenar os registros na memória
registros = []

# Página inicial para mostrar o histórico e os botões de ponto
@app.route('/')
def index():
    return render_template('index.html', registros=registros)

# Rota para bater ponto de entrada
@app.route('/bate_ponto_entrada', methods=['POST'])
def bate_ponto_entrada():
    nome = request.form['nome']
    hora_entrada = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    registros.append({'nome': nome, 'entrada': hora_entrada, 'saida': None})
    return redirect(url_for('index'))

# Rota para bater ponto de saída
@app.route('/bate_ponto_saida', methods=['POST'])
def bate_ponto_saida():
    nome = request.form['nome']
    for registro in reversed(registros):
        if registro['nome'] == nome and registro['saida'] is None:
            registro['saida'] = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            break
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
