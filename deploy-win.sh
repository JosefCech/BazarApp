pipenv lock -r > requirements.txt
rm -r output
rm output.zip
pip install -r requirements.txt -t output
cp -r src ./output/src
alias zip="/c/Program\ Files/7-Zip/7z.exe"
/c/Program\ Files/7-Zip/7z.exe a output.zip ./output/*
#cd ./output
#zip -r  ../output.zip ./*
#cd ../
aws s3 cp  ./output.zip  s3://bazaar-app-lambda/
aws lambda update-function-code --function-name lambda-api-BazaarServerWeb-8PKI4GC0G7GO --s3-bucket bazaar-app-lambda --s3-key output.zip
aws lambda update-function-code --function-name lambda-api-BazaarServerApp-F35G9WXDCZWZ --s3-bucket bazaar-app-lambda --s3-key output.zip
