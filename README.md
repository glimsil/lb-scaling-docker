# lb-scaling-docker
To simply run the application, just type:
    `docker-compose up -d`
The app will serve on port 4000 (localhost:4000)
To scale up type (ex: 5 containers):
    `docker-compose up -d --scale app=5`