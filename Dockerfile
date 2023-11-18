FROM python:3.12
ENV PYTHONUNBUFFERED=1

WORKDIR /src

RUN pip install poetry
# Jinja2テンプレートをDockerコンテナ内にinstall 
RUN pip install Jinja2

COPY pyproject.toml* poetry.look* ./

RUN poetry config virtualenvs.in-project true
RUN if [ -f pyproject.toml ]; then poetry install --no-root; fi

ENTRYPOINT [ "poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload" ]