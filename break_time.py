# ======== TAKE A BREAK =========
# function assumes that the user is not already listening to music while doing work

import time
import webbrowser
import random

def take_a_break(amount_of_breaks):
    total_breaks = amount_of_breaks 
    break_count = 0

    print(start_message)

    while break_count < total_breaks:
        break_music = links[random.randint(1,3)]
        time.sleep(time_in_seconds)
        webbrowser.open(break_music)

        break_count += 1

        if break_count == (total_breaks - 1):
            print(motivational_statement)

# === SET THE VARIABLE VALUES BELOW ===
start_message = "Hi! This program started on " + time.ctime()
time_in_seconds = (2 * (60 * 60))

links = {
    1: "https://www.youtube.com/watch?v=vKikM_W_Fpk",
    2: "https://www.youtube.com/watch?v=x0-v2k14I-Q",
    3: "https://www.youtube.com/watch?v=OHz1fCSHTLA",
    4: "https://www.youtube.com/watch?v=MPa-kWJhnvA",
    5: "https://www.youtube.com/watch?v=091nrE66kpg"
}

motivational_statement = "We kicked ass today...and danced! Good job! :)"

# === CALL UP THE FUNCTION ===
take_a_break(3)