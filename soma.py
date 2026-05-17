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
            raise ValueError("The both values must be binarys (only 0s and 1s)")


def is_binary(value):
    return value in ("0", "1")


def binary_array_to_decimal(binary_array):
    binary_array.reverse()
    decimal_value = 0
    for index, bit in enumerate(binary_array):
        if bit == "1":
            decimal_value += 2**index
    binary_array.reverse()
    return decimal_value 


def make_binary_arrays_has_the_same_length(binary_array_1, binary_array_2):
    len_diference = len(binary_array_1) - len(binary_array_2)

    if(len_diference < 0):
        binary_array_1.reverse()
        binary_array_2.reverse()
        for i in range(abs(len_diference)):
            binary_array_1.append("0")
        if(binary_array_2[0] == "1"):
            binary_array_1.append("0")
            binary_array_2.append("0")
        binary_array_1.reverse()
        binary_array_2.reverse()

    if(len_diference > 0):
        binary_array_2.reverse()
        binary_array_1.reverse()
        for i in range(abs(len_diference)):
            binary_array_2.append("0")
        if(binary_array_1[0] == "1"):
            binary_array_2.append("0")
            binary_array_1.append("0")
        binary_array_2.reverse()
        binary_array_1.reverse()


def binary_sum(binary_array_1, binary_array_2):
    make_binary_arrays_has_the_same_length(binary_array_1, binary_array_2)

    response = []
    carry = 0

    binary_array_1.reverse()
    binary_array_2.reverse()

    for index, bit in enumerate(binary_array_1):
        if(bit != binary_array_2[index]):
            if(carry):
                response.append("0")
                carry = 1
                continue
            response.append("1")
            continue
        if(bit == "0"):
            if(carry):
                response.append("1")
                carry = 0 
                continue
            response.append("0")
            continue
        if(carry):
            response.append("1")
            continue
        response.append("0")
        carry = 1
    if carry:
        response.append("1")
    response.reverse()
    binary_array_1.reverse()
    binary_array_2.reverse()
    return response



def main():
    test_binary_array(binary_array_1)
    test_binary_array(binary_array_2)
    binary_array_1_decimal = binary_array_to_decimal(binary_array_1)
    binary_array_2_decimal = binary_array_to_decimal(binary_array_2)
    array_binary_response = binary_sum(binary_array_1, binary_array_2)
    response_binary = "".join(array_binary_response)
    response_decimal = binary_array_to_decimal(array_binary_response)
    print(f"{args.binary_1} = {binary_array_1_decimal}")
    print(f"{args.binary_2} = {binary_array_2_decimal}")
    print(f"{args.binary_1}({binary_array_1_decimal}) + {args.binary_2}({binary_array_2_decimal}) = {response_binary}({response_decimal})")

main()
