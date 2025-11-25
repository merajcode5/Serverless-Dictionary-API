🌐 Serverless Dictionary API using AWS


Project link-
http://serverless-dictionary-frontend-meraj.s3-website.ap-south-1.amazonaws.com

A fully serverless, scalable, and cost-efficient dictionary lookup service built using AWS Lambda, API Gateway, DynamoDB, S3, and optionally CloudFront.

This project demonstrates real-world cloud skills, modern API development, and serverless best practices — ideal for cloud engineering, AWS, DevOps, and backend roles.

🚀 Features

🔍 Word Lookup API using a Lambda function (Python)

🌐 Serverless API Endpoint via API Gateway (HTTP API)

📦 External Dictionary API Integration (api.dictionaryapi.dev)

📝 Search History Storage (DynamoDB)

🎨 Frontend Web App (HTML + JS hosted on S3, optionally through CloudFront CDN)

♻️ Fully Serverless & Auto-scaling

💰 100% Free-Tier Friendly

<img width="1139" height="811" alt="Screenshot 2025-11-25 072736" src="https://github.com/user-attachments/assets/4e8bf97d-a8cb-4f7d-9091-a53ff1424f29" />

📁 Project Structure

Serverless-Dictionary-API/
│
├── lambda/
│   ├── lambda_function.py
│   ├── requirements.txt
│   └── dependencies (requests, urllib3, etc.)
│
├── frontend/
│   └── index.html
│
├── architecture-diagram/
│   └── (ASCII / PNG / docs)
│
└── README.md

🧠 How It Works

1. User types a word in the frontend UI (hosted on S3).

2. Frontend calls your API endpoint:
https://<api-id>.execute-api.<region>.amazonaws.com/lookup?word=hello

4. API Gateway triggers Lambda.

5. Lambda requests meaning from DictionaryAPI.dev using Python requests.

6. Lambda returns formatted JSON to the frontend.

🛠️ AWS Services Used
Service	Purpose
AWS Lambda (Python)	Core backend logic
API Gateway (HTTP API)	REST endpoint
DynamoDB	Optional search history storage
S3 Static Hosting	Frontend hosting
CloudFront	Optional CDN for performance & HTTPS
CloudWatch Logs	Monitoring


📈 Improvements & Future Enhancements

Add JWT authentication using Cognito

Track per-user search history

Add caching (API Gateway cache or CloudFront)

Add audio pronunciation playback

Deploy using IaC (AWS SAM / Terraform)

🙌 Acknowledgements

Dictionary API powered by https://dictionaryapi.dev

Hosted & deployed on AWS Free Tier
