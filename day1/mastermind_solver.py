color = {
    1: "Red",
    2: "Green",
    3: "Blue",
    4: "Yellow",
    5: "Brown",
    6: "Orange",
    7: "Black",
    8: "White"
}


def print_guess(n: int) -> None:
    for clr in str(n):
        print(color[int(clr)], end=", ")


def is_valid_guess(n: int) -> bool:
    n_as_string = str(n)
    if len(set(n_as_string)) != len(n_as_string):
        return False
    if "0" in n_as_string:
        return False
    if "9" in n_as_string:
        return False
    return True


def get_reds_and_whites(guess: int, secret_number: int) -> tuple[int, int]:
    s_guess = str(guess)
    s_secret_number = str(secret_number)
    reds = 0
    whites = 0

    for i1, d1 in enumerate(s_guess):
        for i2, d2 in enumerate(s_secret_number):
            if d1 == d2:
                if i1 == i2:
                    reds += 1
                else:
                    whites += 1

    return reds, whites


def process_feedback(reds: int, whites: int, previous_guess: int, possible_values: list[int]) -> list[int]:
    return [
        val for val in possible_values
        if get_reds_and_whites(val, previous_guess) == (reds, whites)
    ]


possible_values = [n for n in range(1000, 10_000) if is_valid_guess(n)]

while len(possible_values) > 0:
    next_guess = possible_values[0]
    print_guess(next_guess)
    print()
    reds = int(input("reds: "))
    whites = int(input("whites: "))

    possible_values = process_feedback(reds, whites, next_guess, possible_values)

