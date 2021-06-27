print("\n\n")
print(":::   ::: :::::::::: :::::::::: ::::::::::: 		      ")
print(":+:   :+: :+:        :+:            :+:     		      ")
print(" +:+ +:+  +:+        +:+            +:+     		      ")
print("  +#++:   +#++:++#   +#++:++#       +#+     		      ")
print("   +#+    +#+        +#+            +#+     		      ")
print("   #+#    #+#        #+#            #+#          	      ")
print("   ###    ########## ##########     ###     	   Version 2.0")
print("\n")
print("---------------------------------------------------------------")
print("Made by NEONGASHMEN to crack question paper password in college")
print("---------------------------------------------------------------")
print()


rep = open("Symbols.txt",'r')
list_rep = rep.read().splitlines()
rep.close()

nrep = open("Words.txt",'r')
list_nonrep = nrep.read().splitlines()
nrep.close()

WL = open("WL.txt",'w')
WL.write("")
WL.close()


length = input("What is the number of characters in the password ?   ")
length = int(length)
nrpWord_count = input("How many of the times of core words need to be in your password ?  ")
nrpWord_count = int(nrpWord_count)
rpWord_count = input("How many of the symbols need to be in your password ?  ")
rpWord_count = int(rpWord_count)
preSp_chara = input("Do you want to generate passwords beginning with the symbols(y/N) ?\nNB: This'll generate more number of outputs ")
cps_chara = input("Do you want permutaions based on default capitalization pattern(y/N) ? ")
print()

if (cps_chara == 'y') or (cps_chara == 'Y'):
	for i in range(len(list_nonrep)):
		list_nonrep.append(list_nonrep[i].upper())
		list_nonrep.append(list_nonrep[i].capitalize())
	for i in range(len(list_rep)):
		list_rep.append(list_rep[i].upper())
		list_rep.append(list_rep[i].capitalize())
		
list_nonrep = list(set(list_nonrep))
list_rep = list(set(list_rep))
length_list = len(list_nonrep)+len(list_rep);
count = 0

print("Length of the list: ",length_list) 
print("Words list: ",list_nonrep)
print("Symbols list: ",list_rep)

def permu(chars,space):
	result = chars;
	for i in range(1,space):
		result = result*(chars-1)
		chars = chars - 1
	return result
	
	
def split_list(a_list):
    half = len(a_list)//2
    return a_list[:half], a_list[half:]
    
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
    f.close()
 
def joinArr(a,b):
	res = []
	for idx in b:
		res.append(a[0] + idx)
	return res   
	
def getNum(val,itr):
	a = 0
	for ldf in range(1,itr+1):
		a = a + val**ldf
	return a


list_nonrep.sort(key=len)		
print("\n")

from itertools import product
import linecache
import sys

outlist = []
outlist_rep = []

print("Running.......")
print("You might wanna get a cup of coffee......\n")
print("Generating Core List.......\n")
for i in range(1,rpWord_count+1):
	prod_rep = list(product(list_rep,repeat = i))
	for j in range(len(prod_rep)):
		out_rep = ""
		for k in range(len(prod_rep[j])):
			out_rep = out_rep + prod_rep[j][k]
		outlist_rep.append(out_rep)


outlist_rep.insert(0,"")	
listThree = list(product(list_nonrep,outlist_rep))
list_nonrep = []
for i in range(len(listThree)):
	out = ""
	for j in range(len(listThree[i])):
		out = out + listThree[i][j]
	list_nonrep.append(out)


wholeList = list_nonrep
print("Root list is of size: ",len(wholeList))
print("This'll generate ",getNum(len(wholeList),nrpWord_count)," words. Your crappy PC might not handle it....")
consent = input("Do you want to continue ?? (Y/n) ")

if consent == 'n' or consent == 'N':
	sys.exit("Pussy...!!")

for i in range(len(wholeList)):
	WL = open("WL.txt",'a')
	WL.write(wholeList[i])
	WL.write("\n")
	WL.close()

eachLine = [""]
start = 1
	
for i in range(2,int(nrpWord_count)+1):
	for j in range(start,file_len("WL.txt")+1):
		eachLine[0] = linecache.getline("WL.txt",j)
		eachLine[0] = eachLine[0].strip()
		opArr = joinArr(eachLine,wholeList)
		for k in range(len(opArr)):
			WL = open("WL.txt",'a')
			WL.write(opArr[k])
			WL.write("\n")
			WL.close()
		
		
	start = getNum(len(wholeList),i-1) + 1
	print("val of strt",start)

for element in dir():
	if element[0:2] != "__":
		del globals()[element]