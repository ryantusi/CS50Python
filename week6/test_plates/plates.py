# main function
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # set main flag if all conditions pass
    main_flag = False

    # set flag for if a number turns alpha or numeric
    alpha_flag = False
    num_flag = False

    # characters less 2 or more than 6
    if len(s) < 2 or len(s) > 6:
        return False
    else:
        # copying the string
        arr = s

        # checking for special symbols
        for i in arr:
            if (i == " " or i == "." or i == "!" or i == "," or i == "/"):
                return False
                break

        # checking first two characters are alpha
        for i in range(2):
            if (arr[i].isalpha() == False):
                return False
                break

        # checking the rest characters
        for i in range(2, len(arr)):
            # setting flags for alpha or numeric to true
            if i == 2:
                if (arr[i].isnumeric()):
                    num_flag = True
                    if (arr[i] == '0'):  # if number starts with zero
                        return False
                        break
                elif (arr[i].isalpha()):
                    alpha_flag = True
                else:   # if something else other than alpha or numeric
                    return False
                    break

            else:
                # checking if numbers come in middle
                if (num_flag == True and (arr[i].isalpha()) == True):
                    return False
                    break

                # setting numeric flag if numeric sequence found
                elif (alpha_flag == True and (arr[i].isnumeric()) == True):
                    num_flag = True
                    alpha_flag = False

                    # checking if first number is zero in sequence
                    if (arr[i] == '0'):
                        return False
                        break

        # if all conditions passed, set main flag to true and return
        main_flag = True
        return main_flag

if __name__ == "__main__":
    main()
