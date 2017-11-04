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
# all_account_input={'2017.01.01':{'2017.01.01':{'debt':{'cash':10000},'credit':{'equipment':10000},'描述':'测试'},'2017.03.24':{'debt':{'equipment':10000},'credit':{'cash':80000,'account receiable':20000},'描述':'测试'}}}
all_account_input={'2012.12.12': {'2012.12.12': {'credit': {'cash': '10000'}, 'debt': {'equipment': '10000'}, '描述': '购买设备'}, '2012.12.13': {'debt': {'supplies': '2000'}, 'credit': {'cash': '2000'}, '描述': '购买原料'}, '2012.12.14': {'debt': {'inventory': '5000'}, 'credit': {'cash': '5000'}, '描述': '购买存货', 'q': {'COGS': 'q'}}, '2012.12.15': {'debt': {'cash': '10000'}, 'credit': {'revenue': '10000'}, '描述': '收益'}}}
all_information={'财务报表': {'资产负债表': '', '利润表': '', '现金流表': ''}, '账户': {'cash': {'debt': {'2012.12.15': 10000}, 'credit': {'2012.12.12': 10000, '2012.12.13': 2000, '2012.12.14': 5000}, '流动性': ['流动资产', '1'], '属性': '资产', '余额': 7000}, 'notes receiable': {'debt': {}, 'credit': {}, '流动性': ['流动资产', '2'], '属性': '资产', '余额': 0}, 'accounts receiable': {'debt': {}, 'credit': {}, '流动性': ['流动资产', '3'], '属性': '资产', '余额': 0}, 'supplies': {'debt': {'2012.12.13': 2000}, 'credit': {}, '流动性': ['长期资产', '1'], '属性': '资产', '余额': 2000}, 'land': {'debt': {}, 'credit': {}, '流动性': ['长期资产', '2'], '属性': '资产', '余额': 0}, 'building': {'debt': {}, 'credit': {}, '流动性': ['长期资产', '3'], '属性': '资产', '余额': 0}, 'equipment': {'debt': {'2012.12.12': 10000}, 'credit': {}, '流动性': ['长期资产', '4'], '属性': '资产', '余额': 10000}, 'notes payable': {'debt': {}, 'credit': {}, '流动性': ['流动负债', '1'], '属性': '负债', '余额': 0}, 'accounts payable': {'debt': {}, 'credit': {}, '流动性': ['流动负债', '2'], '属性': '负债', '余额': 0}, 'salaries payable': {'debt': {}, 'credit': {}, '流动性': ['流动负债', '3'], '属性': '负债', '余额': 0}, 'capitial stock': {'debt': {}, 'credit': {}, '流动性': ['所有者权益排名', '1'], '属性': '所有者权益', '余额': 0}, 'retained earnings': {'debt': {}, 'credit': {}, '流动性': ['所有者权益排名', '2'], '属性': '所有者权益', '余额': 0}, 'cash2': {'属性': '负债', '流动性': ['流动负债', '4'], 'debt': {}, 'credit': {}, '余额': 0}, 'credit': {'credit': {}, 'debt': {}, '余额': 0}, 'debt': {'credit': {}, 'debt': {}, '余额': 0}, 'account payable': {'属性': '负债', '流动性': ['流动负债', '5'], 'debt': {}, 'credit': {}, '余额': 0}, 'las': {'属性': '负债', '流动性': ['流动资产', '1'], 'debt': {}, 'credit': {}, '余额': 0}, 'bubuling': {'debt': {}, 'credit': {}, '属性': 'COGS', '流动性': ['成本', '1'], '余额': 0}, 'text1': {'debt': {}, 'credit': {}, '属性': 'expenses', '流动性': ['成本', '2'], '余额': 0}, 'text2': {'debt': {}, 'credit': {}, '属性': '资产', '流动性': ['流动资产', '5'], '余额': 0}, 'textyue': {'debt': {}, 'credit': {}, '属性': '资产', '流动性': ['长期资产', '5'], '余额': 0}, 'text': {'debt': {}, 'credit': {}, '属性': '负债', '流动性': ['流动负债', '2'], '余额': 0}, 'txetpap': {'debt': {}, 'credit': {}, '属性': 'COGS', '流动性': ['成本', '3'], '余额': 0}, 'inventory': {'debt': {'2012.12.14': 5000}, 'credit': {}, '属性': '资产', '流动性': ['流动资产', '4'], '余额': 5000}, 'revenue': {'debt': {}, 'credit': {'2012.12.15': 10000}, '属性': 'revenues', '流动性': ['收入', '1'], '余额': 10000}, 'COGS': {'debt': {}, 'credit': {}, '属性': 'q', '流动性': ['q', 'q'], '余额': 0}}}


balancesheet = ''
balancesheet += '资产负债表:%s'.center(105, ' ')
balancesheet += '\n'
balancesheet += '-' * 105 + '\n'
balancesheet += '资产:' + ' ' * (52 - len('资产')) + '|' + '负债:'+' '*(52 - len('负债'))+'\n'
资产负债表={}
资产负债表.setdefault('资产',{})
资产负债表.setdefault('负债',{})

for i in all_information['账户']:#得到每个账户的名字
    if all_information['账户'][i]['属性]'=='资产':
        资产负债表['资产'].setdefault(i,all_information['账户'][i]['余额'])
    if all_information['账户'][i]['属性]' == '负债':
        资产负债表['负债'].setdefault(i,all_information[i]['负债']




        


len of assets=0
len_of_assets=len(资产负债表['资产'])
len_of_liability=len(资产负债表['负债'])
space_资产=' ' * 52+'|'  # '如果资产是空白
for i in 资产负债表['资产']:  # 获得每个资产项目
    balancesheet += ' ' * 4 + i + ' ' * (52 - len(' ' * 4 + i) - len(资产负债表['资产'][i])) + 资产负债表['资产'][i] + '|'
# 4个空格没有准确计算






print(balancesheet)