import unittest
import aws_functionality as aws


class TestEncrypter(unittest.TestCase):
    """Testing various scenarios of encrypt / decrypt
     ensuring the same string you started with once
     encryption and decryption has occurred"""

    def setUp(self):
        pass

    def test_basic_sqs(self):
        msg = "big message"
        aws.send_sqs_msg(msg)
        message_list = aws.read_sqs_msg()
        self.assertEqual(msg, message_list[0])


if __name__ == '__main__':
    unittest.main()
