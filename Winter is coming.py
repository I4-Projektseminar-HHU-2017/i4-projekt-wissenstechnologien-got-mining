import re 



string_lst = ['Winter is coming']
string_lst2 = ['winter is coming']

text = open("1-5buch.txt", "r").read()

pew = re.findall(r"(?=("+'|'.join(string_lst)+r"))",text)
peww = re.findall(r"(?=("+'|'.join(string_lst2)+r"))",text)
print(pew)
print (peww)


print (pew.count("Winter is coming"))
print (peww.count("winter is coming"))

