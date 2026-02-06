# 🍕 Contador de Rodízio (Pizza Counter)

> Uma aplicação web simples e divertida para contar fatias de pizza em tempo real entre amigos durante um rodízio.

![Status](https://img.shields.io/badge/Status-Concluído-success)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)

## 📸 Screenshots

![Screenshot do App](/print.jpg)

## 📖 Sobre o Projeto

Cansado de perder a conta de quantas fatias comeu no rodízio? Ou quer competir com seus amigos para ver quem é o maior "prejuízo" para o restaurante? 

O **Contador de Rodízio** resolve isso. Você cria uma sala, manda o link no grupo do WhatsApp e todos podem ver o placar atualizando em tempo real (via polling). O sistema identifica o usuário localmente, permitindo que cada um altere apenas o seu próprio contador.

## 🚀 Funcionalidades

- **Criação de Salas Instantânea:** Sem login, sem senha. Apenas um link único.
- **Identificação Automática:** O navegador lembra quem você é (via LocalStorage).
- **Controle de Permissão:** Você só vê os botões de `+` e `-` no seu próprio nome.
- **Atualização "Real-time":** A lista de participantes atualiza automaticamente a cada 2 segundos.
- **Compartilhamento:** Botão direto para enviar o link da sala no WhatsApp.
- **Design Responsivo:** Funciona perfeitamente no celular (Bootstrap 5).

## 🛠 Tecnologias Utilizadas

- **Backend:** Python (Flask)
- **Banco de Dados:** SQLite (com SQLAlchemy)
- **Frontend:** HTML5, CSS3 (Bootstrap 5), JavaScript (Fetch API)
- **Hospedagem Sugerida:** PythonAnywhere

## 📂 Estrutura do Projeto

```text
/
├── flask_app.py      # Lógica do servidor e rotas (Backend)
├── rodizio.db        # Banco de dados SQLite (gerado automaticamente)
└── templates/
    └── sala.html     # Interface do usuário (Frontend)
```

Hospedado temporariamente em: https://rmouradev1.pythonanywhere.com/

📦 Como Rodar Localmente
Pré-requisitos: Python 3 instalado.

Clone o repositório

Bash
git clone [https://github.com/SEU_USUARIO/contador-rodizio.git](https://github.com/SEU_USUARIO/contador-rodizio.git)

cd contador-rodizio
Crie um ambiente virtual (Opcional, mas recomendado)

Bash
python -m venv venv
# No Windows:
venv\Scripts\activate
# No Mac/Linux:
source venv/bin/activate
Instale as dependências

Bash
pip install flask flask-sqlalchemy
Execute o projeto

Bash
flask --app flask_app run
Acesse: Abra http://127.0.0.1:5000 no seu navegador.

☁️ Deploy no PythonAnywhere
Este projeto foi otimizado para rodar facilmente no PythonAnywhere.

Crie uma conta gratuita.

Em Web Apps, crie um novo app Flask.

Em Files, faça upload do flask_app.py e da pasta templates.

Instale as dependências no console do PythonAnywhere: pip install flask-sqlalchemy.

Recarregue o app e pronto!

🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

📝 Licença
Este projeto está sob a licença MIT.
