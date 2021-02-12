#export AWS_DEFAULT_PROFILE=private
aws cloudformation validate-template --template-body file://template.yml
aws cloudformation deploy --stack-name lambda-api --template-file template.yml --capabilities CAPABILITY_IAM
#export AWS_DEFAULT_PROFILE=default