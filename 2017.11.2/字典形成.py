#__author:"LIN SHIH-WAI"
#date:  2017/11/1
f=open('账户类型编辑器','r+',encoding='utf-8')
a=f.read().replace('\n',',')
k=open('输出.txt','w+',encoding='utf-8')
k.write(a)
