def result(*marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

total, average = result(80, 90, 75, 85, 95)
print("Total Marks:", total)
print("Average Marks:", average)
