MORSE_MAP = [
    "-----",  # 0
    ".----",  # 1
    "..---",  # 2
    "...--",  # 3
    "....-",  # 4
    ".....",  # 5
    "-....",  # 6
    "--...",  # 7
    "---..",  # 8
    "----.",  # 9
]


def convert_code(num: str) -> str:
    morse_code = "   ".join([MORSE_MAP[int(char)] for char in num])
    return morse_code


# num = input('Enter a number to convert:')
# morse_code = convert_code(num)
# print(f"The morse code for 9 is {morse_code}")
