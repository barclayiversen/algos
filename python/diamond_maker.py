# This is a cool one. It takes an odd integer N and returns an asterisk diamond of which the center is N asterisks long. 

def diamond(n):  
    if n % 2 == 0 or n < 3:
        return None
    i = 1
    diamond = ""
    while i <= n:
        if i < n:
            diamond += " " * ((n - i) / 2)
        diamond += ("*" * i) + "\n"
        i += 2
    i = n - 2
    while i >= 0:
        if i > 0:
            diamond += " " * ((n - i) / 2)
        diamond += ("*" * i) + "\n"
        i -= 2
    return diamond
