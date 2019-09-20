# Battle For Castile: Match Enqueuer

[![Build Status](https://dev.azure.com/javidgon/Battleforcastile/_apis/build/status/battleforcastile.battleforcastile-match-enqueuer?branchName=master)](https://dev.azure.com/javidgon/Battleforcastile/_build/latest?definitionId=4&branchName=master)

This micro-service handles the enqueuing of pending matches
## 1. Installation and set up

> This guide assumes that there's a K8s cluster (with Helm-tiller).

#### 1.1 Run `helm install helm/battleforcastile-match-enqueuer --set rabbitmqpassword=... --set rabbitmquser=... --set secretkey=...` and in a few minutes it should be deployed! :)

* The value of `rabbitmqpassword` is the `base64` of the rabbitmq password
* The value of `rabbitmquser` is the `base64` value of the rabbitmq user
* The value of `secretkey` is the `base64` value of the secret key of your Flask App (can be random)
