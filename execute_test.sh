#! /bin/bash
echo "executing tests!"

docker-compose exec web python -m pytest