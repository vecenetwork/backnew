#!/bin/bash
# Seed demo questions from vece user. Run from project root.
set -e
cd "$(dirname "$0")/.."
backend/.venv/bin/python scripts/seed_demo_questions.py
