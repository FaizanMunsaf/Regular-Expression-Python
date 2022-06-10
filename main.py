import re

mylist = '''The white swamphen (Porphyrio albus)
was a rail found on Lord Howe Island,
east of the Australian aiai mainland. All contemporary accounts and illustrations were 
produced between 1788 and 1790,
35202-6524719-7
+92-332-8893064
+92-304-4389339 
when the bird was first encountered by British ship crews.
Today, two specimens aiai exist: one in World Museum (pictured) in Liverpool, England, and the holotype in the Natural History Museum of Vienna. It is thought to have been most similar to the Australasian swamphen. The white swamphen was 36 to 55 cm (14 to 22 in) long. Contemporary accounts indicate that individual bird plumage was white, blue, or mixed blue-and-white. The bird's bill, frontal shield and legs were red, and it had a claw (or spur) on its wing. It was probably either flightless or a poor flier; this and its docility made the bird easy prey for visiting humans, who killed it with sticks. Reportedly once common, the species may have been hunted to extinction before 1834, when 
Lord Howe aiai Island was the aiiiiiiiiiiiiiiiii settled. (Full article...)'''

# findall, search, split, sub finditer
# patt = re.compile(r'All')
#
# matchpat = patt.finditer(mylist)
#
# for match in matchpat:
#     print(match)
#     print(mylist[108:111])


'''=========================
    Meta Character
    ========================'''
# dot is use for take any character
# patt = re.compile(r'.')
# patt = re.compile(r'.xt')

# ^ is use for where this string start from...
# patt = re.compile(r'^The')

# $ is use for where this string will end from...
# patt = re.compile(r'...$')

# it's mean a is compulsory and i will 0 or more
# patt = re.compile(r'ai*')

# it's mean a is compulsory and i will 1 or more
# patt = re.compile(r'ai+')

# one a is compulsory and 2 i compulsory in it
# patt = re.compile(r'ai{2}')

# in a group how many ai in a 2 given in our string
# patt = re.compile(r'(ai){2}')
# OR
# in a group how many ai in a 1 given in our string
# patt = re.compile(r'(ai){1}')


# it's mean how many ai or the in our given string
# patt = re.compile(r'ai{1}|the')


'''=========================
    Special Ssequence
    ========================'''

# if The specified string which is start from the string it will return it
# patt = re.compile(r'\AThe')

# it's mean that specified character are at beginning of the spring
# here it will check where does ai word start from in the string and return it
# patt = re.compile(r'\bai')

# here it will check where does ai word or character end from in the string and return it
# patt = re.compile(r'ai\b')
patt = re.compile(r'\Bhe')

matchpat = patt.finditer(mylist)


for match in matchpat:
    print(match)