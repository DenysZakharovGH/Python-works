import re
email_valid= re.compile('(^|\s)[-a-z0-9_.\']+@([-a-z0-9])+.([a-z]{2,6})(\s|$)')
sentence = "denis_zaharov'_1998@bk.ru"
expression = re.match(email_valid,sentence)
if expression :
    print("{} is correct".format(expression.group()))
else:
    print("{} is not correct".format(sentence))
#https://www.debuggex.com/#cheatsheet