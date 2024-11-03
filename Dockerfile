# Usar a imagem base oficial do Python
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do container
WORKDIR /app

# Instalar dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Instalar o Poetry
RUN pip install poetry

# Copiar o arquivo pyproject.toml e poetry.lock para o container
COPY pyproject.toml poetry.lock ./

# Instalar as dependências do Poetry sem os grupos de desenvolvimento e documentação
RUN poetry install --no-root --without dev
RUN 
# Copiar o restante dos arquivos do projeto para o container
COPY . .

# Definir variáveis de ambiente
ENV PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    DJANGO_SETTINGS_MODULE=core.settings \
    PYTHONPATH=/app

# Copiar o script de entrada
COPY entrypoint.sh /app/entrypoint.sh

# Dar permissão de execução para o script
RUN chmod +x /app/entrypoint.sh

# Expor a porta 8000
EXPOSE 8000

# Rodar o script de entrada
ENTRYPOINT ["/app/entrypoint.sh"]