#__author:"LIN SHIH-WAI"
#date:  2017/11/4
def loading_dict(file_name):#只给all_information,而另一个字典由all_information来生成.
    global all_account_input
    all_account_input.clear()
    loading=open(file_name,'r+',encoding='utf-8')
    read_it_and_put_it=loading.read()
    all_account_input=eval(read_it_and_put_it)
    loading.close()

def loading_dict_all_information(file_name):#只给all_information,而另一个字典由all_information来生成.
    global all_information
    all_information.clear()
    loading=open(file_name,'r+',encoding='utf-8')
    read_it_and_put_it_all=loading.read()
    all_information=eval(read_it_and_put_it_all)
    loading.close()
all_information={}
all_account_input={}
loading_dict('保存')
loading_dict_all_information('资产类型记录器.txt')
print(all_information)
print(all_account_input)


balancesheet = ' '
balancesheet += '资产负债表:%s'.center(105, ' ')
balancesheet += '\n'
balancesheet += '-' * 105 + '\n'
balancesheet += '资产:' + ' ' * (52 - len('资产')) + '|' + '负债:'+' '*(52 - len('负债'))+'\n'
资产负债表={}
资产负债表.setdefault('资产',{})
资产负债表.setdefault('负债',{})
for i in all_information['账户']:
    all_information['账户'][i].setdefault('属性','')#以后加入属性的直接添加
    判断=all_information['账户'][i]['属性']
    if 判断=='资产':
        资产负债表['资产'].setdefault(i,all_information['账户'][i]['余额'])
        资产负债表['资产'][i]=all_information['账户'][i]['余额']
    if 判断=='负债':
        资产负债表['负债'].setdefault(i,all_information['账户'][i]['余额'])
        资产负债表['负债'][i]=all_information['账户'][i]['余额']


        
资产排序=sorted(资产负债表['资产'].items(),key=lambda x:x[0],reverse=True)
print(资产排序)


