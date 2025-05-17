# Fullstack Kubeflow Example

A comprehensive example of a full-stack machine learning application using Kubeflow, FastAPI, and React. This project demonstrates how to build and deploy ML pipelines with a modern web interface.

## Overview

This project consists of three main components:
- **Frontend**: React-based web interface for pipeline management and visualization
- **Backend**: FastAPI service handling ML pipeline operations and metrics
- **ML Pipelines**: Kubeflow pipeline components for data preprocessing, model training, and evaluation

## Prerequisites

- Docker and Docker Compose
- Kubernetes cluster with Kubeflow installed
- Python 3.8+
- Node.js 16+

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/fullstack-kubeflow-example.git
   cd fullstack-kubeflow-example
   ```

2. Initialize Kubeflow and setup the database:
   ```bash
   make init-kubeflow
   make setup-db
   ```

3. Start the development environment:
   ```bash
   make dev
   ```

The application will be available at:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Project Structure

```
fullstack-kubeflow-example/
├── backend/                 # FastAPI backend service
│   ├── src/                # Source code
│   └── Dockerfile          # Container definition
├── frontend/               # React frontend application
│   ├── src/                # Source code
│   └── Dockerfile          # Container definition
├── ml-pipelines/           # Kubeflow pipeline components
│   ├── components/         # Individual pipeline steps
│   └── pipelines/         # Pipeline definitions
└── scripts/               # Utility scripts
```

## Development

### Backend Development
```bash
# Start backend in development mode
make backend-dev
```

### Frontend Development
```bash
# Start frontend in development mode
make frontend-dev
```

### ML Pipeline Development
```bash
# Build pipeline components
make build-pipeline-components

# Compile and upload pipeline
make upload-pipeline
```

## Production Deployment

1. Build production images:
   ```bash
   make build
   ```

2. Deploy to production:
   ```bash
   make deploy
   ```

## Contributing

Contributions are welcome! Please read our contributing guidelines and submit pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.