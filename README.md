# 🚀 DevOps Microservices Project

A production-style **end-to-end DevOps pipeline** demonstrating containerization, CI/CD automation, and Kubernetes orchestration.

---

## 📌 Overview

This project illustrates how modern applications are built, packaged, and deployed using industry-standard DevOps practices.

---

## 🏗️ Architecture Diagram

```text
          Developer
              │
              ▼
          GitHub Repo
              │
              ▼
        Jenkins Pipeline
      (CI/CD Automation)
              │
     ┌────────┴────────┐
     ▼                 ▼
Docker Build      Docker Push
     │                 │
     └────────┬────────┘
              ▼
        Kubernetes Cluster
         (Minikube Local)
              │
              ▼
           Service
              │
              ▼
           Ingress
              │
              ▼
            User
   (http://microservices.local)
```

---

## ⚙️ Technology Stack

* **Backend:** Node.js
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube)
* **CI/CD:** Jenkins
* **Networking:** Ingress

---

## 📂 Project Structure

```bash
DevOps-Microservices-Project/
│
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   └── ingress.yaml
│
├── Dockerfile
├── Jenkinsfile
├── package.json
├── app.js
└── README.md
```

---

## 🚀 Setup & Execution

### 1. Clone Repository

```bash
git clone <your-repo-url>
cd DevOps-Microservices-Project
```

---

### 2. Start Kubernetes Cluster

```bash
minikube start
```

---

### 3. Deploy Application

```bash
kubectl apply -f k8s/
```

---

### 4. Verify Deployment

```bash
kubectl get pods
kubectl get svc
```

---

### 5. Access Application

```bash
minikube service microservices-service
```

---

## 🌐 Ingress Configuration

### Enable Ingress Controller

```bash
minikube addons enable ingress
```

---

### Apply Ingress Resource

```bash
kubectl apply -f k8s/ingress.yaml
```

---

### Map Domain (Hosts File)

```text
<minikube-ip> microservices.local
```

---

### Access via Browser

```text
http://microservices.local
```

---

## 🔄 CI/CD Pipeline Flow

```text
1. Developer pushes code to GitHub
2. Jenkins pipeline is triggered
3. Docker image is built
4. Image is pushed to DockerHub
5. Kubernetes deployment is updated
6. Application is redeployed automatically
```

---

## ⚙️ Jenkins Pipeline (Command Flow)

```bash
# Build Docker Image
docker build -t <dockerhub-username>/microservices-app .

# Login to DockerHub
docker login

# Push Image
docker push <dockerhub-username>/microservices-app

# Deploy to Kubernetes
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

## 📊 Kubernetes Lifecycle

```text
Deployment → ReplicaSet → Pods → Service → Ingress
```

---

## 🎯 Key Features

* Automated CI/CD pipeline using Jenkins
* Dockerized application for consistency
* Kubernetes-based deployment and scaling
* Ingress-based domain routing
* Production-like architecture in local environment

---

## 📈 Scalability Example

```bash
kubectl scale deployment microservices-app --replicas=4
```

---

## 📌 Future Enhancements

* Multi-service architecture (User, Product, Order)
* Monitoring with Prometheus & Grafana
* Cloud deployment (AWS EKS)
* Helm-based deployments

---

## 👨‍💻 Author

**Ashwini Gidaveer**
