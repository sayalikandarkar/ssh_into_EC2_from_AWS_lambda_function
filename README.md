# ssh_into_EC2_from_AWS_lambda

There are multiple ways to use python packages in AWS lambda function
1. Create a zip of all the packages along with your python code and upload the zip. But, it has a size limit of 50mb.
2. Upload your packages in a S3 folder and provide a link of the S3 folder in AWS lambda. But, it has a size limit of 250mb.

I was recently working on a project where I had to use heavy NLP libraries like spacy, pandas etc so the entire package size was crossing 250mb.
My code was working perfectly fine in EC2. So, after all my efforts to minimize the package size went in vain.. I tried to SSH into EC2 via AWS Lambda and it worked perfectly fine.

So, I hope this guide saves you the hassle of uploading heavy python packages on S3/AWS lamba.

# 1. Create an AWS lambda function.
# 2. Create an IAM role to allow access to EC2 and S3.
# 3. Assign the IAM role to your AWS lambda function.
# 4. Generate PEM file for access to your EC2.
# 5. Upload the PEM file securely on your S3. Make sure you provide it the correct access rights.
# 6. Use the ssh python code written in the ssh_ec2_lamba.py python file attached in my repository!

Hope it is helpful! Reach out to me in case of any queries


