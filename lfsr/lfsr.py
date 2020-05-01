''' Proof of concept for lfsr driven Neopixel display.
    This program should generate a pseudo random sequence
    of 24-bit numbers using an Linear Feedback Shift Register.
    The ultimate goal is to feed the 24 bit numbers into a
    string of Neopixels to generate a string of random colors. '''

#shifts the values in sr one index to the right
def shift_right(sr):
        for i in range(len(sr)-1, 0, -1):
                sr[i] = sr[i-1]

#prints all the values of the lfsr of length n
def test(n, taps):
        #generate starting values in sr
        sr = [2**(i-1) for i in range(n, 0, -1)]

        for x in range(2**len(sr)-1):
                temp = 0
                for i in range(len(taps)):
                        temp ^= sr[taps[i]-1]
                shift_right(sr)
                sr[0] = temp
                print(sr[0], end=', ')

test(8, [8,6,5,4])
