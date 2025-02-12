# TLDR GCP

| **Service**           | **Type**                                         | **Use Case**                                               | **Best For** |
|----------------------|------------------------------------------------|----------------------------------------------------------|--------------|
| **GKE (Google Kubernetes Engine)** | Managed Kubernetes (Containers & Microservices Orchestration) | Large-scale containerized apps, Stateful apps, Kubernetes workloads | Complex microservices, Stateful applications, Custom networking |
| **Cloud Run**        | Serverless Containers (CaaS - Containers as a Service) | Stateless workloads, APIs, Batch jobs | Auto-scaling APIs, event-driven workloads, and microservices without Kubernetes complexity |
| **Cloud Functions**  | Serverless Functions (FaaS - Function as a Service) | Event-driven tasks, Webhooks, Lightweight APIs | Simple event-driven apps, background tasks, quick computations |

## GKE use case

Large-scale e-commerce platforms with microservices.  
AI/ML workloads requiring GPU and stateful processing.  
Financial applications needing high security and compliance.  

## Cloud run

REST APIs & microservices without Kubernetes overhead.  
Batch jobs (e.g., processing images, videos, or logs).  
Serverless CI/CD pipelines (running containerized builds on demand).  

## cloud functions

Webhooks for processing payments or notifications.  
Triggering functions when a file is uploaded to Cloud Storage.  
Real-time event processing (e.g., logging, monitoring, and chatbots).  
