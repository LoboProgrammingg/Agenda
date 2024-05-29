# Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact

# Configurar o git

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT

# Commitando
git add .
git commit -m 'Criando o app contact'
git push origin main -u ou git push

# Migrando a base de dados do Django

python manage.py makemigrations / Nao necessita usar se ja tiver o migrations
python manage.py migrate

# Criando e modificando a senha de um super usuário Django

python manage.py createsuperuser
python manage.py changepassword nomedousuario


