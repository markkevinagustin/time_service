## Time service

#### No docker infra

https://2vqpmoynvic3tmlaojbdqkrld40ytpod.lambda-url.us-east-1.on.aws/

I tried searching for ways to deploy flask framework as an aws lambda function. Found serverless and zappa, but decided to just use lambda functions because it's simpler.

<u>*Sample request*</u>

`curl --location --request POST 'https://2vqpmoynvic3tmlaojbdqkrld40ytpod.lambda-url.us-east-1.on.aws/' \`
`--header 'Content-Type: application/json' \`
`--data-raw '{`
    `"time_string": "11AM"`
`}'`

#### With docker infra

I've created an image based on AWS base image(python) with the lambda function and pushed it to Amazon ECR repository

https://nzxjy4npdrcwhuvblxx4tkjlvq0racdx.lambda-url.us-east-1.on.aws/

<u>*Sample request*</u>

`curl --location --request POST 'https://nzxjy4npdrcwhuvblxx4tkjlvq0racdx.lambda-url.us-east-1.on.aws/' \`
`--header 'Content-Type: application/json' \`
`--data-raw '{`
    `"time_string": "11AM"`
`}'`


##### Notes

`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 468601951624.dkr.ecr.us-east-1.amazonaws.com`

`docker image build -t time_service .`

`docker tag time_service:latest 468601951624.dkr.ecr.us-east-1.amazonaws.com/time_service:latest`

`docker push 468601951624.dkr.ecr.us-east-1.amazonaws.com/time_service:latest`
