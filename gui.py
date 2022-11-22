import PySimpleGUI as sg
from wordle_solver import WordleSolver

TITLE = "Wordle Solver"
DEFAULT_WORD = "crate"
IMPOSSIBLE_POSITIONS = {}
COLOR_MAP = {0: "black on gray", 1: "black on green", 2: "black on yellow"}


def create_window(location=(None, None)):
    layout = [
        [
            sg.Text(
                "Wordle Solver",
            )
        ],
        [
            sg.Input(key="guess", default_text=DEFAULT_WORD),
            sg.Button("Guess", key="GUESS_BUTTON_CLICK", bind_return_key=True),
        ],
        [sg.HorizontalSeparator()],
        [sg.Text("Guesses")],
        [
            sg.Column([], key="guess_display", vertical_alignment="top"),
            sg.VerticalSeparator(),
            sg.Listbox(
                values=[],
                key="options_display",
                size=(10, 10),
                visible=False,
                enable_events=True,
                bind_return_key=True,
            ),
        ],
        [sg.Button("Quit"), sg.Button("Reset")],
    ]
    return sg.Window(TITLE, layout, keep_on_top=True, location=location)


class Slot:
    position = 0  # not in word
    button_color = COLOR_MAP[position]

    def toggle(self):
        if self.position == 2:  # currently yellow
            self.position = 1  # change to green
        elif self.position == 1:  # currently green
            self.position = 0  # change to green
        elif self.position == 0:  # currently gray
            self.position = 2  # change to yellow
        self.button_color = COLOR_MAP[self.position]

    def set_position(self, position):
        self.position = position
        self.button_color = COLOR_MAP[self.position]


def new_guess(solver: WordleSolver, guess: str, row: int):
    buttons = []
    if not solver.guess:
        solver.set_guess()
    for col, char in enumerate(guess):
        slot = Slot()
        # set the button as green if it is already in the correct position
        if solver.guess[col] == char:
            slot.set_position(1)
        else:
            solver.add_banned_char(char)
        buttons.append(
            sg.Button(
                char,
                key=f"letter_{row}_{col}",
                metadata=slot,
                button_color=slot.button_color,
                size=5,
            )
        )
    window.extend_layout(window["guess_display"], [buttons])


def update_solver(solver: WordleSolver, position: int, letter: str, order_num: int):
    if not solver.guess:
        solver.set_guess()
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
    window["options_display"].update(valid_options)
    window["options_display"].update(visible=True)
    print("valid options: ", valid_options)


# Initialize the solver
solver = None
# Create the window
window = create_window()

# Create an event loop
curr_row = 0
while True:
    event, values = window.read()
    if event == "Quit" or event == sg.WIN_CLOSED:
        window.close()
        break
    elif event == "GUESS_BUTTON_CLICK":
        curr_guess = values.get("guess")
        if not solver:
            solver = WordleSolver(
                word_list=open("word_list.txt").readlines(), num_letters=len(curr_guess)
            )
        if curr_row < 6:
            new_guess(solver, curr_guess, curr_row)
            display_options(solver)
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
    elif event == "options_display":
        if len(values["options_display"]) <= 0:
            continue
        selected = values["options_display"][0]
        if values.get("guess") == selected:
            curr_guess = values.get("guess")
            if not solver:
                solver = WordleSolver(
                    word_list=open("word_list.txt").readlines(),
                    num_letters=len(curr_guess),
                )
            if curr_row < 6:
                new_guess(solver, curr_guess, curr_row)
                display_options(solver)
                curr_row += 1
        else:
            window.Element("guess").update(selected)
            window.Element("guess").set_focus()
    elif event == "Reset":
        curr_loc = window.current_location(True)
        window.close()
        window = create_window(curr_loc)
        if solver:
            solver.reset()
            solver.set_guess()
        curr_row = 0
        IMPOSSIBLE_POSITIONS = {}
