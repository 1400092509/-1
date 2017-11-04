#__author:"LIN SHIH-WAI"
#date:  2017/11/2

def save_dict(name,filename):#x是那个字典,y是文件面#把字典保存到字典中.
    reading=open(filename,'w+',encoding='utf-8')
    saving=dict_name
    reading.write(saving)
    reading.close()

def loading_dict(dict_name,file_name):#只给all_information,而另一个字典由all_information来生成.
    loading=open('file_name','r+',encoding='utf-8')
    read_it_and_put_it=loading.read()
    dict_name=eval(read_it_and_put_it)
    loading.close()