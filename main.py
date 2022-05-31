import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
number = '0123456789'
symbol = '!@#$^&*/?'

add_all = upper+lower+number+symbol
length = 10
password = ''.join(random.sample(add_all, length))

print("Your password is : ", password)