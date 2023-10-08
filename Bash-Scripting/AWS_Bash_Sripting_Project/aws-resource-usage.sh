#!/bin/bash
###########################
# Author: YAKUB YO
# Date: Oct-4-23
# version: v1
# This script will report the AWS resource usage.
############################

set -x

# EC2
# S3
# Lambda
# IAM Users

# list EC2 instances
echo "list all instances in the user account"
aws-vault exec y2o -- aws ec2 describe-instances

# list all the s3 buckets
echo "list all s3 bucket in the user account"
aws-vault exec y2o -- aws s3 ls

# list lambda
echo "list all instalambda functions in the user account"
aws-vault exec y2o -- aws lambda list-functions

# list IAM users
echo "list all iam users in the user account"
aws-vault exec y2o -- aws iam list-users