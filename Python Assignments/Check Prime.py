def check_prime(num,div=2,count=0):
    if div==num and count==0:
        return "Prime"
    elif div==num or num==1:
        return "Not Prime"
    else:
        if num%div==0:
            count+=1
        return check_prime(num,div+1,count)

print(check_prime(2))
