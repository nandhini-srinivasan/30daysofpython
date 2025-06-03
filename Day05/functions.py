def sum_avg(num):
    total=sum(num)
    avg=total/len(num)
    return total,avg

sum_lambda = lambda x: sum(x)
avg_lambda = lambda x: sum(x) / len(x)

numbers = [22, 32, 20, 14,320]

print("Using lambda - Sum:", sum_lambda(numbers), "Average:", avg_lambda(numbers))


