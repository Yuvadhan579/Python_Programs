def claculate_sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(claculate_sum(10,20))
print(claculate_sum(10,20,30,40))
print(claculate_sum(5,10,15,20,25))