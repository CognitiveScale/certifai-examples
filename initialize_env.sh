#!/bin/bash -eu
#
mkdir -p artifacts
touch artifacts/.azure_env
echo "export AML_USE_SP_AUTH=1
export AML_TENANT_ID=${CERTIFAI_AZURE_DEV_TENANT_ID}
export AML_PRINCIPAL_ID=${CERTIFAI_AZURE_DEV_CLIENT_ID}
export AML_PRINCIPAL_PASS=${CERTIFAI_AZURE_DEV_SECRET_KEY}
export CERTIFAI_AZURE_DEV_WORKSPACE_NAME=${CERTIFAI_AZURE_DEV_WORKSPACE_NAME}
export CERTIFAI_AZURE_DEV_RESOURCE_GROUP=${CERTIFAI_AZURE_DEV_RESOURCE_GROUP}
export CERTIFAI_AZURE_DEV_SUBSCRIPTION=${CERTIFAI_AZURE_DEV_SUBSCRIPTION}" > artifacts/.azure_env

touch artifacts/.aws_env
echo "CERTIFAI_DEV_AWS_ACCESS_KEY=${CERTIFAI_DEV_AWS_ACCESS_KEY}
CERTIFAI_DEV_AWS_SECRET_KEY=${CERTIFAI_DEV_AWS_SECRET_KEY}
CERTIFAI_DEV_AWS_ROLE_ARN=${CERTIFAI_DEV_AWS_ROLE_ARN}" > artifacts/.aws_env