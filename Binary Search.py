checklist=[1,3,4,5,6,8,9,10]
n=int(input('enter a number between 1 and 10'))
start=0
end=len(checklist)-1
counter=1
while True:
    mid = int((end - start) / 2)
    if mid < start or mid > end or mid < 0:
        print('Number not in the list')
        break
    if checklist[mid]==n:
        print('Found the number at location: ',mid)
        break
    elif checklist[mid]<n:
        end=mid
    else:
        start=mid
    counter = counter+1
