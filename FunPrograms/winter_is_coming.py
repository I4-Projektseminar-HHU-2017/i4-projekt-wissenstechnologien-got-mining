import re 

string1 = ['Winter is coming']
string2 = ['winter is coming']

text = open("1-5buch.txt", "r").read()

count1 = re.findall(r"(?=("+'|'.join(string1)+r"))",text)
count2 = re.findall(r"(?=("+'|'.join(string2)+r"))",text)
print(count1)
print (count2)


print (count1.count("Winter is coming"))
print (count2.count("winter is coming"))
