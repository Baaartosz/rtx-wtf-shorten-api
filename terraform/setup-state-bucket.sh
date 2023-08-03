export AWS_PROFILE=$1
BUCKET_NAME=$2
BUCKET_REGION=$3

echo Creating "$BUCKET_NAME" in "$BUCKET_REGION"
aws s3 mb s3://"$BUCKET_NAME" --region "$BUCKET_REGION" || exit

echo Enabling versioning...
aws s3api put-bucket-versioning --bucket "$BUCKET_NAME" --versioning-configuration Status=Enabled || exit

echo Enabling encryption...
aws s3api put-bucket-encryption --bucket "$BUCKET_NAME" --server-side-encryption-configuration '{"Rules": [{"ApplyServerSideEncryptionByDefault": {"SSEAlgorithm": "AES256"}}]}' || exit

echo Making bucket private...
aws s3api put-bucket-acl --bucket "$BUCKET_NAME" --acl private || exit

echo Finished creating "$BUCKET_NAME" in "$BUCKET_REGION"


