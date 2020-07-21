https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

set1 =  set(open(r"C:\Users\jainnikh\Desktop\One.txt", 'r').read().split())
set2 =  set(open(r"C:\Users\jainnikh\Desktop\the other.txt", 'r').read().split())
set3=set1.intersection(set2)
print(sorted(set1))
print(sorted(set2))
print(set3)