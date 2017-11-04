#__author:"LIN SHIH-WAI"
#date:  2017/10/30
# 保存
dict_name = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
f = open('temp.txt', 'w')
f.write(str(dict_name))
f.close()

# 读取
f = open('temp.txt', 'r')
a = f.read()
dict_name = eval(a)
f.close()
print(type(dict_name))