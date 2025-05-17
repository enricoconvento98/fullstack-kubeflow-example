fullstack-kubeflow-example/
├── .vscode/
│   └── launch.json
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── config/
│   │   │   ├── __init__.py
│   │   │   ├── development.py
│   │   │   └── production.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── crud.py
│   │   └── api/
│   │       ├── __init__.py
│   │       ├── endpoints/
│   │       │   ├── pipeline.py
│   │       │   └── metrics.py
│   ├── requirements.txt
│   ├── dev-requirements.txt
│   ├── Dockerfile
│   ├── Dockerfile.dev
│   └── entrypoint.sh
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Dashboard.jsx
│   │   │   └── PipelineRun.jsx
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── setupProxy.js
│   ├── package.json
│   ├── Dockerfile
│   ├── Dockerfile.dev
│   └── nginx.conf
├── ml-pipelines/
│   ├── components/
│   │   ├── data_preprocess/
│   │   │   ├── src/
│   │   │   │   └── preprocess.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   ├── model_train/
│   │   │   ├── src/
│   │   │   │   └── train.py
│   │   │   ├── Dockerfile
│   │   │   └── requirements.txt
│   │   └── model_evaluate/
│   │       ├── src/
│   │       │   └── evaluate.py
│   │       ├── Dockerfile
│   │       └── requirements.txt
│   ├── pipelines/
│   │   └── full_pipeline.py
│   └── requirements.txt
├── scripts/
│   ├── setup-db.sh
│   └── init-kubeflow.sh
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── docker-compose.dev.yml
├── Makefile
└── README.md