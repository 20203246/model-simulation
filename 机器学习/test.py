t = int(input())
while t:
    t -= 1
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt0 = 0
    cnt1 = 0
    for x in a:
        if x == '0':cnt0+=1
        else:cnt1+=1
    print(cnt1&1,min(cnt0,cnt1))