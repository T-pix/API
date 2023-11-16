import pandas as pd 
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def online():
    return 'Api ta on'

@app.route('/valortotal')
def valortotal():
    tabela = pd.read_csv('cpu.csv')
    valor_total = tabela['valor'].sum()
    resultado = {'valor_total': valor_total}
    return jsonify(resultado)
    
app.run(host='0.0.0.0')

