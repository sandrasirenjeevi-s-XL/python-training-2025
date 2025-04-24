# square=lambda x: x*x
# print(square(5))
# def double(n):
#     return n*2
# nums=[1,2,3,4]
# double=list(map(double,nums))
#map
# nums=[1,2,3,4]
# double=list(map(lambda num:num*2,nums))
# print(double)
#filter (function,iterable)
# nums=[10,15,12,13,14,12,11,6]
# double=list(filter(lambda num:num>12,nums))
# print(double)
def make_multipier(num):
    return lambda x:x*num
output=make_multipier(4)(5)
print(output)
