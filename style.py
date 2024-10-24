

def colorprint(text, color_code):
    if color_code == 'r':
        print("\033[91m {}\033[00m" .format(text))
    elif color_code == 'g':
        print("\033[92m {}\033[00m" .format(text))
    elif color_code == 'b':
        print("\033[96m {}\033[00m" .format(text))
    elif color_code == 'y':
        print("\033[93m {}\033[00m" .format(text))
    elif color_code == 'pr':
        print("\033[95m {}\033[00m" .format(text))


