import argparse

parser = argparse.ArgumentParser()

parser.add_argument("binary_1")
parser.add_argument("binary_2")

args = parser.parse_args()

binary_array_1 = list(args.binary_1)
binary_array_2 = list(args.binary_2)

def test_binary_array(binary_array):
    for value in binary_array:
        if(not is_binary(value)):
            print("The both values must be binarys (only 0s and 1s)")
            print(f"The strange argument: {binary_array}")
            return 

def is_binary(value):
    return value in ("0", "1")

def binary_array_to_decimal(binary_array):
    binary_array.reverse()
    decimal_value = 0
    for index, bit in enumerate(binary_array):
        if bit == "1":
            decimal_value += 2**index
    return decimal_value 


def main():
    test_binary_array(binary_array_1)
    test_binary_array(binary_array_2)
    print(binary_array_to_decimal(binary_array_1))

main()
