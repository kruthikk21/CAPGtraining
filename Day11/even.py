arr=[23,34,667,89,67]
result=[]
for i in range(0,len(arr)):
    if arr[i]%2==0:
        result.append("even")
    else:
        result.append("odd")
print("".join(result))
