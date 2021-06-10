#! /bin/bash
echo "executing unit test in parallel"

docker-compose exec web pytest -k "unit" -n auto