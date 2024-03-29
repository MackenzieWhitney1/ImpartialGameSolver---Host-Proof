def count_leading_zeroes(binary_string):
    leading_zeroes = binary_string.partition("1")[0]
    return len(leading_zeroes)


def show_optimal_play_binary_string(binary_string):
    current_string = binary_string
    print(current_string)

    while current_string is not "0":  # if first char is 0, there is no choice but to remove it
        if current_string[0] == "0":
            current_string = current_string[1:]
        elif current_string[0] == "1":
            play1 = current_string[1:]
            play2 = "0"+current_string[1:]
            # print(f"play1 is {play1}")
            # print(f"play2 is {play2}")
            if count_leading_zeroes(play2) // 2 == 0:
                current_string = play2
            else:
                current_string = play1
        print(current_string)
 
show_optimal_play_binary_string("1101")
""" Expected Result
1101 (A is given this)
0101 (B is given this. no choice but to remove 0 at each step)
101 (A)
01 (B)
1 (A)
0 (B loses)
"""
