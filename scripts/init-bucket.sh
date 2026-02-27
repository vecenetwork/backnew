#!/bin/sh
set -e

# Create bucket if it doesn't exist
BUCKET_NAME=vece
if ! mc ls minio/$BUCKET_NAME > /dev/null 2>&1; then
  mc mb minio/$BUCKET_NAME
  echo "Bucket '$BUCKET_NAME' created"
else
  echo "Bucket '$BUCKET_NAME' already exists"
fi