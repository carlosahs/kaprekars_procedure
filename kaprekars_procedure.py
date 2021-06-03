import argparse
import math

KAPREKARS_CONSTANT = 6174

# parse the command line
parser = argparse.ArgumentParser()
parser.add_argument("number", type=int, help="Number to start computing the Kaprekar's procedure")
opt = parser.parse_args()

def kaprekars_procedure(num: int) -> None:
    """
    Compute the Kaprekar's procedure to get the Kaprekar's constant

    Parameters:
    @num (int): Four-digit seed number to get the Kaprekar's constant

    Returns:
    @None
    """
    iterations = 0
    while num != KAPREKARS_CONSTANT:
        # test if the number is valid
        assert num > 0 and num < 9999, "invalid number, not within range"
        assert num % 1111 != 0, "invalid number, all digits are the same"
        #assert num % 111 != 0 or num // 111 >= 10, "invalid number, all digits are the same"
        #assert num % 11 != 0 or num // 11 >= 10, "invalid number, all digits are the same"
         
        num_size = math.floor(math.log10(num)) + 1
         
        digits = [(num // 10 ** (num_size - i - 1)) % 10 for i in range(num_size)]
        digits.sort()

        lowest_to_highest = sum(digits[i] * 10 ** (num_size - i - 1) for i in range(num_size))
        highest_to_lowest = sum(digits[i] * 10 ** i for i in range(num_size))

        # make sure this number is 4 digits as the Kaprekar's constant
        highest_to_lowest *= 10 ** (math.floor(math.log10(KAPREKARS_CONSTANT) - num_size + 1))

        num = highest_to_lowest - lowest_to_highest
        print(f"{num:4d}")

        iterations += 1

    print(f"Kaprekar's constant found in #{iterations} iteration")

if __name__ == '__main__':
    kaprekars_procedure(opt.number)
