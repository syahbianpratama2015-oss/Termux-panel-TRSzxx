import random, string
p = int(input("Panjang password (min 8): "))
semua = string.ascii_letters + string.digits + "!@#$%^&*"
print("Password:", ''.join(random.choice(semua) for _ in range(max(8, p))))
