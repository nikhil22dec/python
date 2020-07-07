checklist=[1,3,4,5,6,8,9,10]
n=int(input('enter a number between 1 and 10'))
start=0
end=len(checklist)
mid = int((end - start) / 2)
while mid > start and mid < end and mid > 0:
    mid = int((end - start) / 2)
    if checklist[mid]==n:
        print('Found the number at location: ',mid)
        break
    elif checklist[mid]<n:
        end=mid
    else:
        start=mid