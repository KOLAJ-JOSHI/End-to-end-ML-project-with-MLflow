# End-to-end-ML-project-with-MLflow

## Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update main.py
9. Update app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/KOLAJ-JOSHI/End-to-end-ML-project-with-MLflow
```
### STEP 01- Connect with the python environment after opening the repository


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/KOLAJ-JOSHI/End-to-end-ML-project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=KOLAJ-JOSHI \
MLFLOW_TRACKING_PASSWORD=575e2e36158c71f7e753f7b54c0f5e9547bf8bf1 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/KOLAJ-JOSHI/End-to-end-ML-project-with-MLflow.mlflow \

export MLFLOW_TRACKING_USERNAME=KOLAJ-JOSHI 

export MLFLOW_TRACKING_PASSWORD=575e2e36158c71f7e753f7b54c0f5e9547bf8bf1

```

### Docker

Run this code in command prompt:
To build a docker image:- docker build -t demo-app

To run the docker image :- docker run -p 8080:8080 demo-app

To login docker in terminal :- docker login => To login into docker hub

To push docker image into docker repo :- docker push kolajjoshi/demo-app:latest


Pulling the docker image that has been pushed to docker hub:
docker pull kolajjoshi/demo-app