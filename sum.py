def sum_avg (*num):
    sum = 0
    for n in num :
        sum = sum + n
    avg = sum/len(num)
    return avg
result1 = sum_avg(1.1,2.3,3.4)
result2 = sum_avg(2.2,4.3,6.2)
print("avarage ",round (result1))
print("avarege2 decimal ", result2)
def sum_avg (n):
    sum = 0
    for t in n :
        sum = sum + t
    return sum
print("summery ", sum_avg([2,4,6,8,10]))
