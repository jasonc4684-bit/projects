#!/bin/bash
IDLE=40
last_change=$(date +%s)

while true; do
    if ! git diff --quiet || ! git diff --cached --quiet; then
        last_change=$(date +%s)
    fi

    now=$(date +%s)
    elapsed=$((now - last_change))

    if [ $elapsed -ge $IDLE ]; then
        git add -A
        if ! git diff --cached --quiet; then
            git commit -m "auto-sync $(date '+%Y-%m-%d %H:%M:%S')"
        fi
        branch=$(git rev-parse --abbrev-ref HEAD)
        git push origin "$branch"
        last_change=$(date +%s)
    fi

    sleep 2
done

