FROM python:3.7-slim

COPY ./requirements.txt .
RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

RUN groupadd app && useradd -g app app

COPY --chown=app:app . .

USER app

CMD python -u app.py
