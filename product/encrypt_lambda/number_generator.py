import time

NUMBER_KEY = 4534
OFFSET = 7
INTERVAL = 30

def calculate_number(epoch):
    """takes epoch and from that calculates the 8 digit code returns to the user"""
    results_list_strings = []

    first_result = epoch * NUMBER_KEY
    results_list_strings.append(str(first_result))

    second_result = first_result * NUMBER_KEY
    results_list_strings.append(str(second_result))

    output_string = ''
    for list_string in results_list_strings:
        output_string += list_string[-4:]
    # take the last four digits and concat

    return output_string


def setup_epoch():
    # New epoch starts every 30 seconds at a 7 second offset
    current_time = int(time.time())
    current_time_minus_offset = current_time - OFFSET
    epoch = current_time_minus_offset // INTERVAL
    time_until_next_epoch = INTERVAL -(current_time_minus_offset % INTERVAL)
    print("current time: {}\n"
          "time - offset: {}\n"
          "epoch: {}\n"
          "time until next epoch: {}".format(
        current_time, current_time_minus_offset, epoch, time_until_next_epoch
    ))

    return epoch

# test when running python file as script
if __name__ == '__main__':
    epoch = setup_epoch()
    output = calculate_number(epoch)
    print("FINAL OUTPUT: {} {}".format(output[:4], output[4:]))



