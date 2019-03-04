import boto3

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')

#Create Bucket
new_bucket = s3.create_bucket(Bucket='automatingaws-python-boto3', CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'})

#List Bucket
for bucket in s3.buckets.all():
	print(bucket)

