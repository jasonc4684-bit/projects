#!/bin/bash

# Time (seconds) with no changes before committing
IDLE=40

# Minimum time (seconds) between pushes
MIN_PUSH_INTERVAL=120

last_change=$(date +%s)
last_push=$(date +%s)

while true; do
    # Detect working directory or staged changes
    if ! git diff --quiet || ! git diff --cached --quiet; then
        last_change=$(date +%s)
    fi

    now=$(date +%s)
    elapsed=$((now - last_change))
    since_last_push=$((now - last_push))

    # Commit + push only if idle AND enough time since last push
    if [ $elapsed -ge $IDLE ] && [ $since_last_push -ge $MIN_PUSH_INTERVAL ]; then
        git add -A

        # Only commit if staged changes exist
        if ! git diff --cached --quiet; then
            git commit -m "auto-sync $(date '+%Y-%m-%d %H:%M:%S')"
        fi

        branch