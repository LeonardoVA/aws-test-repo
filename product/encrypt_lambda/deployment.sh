#!/bin/bash

echo "sourcing virtual env"
source ../../env/bin/activate

# Create a temporary directory to get all the bits together required for deployment
echo "Creating 'deployment' directory"
mkdir deployment

# Move the relevant files into setup directory
echo "Moving lambda handler to deployment dir"
cp encrypter.py deployment/
cp encryption_lambda.py deployment/
cp aws_functionality.py deployment/

# Install requirements via pip into the deployment directory as required for aws lambda zips
# -r gives pip a requirements file while -t gives it a target directory
echo "pip installing requirements from requirements.txt file in deployment directory"
pip3.6 install -r requirements.txt -t deployment/

# Prepares the deployment package
echo "Zipping up lambda package"
cd deployment
zip -r package.zip *
mv package.zip ../
cd -

# Remove deployment directory

rm -r deployment
