#!/bin/bash
###########################
# Author: YAKUB YO
# Date: Oct-4-23
# version: v1
# This script will report the AWS resource usage.
############################

# EC2
# S3
# Lambda
# IAM Users

# list EC2 instances
aws-vault exec y2o -- aws ec2 describe-instances

# list all the s3 buckets
aws-vault exec y2o -- aws s3 ls

# list lambda
aws-vault exec y2o -- aws lambda list-functions

# list IAM users
aws-vault exec y2o -- aws iam list-users