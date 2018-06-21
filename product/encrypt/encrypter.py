
simple_test = "test"
test_string = "This is my magical test string lest see if we can change this at all."
test_string2 = "string string string string string string string"
test_number = 99994321


def encrypt(text, number, decrypt=False):
    """This function takes in a string and returns the encrypted string"""
    num_list = list(map(int, str(number)))
    print("args text: {}\n nums: {}\n".format(text, num_list))
    end_string = []
    for idx, char in enumerate(text):
        digit_choice = idx % 4
        if digit_choice is 0:
            mult = num_list[0]
            divis = num_list[4]
        elif digit_choice is 1:
            mult = num_list[1]
            divis = num_list[5]
        elif digit_choice is 2:
            mult = num_list[2]
            divis = num_list[6]
        else:
            mult = num_list[3]
            divis = num_list[7]

        if not decrypt:
            #encrypt
            print("Encrypting...")
            char_num = ord(char)
            print("Mult: {}\nDivis: {}\nChar: {}\nOrd: {}\n".format(mult, divis, char, char_num))
            # change the char num using two of the numbers generated
            char_num += (mult + divis)
            print("char num {}".format(char_num))
            char_num = char_num * mult
            print("char num {}".format(char_num))
            end_string.append(chr(char_num))

        else:
            #decrypting
            print("Decrypting...")
            char_num = ord(char)
            print("Mult: {}\nDivis: {}\nChar: {}\nOrd: {}\n".format(mult, divis, char, char_num))
            # Change the char number inverse to before
            char_num = int(char_num / mult)
            print("char num {}".format(char_num))
            char_num -= (mult + divis)
            print("char num {}".format(char_num))
            end_string.append(chr(char_num))


    print("start string: {}\n"
          "end string: {}\n".format(text, ''.join(end_string)))

    for x in range(len(end_string)):
        print ("Start char: {}={} End char".format(text[x], end_string[x]))

    return end_string

def handler(event, context):
    """Handler for when deployed as a lambda function, this should be called
     from aws when a text file is uploaded into s3 bucket"""
    print("Event: {}\n Context: {}\n".format(event, context))
    print(event['Records'][0]['s3']['bucket'])
    print(event['Records'][0]['s3']['bucket'])
    print(event['Records'][0]['s3']['object'])



# test when running python file as script
if __name__ == '__main__':
    print("Hello from encypter")
    encrypted_test = encrypt(test_string, test_number)
    decrypted_test = encrypt(encrypted_test, test_number, decrypt=True)
    print("start string = {}\n".format(list(simple_test)))
    print("Encrypted string = {}\n".format(encrypted_test))
    print("Decrypted string = {}\n".format(decrypted_test))

