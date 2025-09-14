# wsBackend-Fabrica25.2
Desafio Backend Fábrica de Software 2025.2

# 📖 Pokédex Django Project

Este projeto é uma aplicação Django que consome a [PokéAPI](https://pokeapi.co/) para cadastrar, listar e gerenciar Pokémon e seus movimentos.  
Ele oferece tanto uma interface web quanto uma API REST.

---

## 🚀 Funcionalidades

- Inserir Pokémon pelo nome (dados puxados automaticamente da PokéAPI)
- Listar todos os Pokémon cadastrados
- Ver detalhes completos de um Pokémon (tipos, altura, peso, habilidades, localização, evolução e movimentos)
- Editar Pokémon cadastrados
- Excluir Pokémon
- API REST para acessar os dados no formato JSON

---

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/)
- [PokéAPI](https://pokeapi.co/)

---

## 📂 Estrutura do projeto

```
desafio/
│── app/
│   ├── api/
│   │   ├── serializers.py      # Serializers DRF
│   │   ├── viewsets.py         # Views e ViewSets
│   ├── migrations/             # Migrações do banco
│   ├── templates/              # Templates HTML
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── pokemon_detail.html
│   │   ├── pokemon_lista.html
│   │   ├── pokemon_update.html
│   ├── forms.py                # Formulários Django
│   ├── models.py               # Modelos Pokémon e Moves
│   ├── apps.py                 # Configuração da aplicação
│
│── desafio/
│   ├── settings.py             # Configurações Django
│   ├── urls.py                 # Rotas principais
│   ├── wsgi.py                 # Configuração WSGI
│   ├── asgi.py                 # Configuração ASGI (se necessário)
│
│── manage.py                   # CLI Django
│── requirements.txt            # Dependências do projeto
```

---

## ⚙️ Como rodar o projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seu-usuario/pokedex-django.git
cd pokedex-django
```

### 2️⃣ Criar e ativar ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate    # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Rodar migrações
```bash
python manage.py migrate
```

### 5️⃣ Iniciar o servidor
```bash
python manage.py runserver
```

O projeto estará disponível em:  
👉 [http://127.0.0.1:8000/home/](http://127.0.0.1:8000/home/) (interface web)  
👉 [http://127.0.0.1:8000/api/pokemon/](http://127.0.0.1:8000/api/pokemon/) (API REST)

---

## 📌 Endpoints da API

- `GET /api/pokemon/` → Lista todos os Pokémon
- `POST /api/pokemon/` → Cria um novo Pokémon (apenas com `name`)
- `GET /api/pokemon/{id}/` → Detalhes de um Pokémon
- `PUT /api/pokemon/{id}/` → Atualiza um Pokémon
- `DELETE /api/pokemon/{id}/` → Exclui um Pokémon

---

## 🗄️ Modelos principais

### Pokémon
- `name`
- `pokedex_id`
- `type1`
- `type2`
- `height`
- `weight`
- `location`
- `evolution_chain`
- `abilities`

### Moves
- `name`
- `type`
- `category`
- `power`
- `accuracy`
- `pp`
- `pokemon (ForeignKey)`

---

## 🎨 Interface Web

- **Home**: formulário para inserir um Pokémon
- **Lista**: mostra todos os Pokémon cadastrados com ações (detalhes, editar, excluir)
- **Detalhes**: informações completas de um Pokémon e seus movimentos
- **Editar**: formulário para alterar dados
- **Excluir**: remoção de Pokémon

---

## 🧑‍💻 Autor

Projeto desenvolvido como desafio prático em Django + DRF.  
Feito por William Barreto 🚀
