import boto3
import os
import encrypter
import io

BUCKET = "leo-magic-bucket"
s3 = boto3.resource('s3')
awslambda = boto3.client('lambda', region_name='eu-west-2')
GIGABYTE = 1024 ** 3
MEGABYTE = 1024 ** 2

def get_size_of_file(file_name):
    """Get size of s3 file from aws"""
    files = s3.Bucket(BUCKET).objects.filter(Prefix=file_name, MaxKeys=1)
    for obj in files:
        return obj.size

    raise LookupError("Did not return any objects for key: {}".format(file_name))

def get_system_memory():
    mem_bytes = os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')
    return 12000


def get_lambda_memory(lambda_name):
    """Return memory set for lambda function"""
    response = awslambda.get_function(FunctionName=lambda_name)
    # Because size is returned in Megabytes we have to do some
    # converting to keep measurement consistant
    print("memory size lambda in megabytes: {}".format(
        response['Configuration']['MemorySize']))
    return response['Configuration']['MemorySize']*MEGABYTE


def handler(event, context):
    """Handler for when deployed as a lambda function, this should be called
     from aws when a text file is uploaded into s3 bucket"""

    # Get file key from the event
    s3_key = event['Records'][0]['s3']['object']['key']

    # Get file size
    file_size = get_size_of_file(s3_key)

    memory_size = get_system_memory()

    lambda_size = get_lambda_memory('Encrypt_text_files_lambda')

    print("file size: {} \n memory size: {} \n lambda_size: {}".format(
        file_size, memory_size, lambda_size))

    if file_size > (memory_size/2) or file_size > (lambda_size/2):
        print("File is too big to be dealt with by this lambda...")
        extra_mem_lambda_size = get_lambda_memory('Encrypt_text_files_lambda_extra_memory')
        print("Big lmabda size {}".format(extra_mem_lambda_size))
        if file_size > (extra_mem_lambda_size/2):
            print("File is too big to be dealt with by the biggest lambda")
            raise Exception("File too big to decrypt using any known lambda")
        else:
            print('calling other lambda')
            # call other lambda
    else:
        print('encrypting file')
        #get obj
        file_to_encrypt = s3.Object(BUCKET, s3_key)

        print(file_to_encrypt.get())

        file_string = file_to_encrypt.get()["Body"].read().decode('utf-8')
        # print(file_string)
        #
        # #encrypt

        encrypted_string = encrypter.encrypt(file_string, 12345678)
        # turn encrypted string into a file obj
        fileobj = io.BytesIO(encrypted_string.encode("utf-8"))

        #create key for encrypted file
        key = 'processed/' + s3_key.split('/')[1]

        # print("response from encrypter: {}".format(encrypted_string))
        #decrypt testing
        # decrypted_string = encrypter.encrypt(encrypted_string, 12345678, True)
        # print("decrypted string: {}".format(decrypted_string))
        # print("file string: {} ".format(file_string))

        #upload
        s3.Bucket(BUCKET).upload_fileobj(Fileobj=fileobj, Key=key)


# test when running python file as script
if __name__ == '__main__':
    event = {'Records': [
        {'eventVersion': '2.0',
         'eventSource': 'aws:s3',
         'awsRegion': 'eu-west-2',
         'eventTime': '2018-06-23T12:29:30.262Z',
         'eventName': 'ObjectCreated:Put',
         'userIdentity': {'principalId': 'AYR5JY9HRPUX8'},
         'requestParameters': {'sourceIPAddress': '109.156.63.35'},
         'responseElements': {'x-amz-request-id': '4F92851230D43C4E', 'x-amz-id-2': 'uq8c4LtBLTuB2oOmqk9zJSxE4biDSK0/2g6j6VbFyOnw/x2zjRsu2Fk7Fl9IoEyLjZpNVSK0wBs='},
         's3': {'s3SchemaVersion': '1.0', 'configurationId': '6b38065f-6b9d-41d8-b1e1-d71a6fd0f5ba', 'bucket': {'name': 'leo-magic-bucket', 'ownerIdentity': {'principalId': 'AYR5JY9HRPUX8'}, 'arn': 'arn:aws:s3:::leo-magic-bucket'}, 'object': {'key': 'file_dump/text_file_6.txt', 'size': 70, 'eTag': '5f0e6a1a5f024e8dabd3a26af9a73fe9', 'sequencer': '005B2E3D2A344CAC75'}}}]}
    handler(event,'')


