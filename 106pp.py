f=int(input())
s=input().split()
g=list(dict.fromkeys(s))
print(*g,sep=" ")
