from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rodizio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Participante(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    sala_id = db.Column(db.String(10), nullable=False)
    nome = db.Column(db.String(50), nullable=False)
    fatias = db.Column(db.Integer, default=0)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    sala_id = str(uuid.uuid4())[:8]
    return redirect(url_for('sala', sala_id=sala_id))

@app.route('/rodizio/<sala_id>')
def sala(sala_id):
    return render_template('sala.html', sala_id=sala_id)

@app.route('/api/sala/<sala_id>/dados')
def get_dados(sala_id):
    participantes = Participante.query.filter_by(sala_id=sala_id).order_by(Participante.fatias.desc()).all()
    # Enviamos o ID para o frontend poder comparar com o salvo no localStorage
    lista = [{'id': p.id, 'nome': p.nome, 'fatias': p.fatias} for p in participantes]
    return jsonify(lista)

@app.route('/api/entrar', methods=['POST'])
def entrar():
    dados = request.json
    novo = Participante(sala_id=dados['sala_id'], nome=dados['nome'])
    db.session.add(novo)
    db.session.commit()
    # RETORNAMOS O ID GERADO (Importante!)
    return jsonify({'status': 'ok', 'id': novo.id})

@app.route('/api/atualizar', methods=['POST'])
def atualizar():
    dados = request.json
    participante = Participante.query.get(dados['id'])
    if participante:
        if dados['acao'] == 'add':
            participante.fatias += 1
        elif dados['acao'] == 'remove' and participante.fatias > 0:
            participante.fatias -= 1
        db.session.commit()
    return jsonify({'status': 'ok'})