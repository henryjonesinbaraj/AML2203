import re
my_listy= ["on@3", "two#", "thre'%e"]
print([re.sub('[^a-zA-Z0-9]+', '', g) for g in my_listy])

my_list = ["o:<>n@3", "tw{o'#", "thre%e"]
removetable = str.maketrans("", "", "@#%'%$#@%^&*({)}:"":><?")
my_list=[s.translate(removetable) for s in my_list]
print(my_list)
words_pdf_list=['appl%%$^$#e', "that's", '50%']
remove_characters= str.maketrans("", "", "@#%'%$#@%^&*({)}:"":><?")
words_pdf_list=[s.translate(remove_characters) for s in words_pdf_list]
print(words_pdf_list)