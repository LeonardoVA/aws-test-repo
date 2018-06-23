

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
            print("Mult: {}\nDivis: {}\nChar: {}\nOrd: {}".format(mult, divis, char, char_num))
            # Change the char number inverse to before
            char_num = int(char_num / mult)
            print("char num {}".format(char_num))
            char_num -= (mult + divis)
            print("char num {}\n".format(char_num))
            end_string.append(chr(char_num))


    print("start string: {}\n"
          "end string: {}\n".format(text, ''.join(end_string)))

    for x in range(len(end_string)):
        print ("Start char: {}={} End char".format(text[x], end_string[x]))

    return ''.join(end_string)

def test():
    return "hello"


