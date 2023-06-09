# need to handle grocery items that are all less than 17 characters long
# need to account for duplicate grocery elements
# need to add feature for user-defined output file
# need to do other error checking

## --- helper functions --- ##
def findMaxLenStr(arr):
    max = 0
    for item in arr:
        if(len(item)>max): max=len(item)
    return max
## --- helper functions --- ##

f=None
firstInput = input("Welcome to receipt generator! type 's' to run sample data or specify the path of your input file: ")

cond = False
if(firstInput=="s"): f = open('receipt1.txt','r'); cond=True

while(cond==False):
    try:
        f = open(firstInput,'r'); cond=True
    except FileNotFoundError: firstInput = input("Path not found, please re-enter or type 's' to run sample data: ")

names = list()
prices = list()

for line in f:
    item = line.split(':')
    names.append(item[0].strip())
    prices.append(item[1].strip())

f.close()

#adding white space to items for alignment
maxLen = findMaxLenStr(names)
for i in range(len(names)):
    for j in range(maxLen-len(names[i])):
        names[i]+=' '

lines = list()

for i in range(len(names)):
    lines.append(names[i]+'   '+'$'+prices[i])

f = open('wreceipt.txt', 'w')
for line in lines:
    f.write(line+'\n')

#creating subtotal string
st = "\nSubtotal"
for i in range(maxLen-5): #subtotal is 8 chars long + 3 extra white space
    st+=' '

floatst = 0.0
for price in prices:
    temp = float(price)
    floatst+=temp

st+=('$'+("%.2f" % (floatst)))
f.write(st+'\n')

#creating tax string
tax = "Tax (NJ sales 7%)"
for i in range(maxLen-14): #tax string is 16 chars long + 3 extra white space
    tax+=' '

taxamt = (floatst*0.07)
tax+=('$'+("%.2f" % (taxamt)))
f.write(tax+'\n')

#creating total string
total = "Total"
for i in range(maxLen-2):
    total+=' '

totalamt = floatst+taxamt
total+=('$'+("%.2f" % (totalamt)))

#divider string
div=""
divlen = maxLen+8
if(totalamt>=10.0): divlen+=1
for i in range(divlen):
    div+='-'

f.write(div+'\n')

f.write(total)
if(firstInput=="s"): print("'receipt1.txt' raw data written to 'wreceipt.txt'")
else: print("'"+firstInput+"' raw data written to 'wreceipt.txt'")

f.close()