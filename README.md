# 🚀 BigID DevOps Home Assignment

## 📌 Overview

This project implements a simple web application that returns the client’s originating IP address and demonstrates a complete DevOps workflow including:

* Application development
* Containerization (Docker)
* Kubernetes deployment (Helm)
* CI/CD automation
* Security scanning

---

## 🧱 Architecture

```
Client → Kubernetes Service → Pod (Flask App)
                         ↓
                    Docker Image
                         ↓
                   CI/CD Pipeline
```

---

## 📁 Project Structure

```
bigid-devops-assignment/
│
├── app/
│   ├── main.py
│   ├── requirements.txt
│   └── test_main.py
│
├── Dockerfile
├── .dockerignore
│
├── charts/ip-app/
│   ├── Chart.yaml
│   ├── values.yaml
│   └── templates/
│       ├── deployment.yaml
│       ├── service.yaml
│       └── ingress.yaml (optional)
│
├── .github/workflows/ci.yml
└── README.md
```

---

## ⚙️ Application Details

### Endpoints

| Endpoint  | Description               |
| --------- | ------------------------- |
| `/`       | Returns client IP address |
| `/health` | Liveness probe endpoint   |
| `/ready`  | Readiness probe endpoint  |

---

## 🐳 Docker

### Build Image

```
docker build -t ip-app .
```

### Run Locally

```
docker run -p 8080:8080 ip-app
```

### Why Multi-Stage Build?

* Reduces final image size
* Improves security
* Separates build and runtime environments

---

## ☸️ Kubernetes Deployment

### Prerequisites

* Kubernetes cluster (Kind / Minikube)
* Helm installed

### Start Cluster

```
kind create cluster
```

OR

```
minikube start
```

---

### Deploy with Helm

```
helm upgrade --install ip-app charts/ip-app \
  --set image.repository=<your-dockerhub-username>/ip-app \
  --set image.tag=<tag>
```

---

### Verify Deployment

```
kubectl get pods
kubectl get svc
```

---

## 🔍 Health Check

```
curl http://<service-ip>/health
```

---

## ⚙️ Helm Configuration

All configurations are managed via `values.yaml`:

* Resource limits & requests
* Liveness & readiness probes
* Image repository and tag

### Example

```
resources:
  limits:
    cpu: 500m
    memory: 256Mi
```

---

## 🔐 Secrets Management

No secrets are hardcoded.

Supported approaches:

* Kubernetes Secrets
* External Secrets Operator
* Sealed Secrets

### Example

```
kubectl create secret generic app-secret \
  --from-literal=API_KEY=xxxx
```

---

## 🔄 CI/CD Pipeline

Implemented using **GitHub Actions**.

### Pipeline Stages

1. **Lint**
2. **Unit Tests**
3. **Build Docker Image**
4. **Security Scan (Trivy)**
5. **Push Image**
6. **Helm Lint**
7. **Deploy to Kubernetes**
8. **Smoke Test**

---

### Trigger

* On every `push`
* On every `pull request`

---

## 🧪 Testing

Run tests locally:

```
pytest app/
```

Pipeline fails if any test fails.

---

## 🔍 Security Scanning

Uses **Trivy** to scan container images.

* Detects vulnerabilities
* Can fail pipeline on HIGH/CRITICAL issues

---

## 🚦 Smoke Testing

After deployment:

```
kubectl port-forward svc/ip-app 8080:80 &
sleep 5
curl -f http://localhost:8080/health
```

Pipeline fails if:

* Service is unreachable
* Non-200 response

---

## 📦 Image Registry

Images are tagged using commit SHA:

```
<repo>/ip-app:<commit-sha>
```

Example:

```
docker push your-dockerhub/ip-app:abc123
```

---

## 🧠 Design Decisions

### Why Flask?

* Lightweight
* Minimal overhead
* Fast to implement

### Why Helm?

* Parameterized deployments
* Reusable templates
* Environment flexibility

### Why Trivy?

* Fast and widely adopted
* Easy CI integration

---

## 📈 Future Improvements

* Add Ingress for external access
* Implement HPA (Horizontal Pod Autoscaler)
* Add monitoring (Prometheus + Grafana)
* Use GitOps (ArgoCD / Flux)
* Add SBOM generation (Syft)

---

## ✅ Acceptance Criteria Coverage

| Requirement            | Status |
| ---------------------- | ------ |
| App with endpoints     | ✅      |
| Unit tests             | ✅      |
| Multi-stage Dockerfile | ✅      |
| Helm chart             | ✅      |
| CI/CD pipeline         | ✅      |
| Image scan (Trivy)     | ✅      |
| Smoke test             | ✅      |
| README documentation   | ✅      |

---

## 👨‍💻 How to Run End-to-End

```
# 1. Clone repo
git clone <repo-url>

# 2. Build image
docker build -t ip-app .

# 3. Start Kubernetes
kind create cluster

# 4. Deploy
helm upgrade --install ip-app charts/ip-app

# 5. Test
kubectl port-forward svc/ip-app 8080:80
curl http://localhost:8080/
```

---

## 📬 Submission Notes

* Repository contains all required components
* CI/CD pipeline fully automated
* Deployment verified with smoke tests
* Security scanning included

---

## 🙌 Conclusion

This project demonstrates a complete DevOps lifecycle:

* Code → Build → Scan → Deploy → Validate

Designed with production-grade practices and scalability in mind.

---
