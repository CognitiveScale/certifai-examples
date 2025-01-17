# How to deploy the "containerized" model to Kubernetes?

## Pre-requisites
- A Containerized model.
- `kubectl`.
- Private docker registry to push containerized image to.
- A valid `kubeconfig` file with the current context activated.
- To generate the deployment yaml using the provided template:
  - Python 3, Jinja2 and PyYAML (`pip install Jinja2 PyYAML`)


## Step 1 - Push image to registry (private)
The containerized image that has been built will need to be pushed to a private docker registry in order for the `k8s` cluster to pull it from.

### Pre-requisites
- Private docker registry to push containerized image to. This should be the registry that your`k8s` cluster is configured with.
- Make sure you have write-access to the registry and are authenticated.

### Tag docker image
```
docker tag <docker-image> <your-private-registry-url>:<docker-image-with-tag>
```

### Push the image
```
docker push <your-private-registry-url>:<docker-image-with-tag>
```

## Step 2 - Update deployment configuration and credentials
Update `MODEL_PATH`,  `METADATA_PATH`, cloud storage credentials (e.g s3)
and the `docker image` name in the `generated-container-model/deployment.yml` file.
Below is the snippet from `generated-container-model/deployment.yml` that needs to be updated:
```
spec:
  containers:
    - image: "<your-docker-image>"
      imagePullPolicy: IfNotPresent
      name: {{DEPLOYMENT_NAME}}
      ports:
        - containerPort: 8551
          protocol: TCP
      env:
        - name: MODEL_PATH
          value: "s3://bucket/model.pkl"
        - name: METADATA_PATH
          value: "s3://bucket/metadata.yml"
        - name: BUCKET_ENDPOINT
          value: "<your-s3-bucket-endpoint>"
        - name: BUCKET_SECRET_KEY
          value: "<your-s3-secret-key>"
        - name: BUCKET_ACCESS_KEY
          value: "<your-s3-access-key>"
```

## Step 3 - Deploy
Run the following command in order to deploy the resources mentioned in the `generated-container-model/deployment.yml` file:

Create the namespace (if it doesn't exist already)
```
kubectl create namespace <namespace-name>
```

```
kubectl apply -f generated-container-model/deployment.yml
```

This command will deploy a `Service` and a `Deployment` under the namespace specified in the `generated-container-model/deployment.yml` file (`containermodel` by default).


## Step 4 - Running a remote scan

### Pre-requisites
- datasets have to be in cloud storage (`s3`) and accessible by the same credentials that the scanner uses for writing reports; "datasets" section in the scan definition needs to be point to this cloud storage URL.
- model artifact has to be pushed; model deployment restarted on update of artifact

### Update Scan definition file with valid endpoints
Update `predict_endpoint` field under `models` section in your `scan_definition.yaml` file to the service endpoint. The service endpoint can be created as follows:

`http://<service-name>.<namespace>.svc.cluster.local:8551/predict`

`<service-name>` : should be the same as `metadata.name` under `kind:Service` in `generated-container-model/deployment.yml` file.
`<namespace` : `containermodel` (default namespace)

### SSH into the bastion host
This step is only needed if you don't have access to kubernetes from your local machine. SSH into the bastion host which has access to the k8s cluster.

If you have local access, then install certifai packages from `packages/all` folder inside the toolkit.
```
pip install cortex-certifai-common*.zip
pip install cortex-certifai-client*.zip
```

Note: Follow [this link](https://cognitivescale.github.io/cortex-certifai/docs/toolkit/setup/install-certifai-cli-lib/) for install/setup instructions

### Configure remote scan
Follow the docs [here](https://cognitivescale.github.io/cortex-certifai/docs/toolkit/cli-usage/remote-config-import) to configure certifai remote configuration and create an alias


### Trigger the remote scan
`certifai remote scan -f <path-to-scan-definition> -o --alias <alias>`

## Step 5 -  View Scan results
- Follow the docs [here](https://cognitivescale.github.io/cortex-certifai/docs/toolkit/console/console) to view scan status/results
