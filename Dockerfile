FROM python:latest

RUN pip install poetry

RUN mkdir /code
WORKDIR /code

COPY . .
RUN rm -rf data.db .git
RUN poetry install
RUN pip install .

CMD ["mb"]
