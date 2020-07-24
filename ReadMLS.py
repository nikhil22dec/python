# Excel Libs for Python
import xlrd
import xlsxwriter
from fnmatch import fnmatch
# File Management - To run it on a different machine, just change the loc parameters
readloc = (r"C:\Users\jainnikh\Desktop\MLS - All tomt.xlsx")
readwb = xlrd.open_workbook(readloc)
readsheet = readwb.sheet_by_index(0)
writeloc = (r"C:\Users\jainnikh\Desktop\MLS - All tomt - Customer Impacting - Regionalized.xlsx")
writewb = xlsxwriter.Workbook(writeloc)
writesheet = writewb.add_worksheet()
writeerrorloc = (r"C:\Users\jainnikh\Desktop\MLS - All tomt - Customer Impacting - NON Regionalized.xlsx")
writeerrorwb = xlsxwriter.Workbook(writeerrorloc)
writeerrorsheet = writeerrorwb.add_worksheet()
filtered_my_list=[] #temporary storage for confirming all 3 regions are present
flag=0
#Index values for output excels
a=1
b=0
c=1
d=0
#Filter Customer Impacting Services
my_search_list_customer_impacting = set(
    ['Service - Frontend Customer Utterance Workflow',
     'Service - Backend Customer Utterance Workflow',
     'Backend Service - Customer Impacting',
     'Frontend Customer Impacting',
     'Speechlet',
     '1P Skill'])
#Possible Region Combinations
my_search_list_NA = set(['*NA*/Prod*', '*IAD*/Prod*', '*US*/Prod*'])
my_search_list_EU = set(['*EU*/Prod*','*DUB*/Prod*'])
my_search_list_FE = set(['*FE*/Prod*', '*PDX*/Prod*','*JP*/Prod*'])
#No. of rows and columns in the input excel
noofrows=readsheet.nrows
noofcols=readsheet.ncols
#Cell format for column headers in output excels
cell_format_wb = writewb.add_format({'bold': True, 'font_color': 'black'})
cell_format_errorwb = writeerrorwb.add_format({'bold': True, 'font_color': 'black'})
#Print column headers
for j in range(0,noofcols):
    writesheet.write(0, j, readsheet.cell_value(1, j),cell_format_wb)
    writeerrorsheet.write(0, j, readsheet.cell_value(1, j),cell_format_errorwb)
#Read the input excel and write each row in one of the two output excels
for i in range(2,noofrows):
#Check for customer impacting
    if readsheet.cell_value(i,3) in my_search_list_customer_impacting:
    #Test if Apollo Envs. column has all 3 regions present or not
        my_string=readsheet.cell_value(i,26)
        my_list = my_string.split(",")
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