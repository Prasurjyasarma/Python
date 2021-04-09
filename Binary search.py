lst=[]
y=int(input("enter the size of the list"))
for i in range(0,y):
    x=int(input("enter the values"))
    lst.append(x)
    lst.sort()
n=int(input("enter the value you want to search"))
pos=-1
def serach(lst,n):
    l=0
    u=len(lst)-1
    while l<= u:
        m=(l+u) // 2 #mid value
        if lst[m]==n:
            globals() ['pos'] = m
            return True
        else:
            if lst[m]<n:
                l=m+1
            else:
                u=m-1
    return False

if serach(lst,n):
    print("Found at",pos+1)
else:
    print("not found")
