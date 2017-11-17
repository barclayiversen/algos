//Square all the digits in a given integer.
//no error checking, just a cool one liner. 

def square_digits(num):
    return int( ''.join(str(n) for n in [int(d)*int(d) for d in str(num)]) )
