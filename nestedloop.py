

# i = 1

# while i <= 10:
    
#     j = 1

#     while j <= i:
#         print("%d " % (j * i), end='')

#         j = j + 1

#     print()

#     i = i + 1

for i in range(1, 11):
    for j in range(1, i + 1):
        print("%d " % (i * j), end='')

    print()