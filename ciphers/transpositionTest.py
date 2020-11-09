# Transposition Cipher Test
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import random, sys, transpositionEncrypt, transpositionDecrypt

def main():
    random.seed(42) # Set the random 'seed' ti a static value.

    for i in range(20):
        # Generate random messges to test.

        # The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4, 40)

        # Convert the message string to a list to shuffle it:
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        # Check all possible keys for each message:
        for key in range(1, int(len(message) / 2)):
            encrypted = transpositionEncrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            # If the decryption doesn't match the orginal message, display
            # an error message and quit:
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('Transposition cipher test passed.')

if __name__ == '__main__':
    main()
