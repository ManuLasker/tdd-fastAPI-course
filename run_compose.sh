#! /bin/bash
echo "running docker-compose"
docker-compose up --build -d

sleep 5

docker-compose exec web python app/db.py

sleep 5

docker-compose logs
