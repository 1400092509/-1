#__author:"LIN SHIH-WAI"
#date:  2017/11/4
dict1={'xcav123s':1,'b':2,'c':3,'d':4}
print(list(sorted(list(dict1.items()),key=lambda x:x[0],reverse=True)))