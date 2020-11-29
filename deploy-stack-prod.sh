aws cloudformation validate-template --template-body file://template.yml   
aws cloudformation deploy --stack-name lambda-api-prod  --parameter-overrides Environment=prod --template-file template.yml --capabilities CAPABILITY_IAM
