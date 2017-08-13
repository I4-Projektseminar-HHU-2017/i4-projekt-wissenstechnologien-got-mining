import re 



string_lst = ['you know nothing, Jon Snow']
string_lst2 = ['you know nothing, Jon Snow']

text = open("1-5buch.txt", "r").read()

pew = re.findall(r"(?=("+'|'.join(string_lst)+r"))",text)
peww = re.findall(r"(?=("+'|'.join(string_lst2)+r"))",text)
print(pew)
print (peww)


print (pew.count("you know nothing, Jon Snow"))
print (peww.count("you know nothing, Jon Snow"))

