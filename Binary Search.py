checklist=[1,3,4,5,6,8,9,10]
n=int(input('enter a number between 1 and 10'))
start=0
end=len(checklist)-1
while start<=end:
    mid = int((end + start) / 2)
    print('start: ',start,', mid: ',mid,', end: ',end,', element: ',checklist[mid])
    if checklist[mid]==n:
        print('Found the number at location: ',mid)
        break
    elif checklist[mid]>n:
        end=mid-1
    else:
        start=mid+1


