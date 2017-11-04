#__author:"LIN SHIH-WAI"
#date:  2017/10/30

#字典形式all_information第一层 key财务报表,子账户
#财务报表第key资产负债表,利润表,现金流表,
# 子账户key各类账户
#子账户下 比如一个信息
#--------------------函数定义区--------------------------
def printinformation(x):
    pass
    # distance = 0 #格式打印的距离计算
    # if '属性' not in all_information:
    #     def_type=input('请定义%s账户的属性:')
    # if all_information[x]['属性']=='account':
    #     print('x'.center(distance,''))
    #     print(''.center(globals(distance),'-'))

def account_edit(x):#子账户的编辑
    printinformation((all_information['account'][x]))
    while True:
        edit=input('输入要修改的项目的:')
def printsheetbalance():
    printinformation()

# def print_account(x):#自定义打印
#     distance=0
#     data_list=[]
#     money_list=
#     for every_data in all_information['账户'][x]['debt']:
#         data_list.append(len(i))
#     for every_data in all_information['账户'][x]['credit']:
#         data_list.append(len(i))
#     max_data=max(data_list)
#     for every_money in all_information['账户'][x]['金额']
#
#     all_information['账户'][x]
#     print('x'.center(distance, ''))
def print_account(x):
    print('流动性:%s'%all_information['账户'][x]['流动性'],end='')
    距离=0
    距离=30-len('流动性:%s'%all_information['账户'][x]['流动性'])-len('属性:%s'%all_information['账户'][x]['属性'])
    print("account:%s".center(距离,' ')%x,end='')
    print('属性:%s'%all_information['账户'][x]['属性'])
    print('-'*51)#左边25个右边25个
    data_list=[]#获取借贷中的所有的日期列表
    for i in all_information['账户'][x]['debt']:
        data_list.append(i)
    for v in all_information['账户'][x]['credit']:#2017.01.01
        if v not in data_list:
            data_list.append(v)

    data_list.sort(key=lambda k:(k[2],k[3],k[4],k[5],k[6],k[7]),reverse=False)#排序所有的时间,顺便知道有多少行.
# --------------------------以上是排序层,对日期形成tuple然后排序--------------------------------------------------
    sum_debt = 0
    sum_credit = 0
    minus_it = 0
    for v in all_information['账户'][x]['debt']:  # 所有debt的日期
        sum_debt += all_information['账户'][x]['debt'][v]
    for k in all_information['账户'][x]['credit']:  # 所有debt的日期
        sum_credit += all_information['账户'][x]['credit'][k]
    if sum_debt >= sum_credit:
        minus_it = sum_debt - sum_credit
    if sum_debt < sum_credit:
        minus_it = sum_credit - sum_debt

# -------------------------------------以上是计算余额----------------------------------------------------
    list_show = ''
    for i in data_list:
        space=0
        if i in all_information['账户'][x]['debt']:
            list_show+=i
            space=25-int(len(i))-int(len(str(all_information['账户'][x]['debt'][i])))-int(len('|'))
            list_show+=' '*space+str(all_information['账户'][x]['debt'][i])+'|'
        if i not in all_information['账户'][x]['debt']:
            list_show+=' '*24+'|'
        if i in all_information['账户'][x]['credit']:
            list_show+=i
            space=25-len(i)-len(str(all_information['账户'][x]['credit'][i]))-len('|')
            list_show+=' '*space+str(all_information['账户'][x]['credit'][i])+'\n'
        if i not in all_information['账户'][x]['credit']:
            list_show+='\n'
    list_show+='-'*51
    list_show+='\n'
    if sum_debt > sum_credit:
        list_show+=str(minus_it)
    if sum_debt < sum_credit:
        space = 25-len(str(minus_it)) - len('|')
        list_show += ' '*24+'|'+' '*space+str(minus_it)
    print(list_show)








all_information={'财务报表':{'资产负债表':'','利润表':'','现金流表':''},'账户':{'cash':{'debt':{'2015.01.01':300,'2015.03.03':900},'credit':{'2015.01.02':700,'2015.03.03':1200},'流动性':'流动资产','属性':'资产'}}}
# printinformation(all_information)

print_account('cash')
# while True:
#     information=input('请输入指令,q[退出],s[保存],e[编辑],c[查询],a[添加(账户)]:')
#     if information=='q':
#         exit('程序已经退出,感谢你的使用,作者"LIN SHIH-WAI,版本0.1v')
#     if information=='s':
#         while True:
#             break #所有txt保存
#     if information=='c':
#         while True:
#             information = input('请输入要特定查询的账户:')
#             printinformation(information)
#     if information=='a':
#         all_information.fromkeys('账户')
#         all_information['属性']
#     if information=='e':
#         while True:
#             information = input('请输入要特定编辑的账户,a[总览]:')
#             if information=='a':
#                 printinformation(all_information)
#             else:
#                 printinformation(all_information[information])
#             if information not in all_information:
#                 information_e=input('该账户不存在是否添加 y/n:')
#                 if information_e=='y':
#                     all_information.setdefault(information)
#                 if information_e=='n':
#                     continue

#--------------------------------直接写写一个账号添加.------------------------
while True:
    account_add=input('请输入要添加的账号名')#添加帐户名
    if account_add not in all_information['账户']:
        all_information['账户'].setdefault(account_add, {})
    account_shuxing=input('请输入%s的属性例如assets liability'%account_add)
    all_information['账户'][account_add].setdefault('属性',account_shuxing)
    account_current=input('请输入%s的流动性属性:'%account_add)
    all_information['账户'][account_add].setdefault('流动性',account_current)
    while True:#要不还得重复输入.这里由个while循环
        information_type=input('借[debt]还是贷[credit] 输入debt和credit:(结束请安q)')#添加是借还是贷
        if information_type=='q':
            break
        if information_type!='debt'and 'credit':
            print('必须输入debt或者credit')
            continue
        if information_type=='debt'or'credit':
            all_information['账户'][account_add].setdefault(information_type,{})
            data_input=input('请输入日期格式2017.01.01:')
            all_information['账户'][account_add][information_type].setdefault(data_input,0)
            how_much=int(input('请输入金额数量:'))
            all_information['账户'][account_add][information_type][data_input]=how_much
        print_account(account_add)











