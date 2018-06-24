import os
import time

import boto3

BUCKET = "leo-magic-bucket"
s3 = boto3.resource('s3')
awslambda = boto3.client('lambda', region_name='eu-west-2')
source_dir = os.getcwd() + "/files_to_upload/"
MEGABYTE = 1024 ** 2


def upload_file(file, dest):
    """Upload a file to s3"""
    print("uploading {} to amazon S3".format(file))
    # Upload a file to s3 first param is source second is destination
    s3.Bucket(BUCKET).upload_file(source_dir + file, dest + file)
    print("Done")


def upload_fileobj(fileobj, key):
    """Upload file object to s3"""
    print("uploading fileobj to {} in amazon S3".format(key))
    s3.Bucket(BUCKET).upload_fileobj(Fileobj=fileobj, Key=key)
    print("Done")


def upload_all_files():
    """Upload all the files in the subdirectory"""

    # Get list of all files to upload to s3
    file_names = list_files()
    for name in file_names:
        upload_file(name, "file_dump/")


def list_files():
    """Return list of files in directory"""
    file_list = os.listdir(source_dir)
    print(file_list)
    return [file_list[5]]


def get_file(file_key):
    """Gets file object in s3"""
    return s3.Object(BUCKET, file_key)


def get_file_as_string(file_key):
    """Returns the contents of a file as a string"""
    s3_file = get_file(file_key)
    return s3_file.get()["Body"].read().decode('utf-8')


def get_size_of_file(file_name):
    """Get size of s3 file from aws"""
    files = s3.Bucket(BUCKET).objects.filter(Prefix=file_name, MaxKeys=1)
    for obj in files:
        return obj.size
    raise LookupError("Did not return any objects for key: {}".format(file_name))


def check_file_exists(file_name):
    """Check item is in s3 returns True or False"""
    files = s3.Bucket(BUCKET).objects.filter(Prefix=file_name)
    for file in files:
        if file.key == file_name:
            return True
    return False


def wait_for_file(file_name, timeout=30, initial_delay=0):
    """Waits up to timeout for the file to exist"""
    start_time = time.time()
    print("Waiting for the file {} to appear in aws s3 bucket".format(file_name))

    time.sleep(initial_delay)
    while time.time() < start_time + timeout:
        if check_file_exists(file_name):
            print("File {} found in aws after {} seconds".format(file_name,
                                                                 time.time()-start_time))
            return
        else:
            time.sleep(1)

    raise TimeoutError("Failed to find object: {} in aws s3 bucket: {} "
                       "in: {} seconds".format(file_name, BUCKET, timeout))


def get_lambda_memory(lambda_name):
    """Return memory set for lambda function"""
    response = awslambda.get_function(FunctionName=lambda_name)
    # Because size is returned in Megabytes we have to do some
    # converting to keep measurement consistant (bytes)
    print("memory size lambda in megabytes: {}".format(
        response['Configuration']['MemorySize']))
    return response['Configuration']['MemorySize']*MEGABYTE


if __name__ == '__main__':
    upload_all_files()
