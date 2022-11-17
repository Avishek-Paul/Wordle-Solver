import PySimpleGUI as sg
from wordle_solver import WordleSolver

TITLE = "Wordle Solver"
DEFAULT_WORD = "crate"
IMPOSSIBLE_POSITIONS = {}


class Slot:
    button_color = "gray"
    position = 0  # not in word

    def toggle(self):
        if self.button_color == "yellow":
            self.button_color = "green"
            self.position = 1  # correct position
        elif self.button_color == "green":
            self.button_color = "gray"
            self.position = 0  # not in word
        elif self.button_color == "gray":
            self.button_color = "yellow"
            self.position = 2  # in word, wrong position


def new_guess(solver: WordleSolver, guess: str, row: int):
    buttons = []
    for col, char in enumerate(guess):
        solver.add_banned_char(char)
        buttons.append(
            sg.Button(
                char,
                key=f"letter_{row}_{col}",
                metadata=Slot(),
                button_color=("black on gray"),
                size=5,
            )
        )
    window.extend_layout(window["guess_display"], [buttons])


def update_solver(solver: WordleSolver, position: int, letter: str, order_num: int):
    if position == 0:  # not in word
        solver.add_banned_char(letter)
        solver.remove_required_char(letter)
        solver.guess[order_num] = "."
        if letter in IMPOSSIBLE_POSITIONS and order_num in IMPOSSIBLE_POSITIONS[letter]:
            IMPOSSIBLE_POSITIONS[letter].remove(order_num)
    elif position == 1:  # correct position
        solver.remove_banned_char(letter)
        solver.add_required_char(letter)
        solver.guess[order_num] = letter
        if letter in IMPOSSIBLE_POSITIONS and order_num in IMPOSSIBLE_POSITIONS[letter]:
            IMPOSSIBLE_POSITIONS[letter].remove(order_num)
    elif position == 2:  # in word, wrong position
        solver.remove_banned_char(letter)
        solver.add_required_char(letter)
        solver.guess[order_num] = "."
        if letter not in IMPOSSIBLE_POSITIONS:
            IMPOSSIBLE_POSITIONS[letter] = set()
        IMPOSSIBLE_POSITIONS[letter].add(order_num)


def display_options(solver: WordleSolver):
    options = solver.get_options()
    valid_options = []
    for option in options:
        # print(option)
        valid = True
        for idx, char in enumerate(option):
            if char in IMPOSSIBLE_POSITIONS and idx in IMPOSSIBLE_POSITIONS[char]:
                valid = False
                break
        if valid:
            valid_options.append(option)

    print("valid options: ", valid_options)


# Initialize the solver
solver = WordleSolver(word_list=open("word_list.txt").readlines())
# solver.set_guess([*"salet"])

layout = [
    [
        sg.Text(
            "Wordle Solver",
        )
    ],
    [
        sg.Input(key="guess", default_text=DEFAULT_WORD),
        sg.Button("Guess", key="GUESS_BUTTON_CLICK"),
    ],
    [sg.HorizontalSeparator()],
    [sg.Text("Guesses")],
    [sg.Column([], key="guess_display")],
    [sg.Button("Quit")],
]

# Create the window
window = sg.Window(TITLE, layout, keep_on_top=True)
# Create an event loop
curr_row = 0
while True:
    event, values = window.read()
    curr_guess = values.get("guess")
    if event == "Quit" or event == sg.WIN_CLOSED:
        window.close()
        break
    elif event == "GUESS_BUTTON_CLICK":
        if curr_row < 6:
            display_options(solver)
            new_guess(solver, curr_guess, curr_row)
            curr_row += 1
    elif "letter" in event:
        # get values
        element = window.Element(event)
        letter = element.get_text()
        # toggle the color and position
        element.metadata.toggle()
        element.update(button_color=element.metadata.button_color)
        # grab new position and update solver
        position = element.metadata.position
        order_num = int(event.split("_")[-1])
        update_solver(solver, position, letter, order_num)
        display_options(solver)
        print(
            "solver values: ", solver.required_chars, solver.banned_chars, solver.guess
        )
