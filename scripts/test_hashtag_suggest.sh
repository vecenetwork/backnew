#!/bin/bash
# Test POST /hashtags/suggest (Gemini-based hashtag suggestion)
# Requires: GOOGLE_API_KEY in .env, server running, valid user credentials

BASE_URL="${BASE_URL:-http://localhost:8000/api}"

# Get token (adjust username/password as needed)
TOKEN=$(curl -s -X POST "${BASE_URL}/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=testuser&password=testpass123" | \
  grep -o '"access_token":"[^"]*' | cut -d'"' -f4)

if [ -z "$TOKEN" ]; then
  echo "Error: could not get token. Ensure server is running and user exists."
  exit 1
fi

QUESTION="${1:-What is your favorite programming language?}"
OPTIONS='["Python", "JavaScript", "Go", "Rust"]'

echo "=== Hashtag suggestion (Gemini) ==="
echo "Question: $QUESTION"
echo ""

curl -s -X POST "${BASE_URL}/hashtags/suggest" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"question_text\":\"$QUESTION\",\"options\":$OPTIONS}" \
  --max-time 30 | python3 -m json.tool 2>/dev/null || echo "Response (raw):" && \
curl -s -X POST "${BASE_URL}/hashtags/suggest" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"question_text\":\"$QUESTION\",\"options\":$OPTIONS}" \
  --max-time 30

echo ""
