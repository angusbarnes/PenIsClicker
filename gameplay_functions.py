from pygame.time import get_ticks
MILLION = 10**6

def click_pen(clicked): # Changes clicked/unclicked
    return not clicked

clicks_last_second = [] # Stores the time of clicks

def update_clicks_per_second(): # Get time of most recent click, store it, return that time
    now = get_ticks()
    clicks_last_second.append(now)

    return now

def get_clicks_per_second(): # Get current time, remove all clicks over 1 sec ago, return clicks / 1 sec
    now = get_ticks()

    start_time = now - 1000

    while clicks_last_second and clicks_last_second[0] < start_time:
        clicks_last_second.pop(0)

    if len(clicks_last_second) > 1:
        return len(clicks_last_second) / 1000 * 1000
    elif len(clicks_last_second) == 1:
        return 1
    else:
        return 0

def multiplier(clicks):
    if clicks >= 100*MILLION:
        return 420.69
    elif clicks >= 20*MILLION:
        return 74
    elif clicks >= 10*MILLION:
        return 69
    elif clicks >= 1000000:
        return 42
    elif clicks >= 100000:
        return 25
    elif clicks >= 10000:
        return 20
    elif clicks >= 5000:
        return 10
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
        no_clicks = open("cfg/high_score.cfg", "r")
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
        no_clicks = open("cfg/high_score.cfg", "w")
        no_clicks.write(str(new_high_score))
        no_clicks.close()
    except IOError:
        # Hm, can't write it.
        raise IOError("Unable to save the high score.")