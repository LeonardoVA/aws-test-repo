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
        self.assertEqual(list(string), decrypt_string)


    def test_1(self):
        string = "test string"
        number = 12345431
        self.encrypt_decrypt(string, number)


    def test_2(self):
        string = "test string 23"
        number = 99999999
        self.encrypt_decrypt(string, number)

    def test_3(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st & second strings"
        number = 12341234
        self.encrypt_decrypt(string, number)

    def test_4(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st, 2nd & 3rd strings"
        number = 12344321
        self.encrypt_decrypt(string, number)

    def test_5(self):
        string = "NOW USING A SLIGHTLY more complicated string unlike the 1st, 2nd & 3rd strings, " \
                 "this one is going to be a way longer string maybe even super long. 1234567890-=+_)" \
                 "(**&^^^%$££!QWESAWEJQWE78QWE54321| 웃웃웃웃 ☼ ❤ "
        number = 12344321
        self.encrypt_decrypt(string, number)


if __name__ == '__main__':
    unittest.main()