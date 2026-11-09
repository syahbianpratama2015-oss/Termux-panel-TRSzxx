import random, string
for _ in range(10):
    print(''.join(random.choice(string.ascii_letters) for _ in range(12)))
