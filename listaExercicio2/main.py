import json
import sqlite3
from flask import Flask
from flask import render_template
from flask import jsonify, redirect

app = Flask(__name__)

con = sqlite3.connect("agendaDb.db")

@app.route('/')
def index():
    return redirect('/agenda', code=302)

@app.route("/agenda", methods=["GET"])
def listarAgendas():
    con = sqlite3.connect("agendaDb.db")
    cursor = con.cursor()
    comando_sql = "SELECT * FROM contatos ORDER BY id"
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    return jsonify(dados)

@app.route("/incluirAgenda", methods=["POST"])
def incluirDados():
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = "INSERT INTO contatos (nome, empresa, telefone, email) values ('"+request.get_json().get('nome')+"', '"+request.get_json().get('empresa')+"', '"+request.get_json().get('telefone')+"', '"+ request.get_json().get('email')+"')"
        cursor.execute(comando_sql)
        con.commit()
        return jsonify("Sucesso!"), 200
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route("/alterarAgenda/<int:id>", methods=["PUT"])
def alterarDados(id):
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = f"UPDATE contatos SET nome = '"+request.get_json().get('nome')+"', empresa = '"+request.get_json().get('empresa')+"', telefone = '"+request.get_json().get('telefone')+"', email = '"+ request.get_json().get('email')+"' WHERE id = "+ str(id) +""
        cursor.execute(comando_sql)
        con.commit()
        return jsonify("Sucesso!"), 200
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route("/deletarAgenda/<int:id>", methods=["DELETE"])
def delearDados(id):
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = f"DELETE FROM contatos WHERE id = " + str(id) + ""
        cursor.execute(comando_sql)
        con.commit()
        return jsonify("Sucesso!"), 200
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route("/agendaNomes/<nome>", methods=["GET"])
def consultaNome(nome):
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = "SELECT nome FROM contatos WHERE nome LIKE '%" + str(nome) +"%'"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        return jsonify(dados)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route("/agendaEmpresas/<empresa>", methods=["GET"])
def consultaEmpresas(empresa):
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = "SELECT empresa FROM contatos WHERE empresa LIKE '%" + str(empresa) +"%'"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        return jsonify(dados)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

@app.route("/agendaEmails/<email>", methods=["GET"])
def consultaEmails(email):
    try:
        con = sqlite3.connect("agendaDb.db")
        cursor = con.cursor()
        comando_sql = "SELECT email FROM contatos WHERE email LIKE '%" + str(email) +"%'"
        cursor.execute(comando_sql)
        dados = cursor.fetchall()
        return jsonify(dados)
    except sqlite3.OperationalError:
        return jsonify("Erro de execução de query!"), 404

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)