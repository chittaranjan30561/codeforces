def isDist(n):
    a=[0]*26
    for i in n:
        a[ord(i)-ord('0')]+=1;
    for i in a:
        if(i>1):
            return False
    return True;
n=int(input())
ans=0
while(True):
    n+=1;
    ans=str(n)
    if(isDist(ans)):
        break;
print(ans)
