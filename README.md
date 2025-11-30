## Support Veículos (Backend)

API REST para gerenciamento de anúncios de veículos, incluindo autenticação com JWT, CRUD completo de anúncios e upload de múltiplas fotos por anúncio.

## 🚀 Tecnologias Utilizadas

Python 3.12+

Django 5

Django Rest Framework (DRF)

Djoser (registro/login com JWT)

Simple JWT

SQLite (ambiente de desenvolvimento)

Pillow (upload de imagens)

## 📦 Funcionalidades da API
## 🔐 Autenticação

Registro de usuários

Login com JWT

Refresh de token

Recuperação e alteração de senha (por Djoser)

## 🚘 Anúncios

Criar anúncio (autenticado)

Listar anúncios (público)

Buscar anúncio por ID (público)

Editar somente se for dono do anúncio

Excluir somente se for dono do anúncio

## 🖼️ Fotos do Anúncio

Cada anúncio pode conter várias fotos.

Adicionar foto (autenticado + dono)

Listar fotos do anúncio

Excluir foto (autenticado + dono)

Upload em multipart/form-data

## 📁 Estrutura do Projeto
supportveiculos-backend/
│
├── anuncios/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py (não utilizado)
│
├── core/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── media/
└── manage.py

## ⚙️ Instalação e Setup
## 1️⃣ Clone o projeto
git clone https://github.com/seu-repo/supportveiculos-backend.git
cd supportveiculos-backend

## 2️⃣ Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows

## 3️⃣ Instale as dependências
pip install -r requirements.txt

## 4️⃣ Execute migrações
python manage.py migrate

## 5️⃣ Execute o servidor
python manage.py runserver

## 🔑 Autenticação (Djoser + JWT)
## ➤ Criar usuário

POST /api/auth/users/

Body:

{
  "username": "teste",
  "password": "123456"
}

## ➤ Login

POST /api/auth/jwt/create/

{
  "username": "teste",
  "password": "123456"
}


Retorno:

{
  "refresh": "token...",
  "access": "token..."
}


Use o token no header:

Authorization: Bearer SEU_TOKEN

## 🚘 Rotas de Anúncios
➤ Listar anúncios (público)

GET /api/anuncios/

## ➤ Buscar anúncio

GET /api/anuncios/<id>/

## ➤ Criar anúncio (autenticado)

POST /api/anuncios/

Exemplo:

{
  "titulo": "Honda Civic 2010",
  "descricao": "Carro conservado",
  "preco": 35000,
  "marca": "Honda",
  "modelo": "Civic",
  "ano": 2010,
  "km": 120000,
  "telefone_contato": "14998887766"
}

## ➤ Editar anúncio

PATCH /api/anuncios/<id>/

## ➤ Excluir anúncio

DELETE /api/anuncios/<id>/

## 🖼️ Rotas de Fotos
## ➤ Adicionar foto (autenticado + dono)

POST /api/anuncios/<id>/adicionar_foto/
Form-data:

imagem: (FILE)
ordem: 1

## ➤ Listar fotos do anúncio

GET /api/anuncios/<id>/listar_fotos/

## ➤ Excluir foto

DELETE /api/anuncios/<id>/deletar-foto/<foto_id>/

## 🔒 Regras de Permissão
Ação	            Permissão
Listar anúncios	    Público
Ver detalhes	    Público
Criar anúncio	    Autenticado
Editar anúncio	    Somente o dono
Excluir anúncio	    Somente o dono
Adicionar foto  	Somente o dono
Listar fotos	    Público
Excluir foto	    Somente o dono

Implementado via:

IsAuthenticatedOrReadOnly

IsOwnerOrReadOnly

Checagem manual no método da view

## 🗂️ Media Files

As imagens ficam em:

/media/fotos/


Servidas automaticamente em DEBUG=True.

## 🌐 Rotas principais
/api/anuncios/                         → CRUD de anúncios
/api/anuncios/<id>/adicionar_foto/     → upload de foto
/api/anuncios/<id>/listar_fotos/       → lista fotos
/api/anuncios/<id>/deletar-foto/<id>/  → remove foto

/api/auth/users/                       → registro
/api/auth/jwt/create/                  → login
/api/auth/jwt/refresh/                 → refresh token

## 🚀 Preparando para Deploy (Checklist)

✔ Ativar DEBUG=False
✔ Configurar ALLOWED_HOSTS
✔ Configurar CORS (se houver frontend separado)
✔ Configurar o caminho para MEDIA_ROOT
✔ Instalar Gunicorn (Linux)
✔ Criar pasta de mídia no servidor
✔ Definir SECRET_KEY segura
✔ Criar superuser no ambiente de produção

## 🧪 Testes

## Testes manuais foram executados em todas as rotas:

autenticação (OK)

criar anúncio (OK)

listar anúncios (OK)

detalhe do anúncio (OK)

editar somente se dono (OK)

excluir somente se dono (OK)

upload de fotos (OK)

listar fotos (OK)

excluir foto (OK)

Tudo 100% funcionando.

## Autor
Lucas Tamborim — GitHub

## Licença
MIT License