#WAS add.py that takes 2 numbers and prints sum
# if you pass less than or more than 2 numbers, an error message should be displayed.



import sys

def print_error_message(value, expected_type):
    print(" '{}' is not a {}. Please enter {}". format(value, expected_type.__name__, expected_type.__name__))
    
if len(sys.argv) == 3:
    if not sys.argv[1].isdigit():
        print_error_message(sys.argv[1], int)
    elif not sys.argv[2].isdigit():
        print_error_message(sys.argv[2], int)
    else:
        print( int(sys.argv[1]) + int(sys.argv[2]))
else:
    print("Expeced 2 values, got {}".format(len(sys.argv) - 1))
