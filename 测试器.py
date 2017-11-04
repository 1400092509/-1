#__author:"LIN SHIH-WAI"
#date:  2017/10/30
# 保存
# dict_name = {1: {1: 2, 3: 4}, 2: {3: 4, 4: 5}}
# f = open('temp.txt', 'w')
# f.write(str(dict_name))
# f.close()
#
# # 读取
# f = open('temp.txt', 'r')
# a = f.read()
# dict_name = eval(a)
# f.close()
# print(type(dict_name))
all_account_input={'2017.01.01':{'2017.01.01':{'debt':{'cash':10000},'credit':{'equipment':10000},'描述':'测试'},'2017.03.24':{'debt':{'equipment':10000},'credit':{'cash':80000,'account receiable':20000},'描述':'测试'}}}

all_information={'财务报表':{'资产负债表':'','利润表':'','现金流表':''},'账户':{'cash':{'debt':{},'credit':{},'流动性':['流动资产','1'],'属性':'资产'},'notes receiable':{'debt':{},'credit':{},'流动性':['流动资产','2'],'属性':'资产'},'accounts receiable':{'debt':{},'credit':{},'流动性':['流动资产','3'],'属性':'资产'},'supplies':{'debt':{},'credit':{},'流动性':['长期资产','1'],'属性':'资产'},'land':{'debt':{},'credit':{},'流动性':['长期资产','2'],'属性':'资产'},'building':{'debt':{},'credit':{},'流动性':['长期资产','3'],'属性':'资产'},'equipment':{'debt':{},'credit':{},'流动性':['长期资产','4'],'属性':'资产'},'notes payable':{'debt':{},'credit':{},'流动性':['流动负债','1'],'属性':'负债'},'accounts payable':{'debt':{},'credit':{},'流动性':['流动负债','2'],'属性':'负债'},'salaries payable':{'debt':{},'credit':{},'流动性':['流动负债','3'],'属性':'负债'},'capitial stock':{'debt':{},'credit':{},'流动性':['所有者权益排名','1'],'属性':'所有者权益'},'retained earnings':{'debt':{},'credit':{},'流动性':['所有者权益排名','2'],'属性':'所有者权益'}}}

balancesheet = ''
balancesheet += '资产负债表:%s'.center(105, ' ')
balancesheet += '\n'
balancesheet += '-' * 105 + '\n'
balancesheet += '资产:' + ' ' * (52 - len('资产')) + '|' + '负债:'+' '*(52 - len('负债'))+'\n'
资产负债表={}
资产负债表.setdefault('资产',{})
资产负债表.setdefault('负债',{})
#重新生成一个字典 以{资产{cash:1,这样的排名},负债,所有者权益)
# for i in all_information['账户']:#得到每个账户的名字
#     for ii in all_information['账户']['属性']:#得到每个账户的属性
#         if ii=='资产':
#             for all_information['账户'][i]:
#                 资产负债表['资产'].setdefault(i,all_information[i]['余额'])
#                 资产负债表['资产'][i]=['余额']
#         if ii=='负债':
#             for all_information['账户'][i]:
#                 资产负债表['负债'].setdefault(i,all_information[i]['负债'])
#                 资产负债表['负债'][i] = ['余额']
# #计算长度打印
len_of_assets=len(资产负债表['资产'])
len_of_liability=len(资产负债表['负债'])
for i in 资产负债表['资产']:#获得每个资产项目
    space_资产=' '*52+'|'#'如果资产那个
    balancesheet+=' '*4+i+' '*34+资产负债表['资产'][i]+'|'#4个空格没有准确计算





print(balancesheet)