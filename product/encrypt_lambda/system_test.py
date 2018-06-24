import unittest
import encrypter
import aws_functionality as aws

class TestSystem(unittest.TestCase):
    """Testing various full system scenarios"""

    def setUp(self):
        pass

    def local_file_as_string(self, file_path):
        """Read in local file and return string contents"""
        with open(file_path, 'rb') as file:
            string = file.read().decode('utf-8')
        return string


    def test_upload_encrypt_decrypt(self):

        # Read in original file contents to check against later
        original_file_str = self.local_file_as_string('files_to_upload/text_file_1.txt')

        aws.upload_file('text_file_1.txt', 'file_dump/')

        # Wait for file to upload to s3 and the lambda to handle the request
        # and process the file once it has finished it should create an encrypted
        # version in processed dir
        aws.wait_for_file('processed/text_file_1.txt')

        processed_file_str = aws.get_file_as_string('processed/text_file_1.txt')

        #Currently the encrypt key used is 12345678 in the live lambdas this will change
        unencrypted_file_str = encrypter.encrypt(processed_file_str, 12345678, decrypt=True)

        print("Original str: {}\n"
              "processed str: {}\n"
              "Unencrypted str: {}".format(original_file_str,
                                           processed_file_str, unencrypted_file_str))




if __name__ == '__main__':
    unittest.main()