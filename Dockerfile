FROM python:3.10
ENV POETRY_VERSION=1.4.2
WORKDIR /code
COPY ./pyproject.toml /code/pyproject.toml
RUN pip install "poetry==$POETRY_VERSION"
RUN poetry update
COPY ./main.py /code/main.py
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
