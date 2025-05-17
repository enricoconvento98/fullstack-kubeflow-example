# backend/setup.py
from setuptools import setup, find_packages

setup(
    name="fullstack_kubeflow_backend",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi==0.68.1",
        "uvicorn==0.15.0",
        "sqlalchemy==1.4.23",
        "psycopg2-binary==2.9.1",
        "python-dotenv==0.19.0",
        "kfp-server-api==1.8.0"
    ],
)