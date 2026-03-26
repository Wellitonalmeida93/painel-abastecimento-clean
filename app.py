from flask import Flask, jsonify
from datetime import datetime
import requests

app = Flask(__name__)

URL = "https://srv1.ticketlog.com.br/ticketlog-servicos/ebs/transacaoVeiculo/search"
AUTHORIZATION = "Basic W09wZXJhZG9yV2ViXWFwcDEyMjg0MDQxOTg4OjExO1BTVG55"
CODIGO_CLIENTE = 122840


def consultar():
    hoje = datetime.now()
    inicio_mes = hoje.replace(day=1)

    data_inicio = inicio_mes.strftime("%Y-%m-%dT00:00:00")
    data_fim = hoje.strftime("%Y-%m-%dT23:59:59")

    payload = {
        "codigoCliente": CODIGO_CLIENTE,
        "codigoTipoCartao": 4,
        "dataTransacaoInicial": data_inicio,
        "dataTransacaoFinal": data_fim,
        "considerarTransacao": "T",
        "ordem": "S",
        "validacao": "S"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": AUTHORIZATION
    }

    try:
        response = requests.post(URL, json=payload, headers=headers, timeout=30)

        print("STATUS:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            return data.get("transacoes", [])

        return []

    except Exception as e:
        print("ERRO:", str(e))
        return []


@app.route("/")
def home():
    return "API TicketLog 🚀"


@app.route("/api/transacoes")
def transacoes():
    dados = consultar()
    return jsonify(dados)


if __name__ == "__main__":
    app.run()
