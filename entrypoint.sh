#!/bin/bash
# Exit the script if any command fails
set -e

# Rodar as migrações do banco de dados
echo "Running migrations..."
poetry run python manage.py migrate

# Criar um superusuário
echo "Creating superuser..."
poetry run python create_superuser.py

# Rodar o populate
echo "Running populate script..."
poetry run python manage.py populate

# Iniciar o servidor Django
echo "Starting Django server..."
poetry run python manage.py runserver 0.0.0.0:8000
