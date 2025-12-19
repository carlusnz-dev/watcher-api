# Watch API

[![License: GNU](https://img.shields.io/badge/License-GNU-yellow.svg)](https://opensource.org/licenses-old/gpl-license-html)
[![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/carlusnz-dev/watcher-api/graphs/commit-activity)

Uma aplicação web completa para monitoramento de suas API's locais em seu ambiente construído com Flask e NextJS. O **Watcher API** permite automatizar a vigilância de mudanças em sites específicos de forma eficiente.

---

## 📌 Sumário

- [Sobre](#sobre)
- [Tecnologias](#tecnologias)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Contribuição](#contribuição)
- [Licença](#licença)

## 📖 Sobre

O Watcher API resolve o problema do monitoramento manual de API's que estão rodando localmente em seu ambiente. Ele utiliza do **requests** do Python para obter o status e log, posteriormente, salvando em um banco de dados e retornando no front-end.

- **Objetivos:** Notificar o usuário, em tempos determinados, o status atual da API.

- **Status:** Em desenvolvimento (Alpha).

---

## 🛠 Tecnologias

As principais ferramentas do projeto são:

- [Python](https://www.python.org) - Linguagem base
- [Flask](https://flask.palletsprojects.com/en/stable/) - Back-end
- [NextJS](https://nextjs.org/) - Front-end
- [Requests](https://requests.readthedocs.io/en/latest/) - Para obter status das url's
- [SQLAlchemy](https://flask-sqlalchemy.readthedocs.io/en/stable/) - Controle do banco de dados (SQLite)

## ⚙️ Instalação

Siga os passos para instalar e rodar o projeto.

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/carlusnz-dev/watcher-api.git](https://github.com/carlusnz-dev/watcher-api.git)
    cd watcher-api/server
    ```

2.  **Crie e ative o ambiente virtual:**

    ```bash
    python3 -m venv watcher_venv
    source watcher_venv/bin/activate  # Linux/macOS
    # No Windows: .\watcher_venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Rode o projeto**

---
