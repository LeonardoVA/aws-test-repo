import boto3
import os

BUCKET = "leo-magic-bucket"
s3 = boto3.resource('s3')
source_dir = os.getcwd() + "/files_to_upload/"


def upload_file(file):
    """Upload a file to s3"""
    print("uploading {} to amazon S3".format(file))
    # Upload a file to s3 first param is source second is destination
    s3.Bucket(BUCKET).upload_file(source_dir + file, "file_dump/" + file)
    print("Done")


def upload_all_files():
    """Upload all the files in the subdirectory"""

    # Get list of all files to upload to s3
    file_names = list_files()
    for name in file_names:
        upload_file(name)


def list_files():
    """Return list of files in directory"""
    file_list = os.listdir(source_dir)
    print(file_list)
    return file_list[1]

upload_all_files()




