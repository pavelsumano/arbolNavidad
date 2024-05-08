num = 10
inicio=1
print(" "*(2*num+2), end="")
print("*")
for i in range(1, num+1):
    print(" "*(2*num-i+3), end="")
    for j in range(1, inicio+1):
        print("0", end="")
    inicio=inicio+2
    print()