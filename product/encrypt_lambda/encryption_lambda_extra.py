import io

import encrypter
import aws_functionality as aws

def handler(event, context):
    """Handler for when deployed as a lambda function, this should be called
     from aws when a text file is uploaded into s3 bucket"""
    print('encrypting file')

    # Get file key from the event
    s3_key = event['Records'][0]['s3']['object']['key']

    # get string contents of file
    file_string = aws.get_file_as_string(s3_key)

    # encrypt
    encrypted_string = encrypter.encrypt(file_string, 12345678)

    # turn encrypted string into a file obj
    fileobj = io.BytesIO(encrypted_string.encode("utf-8"))

    # create key for encrypted file
    key = 'processed/' + s3_key.split('/')[1]

    # upload
    aws.upload_fileobj(fileobj, key)