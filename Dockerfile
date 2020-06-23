FROM python:3.8-alpine as base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"


FROM base as builder

RUN apk add --no-cache postgresql-dev gcc python3-dev musl-dev
RUN python -m venv /venv && pip install --upgrade pip && pip install pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy


FROM base as production

RUN apk add --no-cache libpq
WORKDIR /app

COPY --from=builder /venv /venv
COPY . /app
RUN python manage.py collectstatic --no-input

RUN addgroup -S app && adduser -S app -G app && chown app:app -R /app
USER app

ENTRYPOINT ["/app/entrypoint.sh"]
