# nums=[1,2,3,4]
# r=list(map(lambda num:num*2,nums))
# print(r)


# nums=[10,15,12,13,14,12,11,6]
# r=list(filter(lambda num : num>12 , nums))
# print(r)

def make_mul(num):
    return lambda x:x*num

print(make_mul(4)(5))