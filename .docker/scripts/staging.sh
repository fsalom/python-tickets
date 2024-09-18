#!/bin/bash

set -o errexit
set -o nounset

export DJANGO_SETTINGS_MODULE=boot.settings.staticfiles
export ALLOWED_HOSTS=chatbot-staging.rudo.es,localhost
export CSRF_TRUSTED_ORIGINS=https://chatbot-staging.rudo.es,http://localhost
export DEBUG=0
export AWS_ACCESS_KEY_ID=DO007WXZVEZGE8EKN6GK
export AWS_SECRET_ACCESS_KEY=wB116IkSPDt8ZFBMBboL+yi2HpdfuoDYqsOqVwpXJeo
export AWS_STORAGE_BUCKET_NAME=staging
export AWS_S3_ENDPOINT_URL=https://chat-bot-rudo.fra1.digitaloceanspaces.com
export POSTGRES_DB=chatbot
export POSTGRES_USER=admin
export POSTGRES_PASSWORD=vO9_opN2bONgWApvVzNS
export POSTGRES_HOST=postgres
export POSTGRES_PORT=5432
export DB_ENGINE=django.db.backends.postgresql
export API_ACCESS_TOKENS=VY2XjB6euy4wRW2hdvlok7PFWg1BlLVb,GoX4lhhP5roOx5QrLRBOEblL5CR0UX7Y,7ktw8mk8Q3dt2f2hCVOAArO8WOAMbRdd
export FIBONACCI=12358
export X=983647
