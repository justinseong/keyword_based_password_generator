#<><><><><><><><><><><><><><><><><><><>#
#       Password Generator  BETA       #
#<><><><><><><><><><><><><><><><><><><>#

import random
chars = ''

letter = '`~!@#$%^&*()_-+=|'

length = input('password length?')
length = int(length)

string = input('input keyword:')
password = ''
saved_lcs = 0
saved_password = ''

def lcs(a, b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                    e = prev[j-1]+1 if i* j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]

if len(string) < length:
    print('error')

else:
    for i in range(100):
        password = ''
        for c in string:
            password += random.choice(string)

        generated_password = ''

        for i in range(length):
            if i % 2 == 0:
                # print(password[i].capitalize(), end="")
                generated_password += password[i].capitalize()
            else:
                # print(password[i], end="")
                generated_password += password[i]
        duration = random.randint(1, 3)
        for i in range(duration):
            j = random.randint(1, len(letter)-1)
            # print(letter[j], end="")
            generated_password += letter[j]
        # print('')
        # print('lcs: ' + str(lcs(string, generated_password)))
        lcs_value = lcs(string, generated_password)
        if saved_lcs < lcs_value:
            saved_lcs = lcs_value
            saved_password = generated_password
    print(saved_password)
    print('lcs: ' + str(lcs(string, generated_password)))