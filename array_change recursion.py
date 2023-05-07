
a=[5]
def rec(a):
    if a[0]==0:
        return 
    a[0]-=1
    rec(a)
rec(a)
print(a)    