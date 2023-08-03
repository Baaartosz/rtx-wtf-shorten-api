## Terraform Project Starter

#### Setup Terraform State Bucket
```shell
AWS_PROFILE=<aws cli profile>
BUCKET_NAME=<bucket name>
REGION=<aws region>
make terraform-setup-state-bucket
```

#### Setup Terraform Backend
```shell
make terraform-setup
```

#### Plan Terraform
```shell
make terraform-plan
```

#### Apply Terraform
```shell
make terraform-apply
```

#### Destroy Terraform
```shell
make terraform-destroy
```