import unittest
import encrypter

class TestEncrypter(unittest.TestCase):
    """Testing various scenarios of encrypt / decrypt
     ensuring the same string you started with once
     encryption and decryption has occurred"""

    def setUp(self):
        pass


    def encrypt_decrypt(self, string, number):
        """Functionality for testing encryption and decryption"""
        encrypt_string = encrypter.encrypt(string, number)
        decrypt_string = encrypter.encrypt(encrypt_string, number, decrypt=True)
        print("Testing string: {}\nNumber: {} ".format(string, number))
        self.assertEqual(string, decrypt_string)


    def test_basic_1(self):
        string = "test string"
        number = 12345431
        self.encrypt_decrypt(string, number)


    def test_basic_2(self):
        string = "test string 23"
        number = 99999999
        self.encrypt_decrypt(string, number)

    def test_basic_3(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st & second strings"
        number = 12341234
        self.encrypt_decrypt(string, number)

    def test_basic_4(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st, 2nd & 3rd strings"
        number = 12344321
        self.encrypt_decrypt(string, number)

    def test_basic_5(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st, 2nd & 3rd strings, " \
                 "this one is going to be a way longer string maybe even super long. 1234567890-=+_)" \
                 "(**&^^^%$££!QWESAWEJQWE78QWE54321| 웃웃웃웃 ☼ ❤ "
        number = 12344321
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_1(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_1.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_2(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_2.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_3(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_3.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_4(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_4.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_5(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_5.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

    def test_encrypt_from_file_6(self):
        """Test the upload files ensuring they can be encrypted then decrypted."""

        # opening as bytes initially to replicate how it is read once downloaded S3 object
        with open('files_to_upload/text_file_6.txt', 'rb') as file:
            string = file.read().decode('utf-8')
        number = 12345678
        self.encrypt_decrypt(string, number)

if __name__ == '__main__':
    unittest.main()