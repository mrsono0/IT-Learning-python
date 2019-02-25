# IT-it_learning_python

### docker-infra

- Docker base python example project  

- IDE : vscode + 분석 라이브러리

```
    docker build -f Dockerfile.ide --tag mrsono0/it_learning_python:ide .
    docker run --rm -itd -p 33890:3389 -p 2222:22 mrsono0/it_learning_python:ide
    docker tag it_learning_python:ide mrsono0/it_learning_python:ide
    docker push mrsono0/it_learning_python:ide
```

- flask + 분석 라이브러리

```
    docker build -f Dockerfile.flask --tag mrsono0/it_learning_python:flask .
    docker run --rm -itd -p 80:80 -p 2222:22 mrsono0/it_learning_python:flask
    docker run --rm -it -e FLASK_APP=main.py -e FLASK_DEBUG=1 -p 80:80 -P mrsono0/base_project:flask_alpine flask run --host=0.0.0.0 --port=80
    docker tag it_learning_python:flask mrsono0/it_learning_python:flask
    docker push mrsono0/it_learning_python:flask

    https://hub.docker.com/u/petronetto
```

- jupyter + 분석 라이브러리

```
    docker build -f Dockerfile.jupyterlab --tag mrsono0/it_learning_python:jupyterlab .
    docker build -f Dockerfile.jupyter --tag mrsono0/it_learning_python:jupyter .
    docker run --rm -it -p 8888:8888 -e JUPYTER_ENABLE_LAB=pyspark mrsono0/it_learning_python:jupyterlab
    docker run --rm -it -p 8888:8888 -e JUPYTER_ENABLE_LAB=pyspark mrsono0/it_learning_python:jupyter
    docker tag it_learning_python:jupyterlab mrsono0/it_learning_python:jupyterlab
    docker push mrsono0/it_learning_python:jupyterlab
```

- docker compose cli command

```
    docker-compose -f ./docker-compose.yml up
    docker-compose -f ./docker-compose.yml run workspace
    docker-compose -f ./docker-compose.yml run workspace /bin/bash
    docker-compose -f ./docker-compose.yml stop workspace
    docker-compose -f ./docker-compose.yml restart workspace
    docker-compose -f ./docker-compose.yml logs
    docker-compose kill -s SIGINT
    docker cp ./app_flask flask:/workspace/app
```

```
docker commit it_learning_python_workspace
docker commit -a "Foo Bar <foo@bar.com>" -m "add hello.txt" hello-nginx hello:0.2
docker tag it_learning_python:jupyterlab mrsono0/it_learning_python:jupyterlab

```