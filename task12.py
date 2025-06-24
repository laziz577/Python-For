n = int(input("mos sonni kiriting:"))
juft_son = 0
toq_son = 0
for i in range(1, n +1):
    if 1 % 2 == 0:
        juft_son += i
    else:
        toq_son += i
        print(juft_son, ",", toq_son)
