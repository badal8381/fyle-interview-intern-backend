#!/bin/bash

# to stop on first error
set -e

# Delete older .pyc files
# find . -type d \( -name env -o -name venv  \) -prune -false -o -name "*.pyc" -exec rm -rf {} \;

# Run required migrations
export FLASK_APP=core/server.py

# flask db init -d core/migrations/
# flask db migrate -m "Initial migration." -d core/migrations/
if [ -f "core/store.sqlite3" ]; then
    rm core/store.sqlite3
fi
flask db upgrade -d core/migrations/ && pytest --cov -vvv -s tests/
# flask db upgrade -d core/migrations/ && pytest -vvv -s tests/

# Run server
gunicorn -c gunicorn_config.py core.server:app
