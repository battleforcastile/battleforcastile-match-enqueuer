# Battle For Castile: Match Enqueuer

This micro-service handles the enqueuing of pending matches
## 1. Installation and set up

> This guide assumes that there's a K8s cluster (with Helm-tiller).

#### 1.1 First, deploy `rabbitmq` Chart
```
helm install stable/rabbitmq --name rabbitmq
```

#### 1.2 Go to `/helm/battleforcastile-match-enqueuer/` folder and copy the content from `templates-examples` to `templates`
```
cp helm/battleforcastile-match-enqueuer/templates-examples/* helm/battleforcastile-match-enqueuer/templates/*
```

#### 1.3 Uncomment the content from `battleforcastile-match-enqueuer-secrets.yml` (from `templates`) and replace:
 - The value of `secret_key` by the `base64` value of the secret key of your Flask App (can be random)

#### 1.4 Run `helm install helm/battleforcastile-match-enqueuer` and in a few minutes it should be deployed! :)
