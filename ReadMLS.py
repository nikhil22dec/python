# Reading an excel file using Python
import xlrd
import xlsxwriter
from fnmatch import fnmatch

# Give the location of the file
readloc = (r"C:\Users\jainnikh\Desktop\MLS - Show Services.xlsx")
readwb = xlrd.open_workbook(readloc)
readsheet = readwb.sheet_by_index(0)
writeloc = (r"C:\Users\jainnikh\Desktop\MLS - Show Services Updated.xlsx")
writewb = xlsxwriter.Workbook(writeloc)
writesheet = writewb.add_worksheet()
writeerrorloc = (r"C:\Users\jainnikh\Desktop\MLS - Show Services Error.xlsx")
writeerrorwb = xlsxwriter.Workbook(writeerrorloc)
writeerrorsheet = writeerrorwb.add_worksheet()
cell_format = writewb.add_format({'bold': True, 'font_color': 'black'})
cell_format = writeerrorwb.add_format({'bold': True, 'font_color': 'black'})
#Read the entire excel cell by cell
noofrows=readsheet.nrows-1
noofcols=readsheet.ncols-1
filtered_my_list=[]
flag=0
a=1
b=0
c=1
d=0
#Print column names
for j in range(0, noofcols):
    writesheet.write(0, j, readsheet.cell_value(1, j),cell_format)
    writeerrorsheet.write(0, j, readsheet.cell_value(1, j),cell_format)
for i in range(2,noofrows):
#Test if Apollo Envs. column has all 3 regions present or not
    my_string=readsheet.cell_value(i,26)
    my_list = my_string.split(",")
    my_search_list_NA = set(['*NA*Prod*', '*IAD*Prod*', '*US*Prod*'])
    my_search_list_EU = set(['*EU*Prod*','*DUB*Prod*'])
    my_search_list_FE = set(['*FE*Prod*', '*PDX*Prod*','*JP*Prod*'])
    filtered_my_list=[x for x in my_list if any(fnmatch(x, p) for p in my_search_list_NA)]
    if filtered_my_list:
        filtered_my_list = []
        filtered_my_list = [x for x in my_list if any(fnmatch(x, p) for p in my_search_list_EU)]
        if filtered_my_list:
            filtered_my_list = []
            filtered_my_list = [x for x in my_list if any(fnmatch(x, p) for p in my_search_list_FE)]
            if filtered_my_list:
                for j in range(0,noofcols):
                    flag=1
                    writesheet.write(a,b,readsheet.cell_value(i,j))
                    b=b+1
                a=a+1
                b=0
    if flag==0:
        for j in range(0, noofcols):
            writeerrorsheet.write(c, d, readsheet.cell_value(i, j))
            d=d+1
        c=c+1
        d=0
    filtered_my_list = []
    flag=0
writewb.close()
writeerrorwb.close()