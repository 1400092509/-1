#__author:"LIN SHIH-WAI"
#date:  2017/11/4

print('-'*103)

print('%20s     %20s    %11s    %20s\n'%('sdfsd','sdferwqer','sdffsdf','asdfsf'))
print(len('%20s     %20s    %11s    %20s'%('sdfsd','sdferwqer','sdffsdf','asdfsf')))
print('%20s     %20s    %11s    %20s'%('sdfsdsdfsfsfsfs','sdf13123erwqer','sdf1231313fsdf','a12313sdfsf'))

kkk="'sdfsd','sdferwqer','sdffsdf','asdfsf'"
kkk2=kkk.replace("'",'')
print(kkk2)
kkk2=kkk.split(',')
加总=0
for i in kkk2:
    print(i,'%20s'%len(i))
    加总+=len(i)
print('加总:%s'%加总)
kkk=kkk.replace(',','')
kkk=kkk.replace("'",'')
print(kkk)
print(len(kkk))
len