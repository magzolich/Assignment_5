# PIN code validator
# Create a robust and user-friendly system for validating pin-codes entered by users.
# Develop a Pin-Code Validator code to ensure pin security and adherence to specific criteria:
# ·Pin-codes consist only of numbers and are either 4 or 6 digits in length.
# ·Enforce a rule preventing consecutive numbers to repeat in the pin-code sequence.
# ·Ask for confirmation to check if two entered pin-codes match, indicating successful validation.
# Good Pin-Codes:
# "1234" - 4 digits, no consecutive numbers repeat.
# "987654" - 6 digits, no consecutive numbers repeat.
# Bad Pin-Codes:
# "0000" - Consecutive numbers repeated.
# "1145" - Consecutive numbers repeated.
# "12345" - 5 digits
# "34" - 2 digits
# "ab12" - 4 digits, contains letters.
# Todo
# 1st function input from user (two times)
# -> save input to list
# requirements:
# only integers
# length 4 or 6
# no repeats
# check if the 1st input matches 2nd input

pin_number_1 = (input("Provide your PIN number: "))
pin_number_2 = (
    input("Provide your PIN number: . It should match your first PIN number "))


def validate_pin(pin_number_1: list, pin_number_2: list):
    # check list len (only 4 or 6)
    length_valid = (len(pin_number_1) == 4 and len(pin_number_2) == 4) or (len(
        pin_number_1) == 6 and len(pin_number_2) == 6)
    if not length_valid:
        return (False, "PIN number must contain 4 or 6 characters")

    # check if ints only
    # for i in int(pin_number_1):
    # if not isinstance(i, int):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in pin_number_1:
        if i not in numbers:
            return (False, "You should use only numbers from 0 to 9")

    # check if no repeats
    for i in range(len(pin_number_1)-1):
        if pin_number_1[i] == pin_number_1[i+1]:
            return (False, "Consecutive numbers repeated")

    # check if input1 matches input 2
    if not pin_number_1 == pin_number_2:
        return (False, "PIN numbers don't match.")

    return True


def main():
    pin_validation = validate_pin(pin_number_1, pin_number_2)
    print(pin_validation)


if __name__ == "__main__":
    main()
