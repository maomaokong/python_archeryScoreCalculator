#! /usr/bin/python

import sys
import datetime
import numpy as np


def print_color_output(input_string, input_type):
    if input_type == 'O':
        print("\x1b[0;30;42m{0}\x1b[0m".format(input_string))
    elif input_type == 'W':
        print("\x1b[0;30;41m{0}\x1b[0m".format(input_string))


def main():
    error1 = False
    continue1 = True

    print()
    input1 = input("Please press [Enter] to get the Archery Score...").strip()

    if input1 != '':
        print()
        #print("You didn't press [Enter]. System terminated...")
        print_color_output("You didn't press [Enter]. System terminated...", 'W')
        continue1 = False
        error1 = True

    retry1 = 0
    no_of_try = 0
    no_of_correct = 0

    while continue1 and retry1 <= 3:
        # If retry no need to re-assign the array again
        time_start = datetime.datetime.now()

        if retry1 == 0:
            # Get random six scores and put in array
            array1 = np.random.randint(low=0, high=11, size=6)

        print()
        print("The scores from Target Butt is: {0}".format(array1))
        input2 = input("Please enter the total score from the six arrows...").strip()

        if not input2.isnumeric():
            if retry1 < 3:
                print()
                #print("[retry:{0}] You not entering the proper numeric for the total score, please try again..."
                #      .format(3 - retry1))
                print_color_output(
                    "[retry:" + str(3 - retry1) + "] You not entering the proper numeric for the total score"
                    + ", please try again..."
                    , 'W')

                retry1 += 1
                continue2 = False
                continue
            else:
                print()
                #print("[retry:{0}] You not entering the proper numeric for the total score for more than three times."
                #      + "\nSystem terminated...".format(3 - retry1)
                #      )
                print_color_output(
                    "[retry:" + str(3 - retry1)
                    + "] You not entering the proper numeric for the total score for more than three times."
                    + "\nSystem terminated..."
                    , 'W'
                )

                continue1 = False
                error1 = True
                break

        time_end = datetime.datetime.now()
        no_of_try += 1
        # Add-up all the number in the array
        print()
        print("Your input is: {0}".format(input2))
        total1 = array1.sum()
        print("Total from Target Butt is: {0}".format(total1))
        delta = time_end - time_start
        if int(input2) == total1:
            no_of_correct += 1
            print()
            print("You are correct!\nYou used up {0} seconds to answer!".format(delta.seconds))
            print()
            # print("No of Correct ==> ( {0} / {1} ) <== Total Tries".format(no_of_correct, no_of_try))
            print_color_output("No of Correct ==> ( "
                               + str(no_of_correct) + " / " + str(no_of_try) + " ) <== Total Tries", 'O')
        else:
            print()
            print("You are wrong!\nYou used up {0} seconds to answer!".format(delta.seconds))
            print()
            #print("No of Correct ==> ( {0} / {1} ) <== Total Tries".format(no_of_correct, no_of_try))
            print_color_output("No of Correct ==> ( "
                               + str(no_of_correct) + " / " + str(no_of_try) + " ) <== Total Tries", 'O')

        continue2 = True
        while continue2:
            print()
            input3 = input("Do you want to [C]ontinue or [Q]uit?").upper().strip()

            if input3 == 'Q':
                print()
                print("System terminated...")
                continue1 = False
                continue2 = False
                error1 = True
                break
            elif input3 == 'C':
                continue2 = False
                retry1 = 0
                break
            else:
                print()
                #print("You not entering the [C]ontinue or [Q]uit, please try again...")
                print_color_output("You not entering the [C]ontinue or [Q]uit, please try again...", 'W')

    if error1:
        sys.exit(1)


if __name__ == '__main__':
    main()
