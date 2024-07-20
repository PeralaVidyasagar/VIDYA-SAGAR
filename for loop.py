name =(87,21,39,48,51,60,73)
for i in name:
    if i%8==0:
        print(i)
        break
    else:
        print("there is no divisible by 8")
        
else:
    print("its succesfully complete iteration")