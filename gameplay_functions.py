def click_pen(clicked): # Changes clicked/unclicked
    return not clicked

def multiplier(clicks):
    if clicks >= 10000:
        return 10
    elif clicks >= 5000:
        return 5
    elif clicks >= 1000:
        return 5
    elif clicks >= 420:
        return 3
    elif clicks >= 69:
        return 2
    else: return 1

def get_clicks():
    # Default high score
    high_score = 0
 
    # Try to read the high score from a file
    try:
        no_clicks = open("high_score.cfg", "r")
        high_score = int(no_clicks.read())
        no_clicks.close()
        print("The high score is", high_score)
    except IOError:
        # Error reading file, no high score
        print("There is no high score yet.")
    except ValueError:
        # There's a file there, but we don't understand the number.
        print("I'm confused. Starting with no high score.")
 
    return high_score
 
 
def save_clicks(new_high_score):
    try:
        # Write the file to disk
        no_clicks = open("high_score.cfg", "w")
        no_clicks.write(str(new_high_score))
        no_clicks.close()
    except IOError:
        # Hm, can't write it.
        print("Unable to save the high score.")