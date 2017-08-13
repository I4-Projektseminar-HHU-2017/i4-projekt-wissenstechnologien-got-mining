import re 

string1 = ['you know nothing, Jon Snow']
string2 = ['You know nothing, Jon Snow']

text = open("1-5buch.txt", "r").read()

count1 = re.findall(r"(?=("+'|'.join(string1)+r"))",text)
count2 = re.findall(r"(?=("+'|'.join(string2)+r"))",text)
print(count1)
print (count2)


print (count1.count("you know nothing, Jon Snow"))
print (count2.count("You know nothing, Jon Snow"))
