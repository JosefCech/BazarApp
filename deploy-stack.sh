aws cloudformation validate-template --template-body file://template.yml   
aws cloudformation deploy --stack-name lambda-api --template-file template.yml --capabilities CAPABILITY_IAM
