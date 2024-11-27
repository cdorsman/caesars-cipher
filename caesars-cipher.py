#/usr/bin/env python3

from sys import argv

alphabet = [
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

def encrypt(char: str) -> str:
    buffer = 0
    result = []

    for alpha_index, alpha_char in enumerate(alphabet):
        if alpha_char == char:
            buffer = alpha_index - 3
            result.append(alphabet[buffer])
    return result

def main():
    length = len(argv)
    result = []

    for index in range(1, length):
        input_word = list(argv[index])
        for input_letter in input_word:
            for _, char in enumerate(input_letter):
                result.append(encrypt(char))

    joined = ''.join(','.join(map(str, row)) for row in result)
    print(joined)

if __name__ == '__main__':
    main()
