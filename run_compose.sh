#! /bin/bash
echo "running docker-compose"
docker-compose up --build -d
docker-compose exec web python app/db.py
docker-compose logs