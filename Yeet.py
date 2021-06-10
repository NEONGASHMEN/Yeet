print("\n\n")
print(":::   ::: :::::::::: :::::::::: ::::::::::: 		      ")
print(":+:   :+: :+:        :+:            :+:     		      ")
print(" +:+ +:+  +:+        +:+            +:+     		      ")
print("  +#++:   +#++:++#   +#++:++#       +#+     		      ")
print("   +#+    +#+        +#+            +#+     		      ")
print("   #+#    #+#        #+#            #+#          	      ")
print("   ###    ########## ##########     ###     	   Version 1.0")
print("\n")
print("---------------------------------------------------------------")
print("Personalised password generator for bruteforcing")
print("---------------------------------------------------------------")
print()


rep = open("Rep.txt",'r')
list_rep = rep.read().splitlines()
rep.close()

nrep = open("Non_rep.txt",'r')
list_nonrep = nrep.read().splitlines()
nrep.close()

WL = open("WL.txt",'w')
WL.write("")
WL.close()


length = input("What is the number of characters in the password ?   ")
length = int(length)
nrpWord_count = input("How many of the non repeating words need to be in your password ?  ")
nrpWord_count = int(nrpWord_count)
rpWord_count = input("How many of the repeating words need to be in your password ?  ")
rpWord_count = int(rpWord_count)
preSp_chara = input("Do you want to generate passwords beginning with the repeating words(y/N) ?\nNB: This'll generate more number of outputs ")
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
print("Non repeating list: ",list_nonrep)
print("Repeating list: ",list_rep)

def permu(chars,space):
	result = chars;
	for i in range(1,space):
		result = result*(chars-1)
		chars = chars - 1
	return result

list_nonrep.sort(key=len)		
print("\n")

from itertools import product
import linecache
import sys

outlist = []
outlist_rep = []

print("Running.......")
print("You might wanna get a cup of coffee......\n")
print("Generating repeating word permutations.......\n")
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


print("Generating non repeating word permutations.......\n")
for i in range(1,nrpWord_count+1):
	prod = list(product(list_nonrep,repeat = i))
	prod = list(set(prod))
	for j in range(len(prod)):
		out = ""
		for k in range(len(prod[j])):
			out = out + prod[j][k]
		WL = open("WL.txt",'a')
		WL.write(out)
		WL.write("\n")
		WL.close()
		count = count + 1
				
print("Stripping un-necessary words.......\n")
outlist_rep.remove("")
	

tempCount = count

print("Prepending repeating words.......\n")
if (preSp_chara == "Y") or (preSp_chara == "y"):
	for i in range(tempCount):
		eachLine = linecache.getline("WL.txt",i)
		preLists = list(product(outlist_rep,[eachLine]))
		for j in range(len(preLists)):
			out = ""
			for k in range(len(preLists[j])):
				out = out + preLists[j][k]
			WL_a = open("WL.txt",'a')
			WL_a.write(out)
			WL_a.close()
			count = count + 1

print("Wordlist generation successful !!!")		
print(count," words written on ./WL.txt")

for element in dir():
	if element[0:2] != "__":
		del globals()[element]





