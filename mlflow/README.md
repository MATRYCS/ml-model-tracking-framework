# ML Model Tracking Framework containers

To run the containers:

1. Make sure **Docker** and **docker-compose** are installed.
2. Copy `.env.example` into `.env` and adapt default values.
3. Run `docker-compose build` in terminal.
4. Run `docker-compose up` in terminal.

To access the services:

- MinIO at port [:9000](http://127.0.0.1:9000), web UI at port [:9001](http://127.0.0.1:9001)
- MLFlow web UI at port [:5000](http://127.0.0.1:5000)
