#!/usr/bin/python3
import sys
import calculator_1

if __name__ == "__main__":

    count = len(sys.argv)

    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    sign = sys.argv[2]

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sign == '+':
        print("{:} + {:} = {:}".format(a, b, calculator_1.add(a, b)))
    elif sign == '-':
        print("{:} - {:} = {:}".format(a, b, calculator_1.sub(a, b)))
    elif sign == '*':
        print("{:} * {:} = {:}".format(a, b, calculator_1.mul(a, b)))
    elif sign == '/':
        print("{:} / {:} = {:}".format(a, b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
