import boto3

BUCKET = "leo-magic-bucket"
s3 = boto3.resource('s3')


def upload_file(file):
    print("uploading {} to amazon S3".format(file))

    s3.Bucket(BUCKET).upload_file("/home/leo/repos/aws-test-repo/product/" + file, file)
    print("Done")


upload_file("test.txt")