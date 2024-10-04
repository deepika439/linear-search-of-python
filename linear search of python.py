n=int(input())
lst=[]
flag=-1
for i in range(n):
    lst.append(int(input()))
search=int(input())
low=0
high=n-1
while(low<=high):
    mid=low+high//2
    if(lst[mid]==search):
        flag=mid
        break
    elif(search>lst[mid]):
        low=mid+1
    else:
        high=mid-1

if(flag==-1):
    print("Element not found")
else:
    print(f"Element prsent at the index {flag}")
