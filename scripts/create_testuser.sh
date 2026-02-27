#!/bin/bash
# Create default test user (testuser / testpass123) in the local DB.
# Run from project root. Requires backend container running.

set -e
cd "$(dirname "$0")/.."

echo "Creating testuser (password: testpass123) if not present..."
docker exec vecenetwork-project-backend-1 bash -c "cd /src && .venv/bin/python -c \"
from tests.fake.db_data.main import ensure_testuser
ensure_testuser()
\"" 2>/dev/null && exit 0

# Fallback: run from host (need backend code and DB on localhost:5432)
(cd backend && POSTGRES_HOST=localhost POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres POSTGRES_DB=test uv run python -c "
import sys
sys.path.insert(0, 'src')
from tests.fake.db_data.main import ensure_testuser
ensure_testuser()
")
echo "Done. Login: testuser / testpass123"
