import random


def get_difficulty_settings():
    settings = {
        '1': {'name': 'Easy', 'code_length': 3, 'colors': ['R', 'G', 'B', 'Y']},
        '2': {'name': 'Medium', 'code_length': 4, 'colors': ['R', 'G', 'B', 'Y', 'W', 'P']},
        '3': {'name': 'Hard', 'code_length': 5, 'colors': ['R', 'G', 'B', 'Y', 'W', 'P', 'O', 'C']}
    }
    return settings


def generate_code(colors, code_length):
    return [random.choice(colors) for _ in range(code_length)]


def get_guess(colors, code_length, hints_used, max_hints, code, revealed_positions):
    while True:
        try:
            guess = input(
                f"Enter your guess ({code_length} colors, e.g., {''.join(colors[:code_length])}), or 'H' for a hint ({max_hints - hints_used} left): ").upper()
            if guess == 'H':
                if hints_used < max_hints:
                    # Find unrevealed positions
                    unrevealed = [i for i in range(code_length) if i not in revealed_positions]
                    if unrevealed:
                        hint_pos = random.choice(unrevealed)
                        print(f"Hint: Position {hint_pos + 1} is {code[hint_pos]}")
                        return None, True, hint_pos
                    else:
                        print("No more unique hints available.")
                        continue
                else:
                    print("No hints left!")
                    continue
            if len(guess) == code_length and all(c in colors for c in guess):
                return list(guess), False, None
            print(f"Invalid guess. Use {code_length} letters from {''.join(colors)} or 'H' for a hint.")
        except EOFError:
            print("Input interrupted. Please enter a valid guess.")
            continue


def evaluate_guess(code, guess):
    correct_position = 0
    correct_color = 0
    code_copy = code.copy()
    guess_copy = guess.copy()

    # Check for correct positions
    for i in range(len(code)):
        if guess[i] == code[i]:
            correct_position += 1
            code_copy[i] = guess_copy[i] = None

    # Check for correct colors in wrong positions
    for g in guess_copy:
        if g and g in code_copy:
            correct_color += 1
            code_copy[code_copy.index(g)] = None

    return correct_position, correct_color


def play_mastermind():
    print("Welcome to Mastermind!")
    print("Choose difficulty:")
    settings = get_difficulty_settings()
    for key, value in settings.items():
        print(f"{key}. {value['name']} ({value['code_length']} colors from {''.join(value['colors'])})")

    while True:
        difficulty = input("Enter 1, 2, or 3: ")
        if difficulty in settings:
            break
        print("Invalid choice. Enter 1, 2, or 3.")

    code_length = settings[difficulty]['code_length']
    colors = settings[difficulty]['colors']
    max_attempts = 10
    max_hints = 3
    hints_used = 0
    revealed_positions = []

    print(f"Guess the {code_length}-color code using: {', '.join(colors)}")
    print("Feedback: X correct colors in correct positions, Y correct colors in wrong positions")
    print("Type 'H' to use a hint (up to 3 hints available).")

    code = generate_code(colors, code_length)
    attempts = 0

    while attempts < max_attempts:
        guess, used_hint, hint_pos = get_guess(colors, code_length, hints_used, max_hints, code, revealed_positions)
        if used_hint:
            hints_used += 1
            revealed_positions.append(hint_pos)
            continue
        attempts += 1
        correct_pos, correct_col = evaluate_guess(code, guess)

        if correct_pos == code_length:
            print(
                f"Congratulations! You cracked the code {''.join(code)} in {attempts} attempts with {hints_used} hints used!")
            return

        print(f"Feedback: {correct_pos} correct positions, {correct_col} correct colors")

    print(f"Game Over! The code was {''.join(code)}")


if __name__ == "__main__":
    play_mastermind()
