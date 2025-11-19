num=[1,2,3]
num1=["a","b","c"]
result=list(zip(num,num1))
print(result)

number=[1,2,3]
number1=[10,20,30]
for x,y in zip(number,number1[::1]):
    print(x,y)

dic=[1,2,3]
dic1=["a","b","c"]
result1={dic:dic1 for dic,dic1 in zip(dic,dic1)}
print(result1)