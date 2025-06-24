n = int(input("1-son:"))
for i in range(6):
    raqam = int(input(f"{i +2} - raqam :"))

    if raqam > n:
        n = raqam
        print("maksimal son",n)
        