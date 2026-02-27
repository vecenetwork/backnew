#!/bin/bash
# Create VECE user (username: vece, password: testpass123) in the DB.
# Run from project root. Uses psycopg2 (no app dependencies).

set -e
cd "$(dirname "$0")/.."

echo "Creating vece user (username: vece, password: testpass123)..."
backend/.venv/bin/python scripts/seed_vece_user.py

echo "Done. Login: vece / testpass123"
