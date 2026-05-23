#!/bin/bash
set -euo pipefail

if [ -z "${1:-}" ]; then
    echo "usage: ./bakup.sh directory_path"
    exit 1
fi

SOURCE_DIR="$1"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: directory does not exist"
    exit 1
fi

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="backup_${TIMESTAMP}.tar.gz"

tar -czf "$BACKUP_FILE" "$SOURCE_DIR"

echo "$(date) Backup created : $BACKUP_FILE from $SOURCE_DIR" >> bakup.>
echo "backup created successfully : $BACKUP_FILE"