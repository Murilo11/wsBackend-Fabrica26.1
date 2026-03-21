# 💼 wsBackend-Fabrica26.1 — Holding Familiar Crypto

Aplicação web para gestão de patrimônio familiar em criptomoedas. Permite cadastrar membros da família, registrar seus investimentos em cripto e calcular o patrimônio total em tempo real consumindo dados de preço da API CoinGecko.

---

## 🛠️ Tecnologias

- **Python 3.12** + **Django 6**
- **PostgreSQL 16** — banco de dados relacional
- **Docker** + **Docker Compose** — containerização
- **CoinGecko API** — preços de criptomoedas em tempo real (gratuita)

---

## ✅ Pré-requisitos

- [Docker](https://www.docker.com/) instalado
- [Docker Compose](https://docs.docker.com/compose/) instalado

---

## 🚀 Como rodar o projeto

**1. Clone o repositório:**
```bash
git clone https://github.com/SeuUsuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```

**2. Crie o arquivo `.env` na raiz com as variáveis:**
```
SECRET_KEY=sua-chave-secreta
DB_NAME=holding_db
DB_USER=postgres
DB_PASSWORD=suasenha123
DB_HOST=db
DB_PORT=5432
```

**3. Suba os containers:**
```bash
docker-compose build
docker-compose up
```

**4. Em outro terminal, aplique as migrations:**
```bash
docker-compose exec web python manage.py migrate
```

**5. Acesse no navegador:**
```
http://localhost:8000
```

---

## 📋 Funcionalidades

- Cadastro de membros da família (nome e parentesco)
- Cadastro de ativos em criptomoedas por membro
- Cálculo automático do patrimônio individual e total em BRL
- Preços atualizados em tempo real via CoinGecko
- CRUD completo de membros e ativos

---

## 🗂️ Estrutura do Projeto

```
wsBackend-Fabrica26.1/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
├── manage.py
├── core/               # Configurações do projeto
│   ├── settings.py
│   └── urls.py
└── portfolio/          # App principal
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── services.py
    └── templates/
```

---

## 📌 Observação

Os IDs de criptomoedas devem seguir o padrão da CoinGecko (letras minúsculas). Exemplos: `bitcoin`, `ethereum`, `solana`.