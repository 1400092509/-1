#__author:"LIN SHIH-WAI"
#date:  2017/10/30

#字典形式all_information第一层 key财务报表,子账户
#财务报表第key资产负债表,利润表,现金流表,
# 子账户key各类账户
#子账户下 比如一个信息
#--------------------函数定义区--------------------------
#--------------------属性判断函数--------------------------
def add_shuxing_and_check(x):
    if '属性' not in all_information['账户'][x]:
        account_shuxing = input(
            "请输入%s的属性例如[1]assets [2]liability [3]revenues [4]expenses [5]sells [6]COGS [7]stockholders' equity:" % x)
        if str(account_shuxing) == '1':
            account_shuxing = '资产'
        if str(account_shuxing) == '2':
            account_shuxing = '负债'
        if str(account_shuxing) == '3':
            account_shuxing = 'revenues'
        if str(account_shuxing) == '4':
            account_shuxing = 'expenses'
        if str(account_shuxing) == '5':
            account_shuxing = 'sells'
        if str(account_shuxing) == '6':
            account_shuxing = 'COGS'
        if str(account_shuxing) == '7':
            account_shuxing = "所有者权益"
        all_information['账户'][x].setdefault('属性', account_shuxing)
        # ------------------------账户属性的添加-----------------------------------------
    if '流动性' not in all_information['账户'][x]:
        account_current = input('请输入%s的流动性属性 [1]current assets [2]current liability [3]所有者权益:' % x)
        if str(account_current) == '1':
            account_current = '流动资产'
        if str(account_current) == '2':
            account_current = '流动负债'
        if str(account_current) == '3':
            account_current = '所有者权益排名'
        all_information['账户'][x].setdefault('流动性', [])
        all_information['账户'][x]['流动性'].append(account_current)
        all_information['账户'][x]['流动性'].append('0')
    all_information['账户'][x].setdefault('debt', {})
    all_information['账户'][x].setdefault('credit', {})

#-----------------------------特定日期的删除-----------------------------------
def del_it(x):
    del_data = input('请输入你要删除的日期:')
    if del_data in all_information['账户'][account_add][x]:
        del all_information['账户'][account_add][x][del_data]
        print_account(account_add)
    else:
        print('不存在或输入错误')


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

# ---------------------------------------子账号的打印--------------------------------
def print_account(x):#子账号的打印
    print('流动性分类[排名]:%s[%s]'%(all_information['账户'][x]['流动性'][0],all_information['账户'][x]['流动性'][1]),end='')
    距离=0
    距离=65-len('流动性分类[排名]:%s[%s]'%(all_information['账户'][x]['流动性'][0],all_information['账户'][x]['流动性'][1]))-len('属性:%s'%all_information['账户'][x]['属性'])
    print("account:%s".center(距离,' ')%x,end='')
    print('属性:%s'%all_information['账户'][x]['属性'])
    print('-'*101)#左边25个右边25个
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
            space=50-int(len(i))-int(len(str(all_information['账户'][x]['debt'][i])))-int(len('|'))
            list_show+=' '*space+str(all_information['账户'][x]['debt'][i])+'|'
        if i not in all_information['账户'][x]['debt']:
            list_show+=' '*49+'|'
        if i in all_information['账户'][x]['credit']:
            list_show+=i
            space=50-len(i)-len(str(all_information['账户'][x]['credit'][i]))-len('|')
            list_show+=' '*space+str(all_information['账户'][x]['credit'][i])+'\n'
        if i not in all_information['账户'][x]['credit']:
            list_show+='\n'
    list_show+='-'*101
    list_show+='\n'
    if sum_debt > sum_credit:
        list_show+=str(minus_it)
    if sum_debt < sum_credit:
        space = 50-len(str(minus_it)) - len('|')
        list_show += ' '*49+'|'+' '*space+str(minus_it)
    if '余额' not in all_information['账户'][account_add]:
        all_information['账户'][account_add].setdefault('余额',minus_it)
    if '余额' in all_information['账户'][account_add]:
        all_information['账户'][account_add]['余额']=minus_it
    print(list_show)

def accounting_print(x):#全账号打印
    print('日记表模式'.center(101,' '))
    print('编制日期:%s'%x,end=' '*10)
    print('账号',end=' '*35)
    print('debt',end=' '*20)
    print('credit')
    print('-'*101)#左边25个右边25个
    data_list=[]#获取借贷中的所有的日期列表
    账号的起始距离=len('编制日期:%s'%x+' '*10)#前方空格数
    debt的起始距离=len('编制日期:%s'%x+' '*10)+len('账号'+' '*35)
    credit的起始距离=len('编制日期:%s'%x+' '*10)+len('账号'+' '*35)+len('debt'+' '*20)
    for i in all_account_input[x] :
        data_list.append(i)
    data_list.sort(key=lambda k:(k[2],k[3],k[4],k[5],k[6],k[7]),reverse=False)#排序所有的时间,顺便知道有多少行.
# --------------------------以上是排序层,对日期形成tuple然后排序--------------------------------------------------
    for aaa in data_list:#得到所有的账户的日期,编制日期
        print(aaa,end='')#打印开头的日期并且对距离做出修正.
        b=0
        for bbb in all_account_input[x][aaa]:#由于日期下面的是借贷.而借贷下面才是账号.#bbbshi借贷信息.只用于判断
            if bbb=='debt':
                a=0
                flag=True
                while flag:
                    for zzz in all_account_input[x][aaa][bbb]:#得到所有的账户信息.
                        a+=1
                        if b==0:
                            print(' '*((账号的起始距离)-len(aaa))+zzz,end=' '*(debt的起始距离-len(aaa)-len(zzz)))#zzz是账号
                        if b!=0:
                            print(' '*账号的起始距离+zzz,end=' '*(debt的起始距离-len(zzz)-len(aaa)))
                        print('%s'%all_account_input[x][aaa][bbb][zzz])
                        b+=1
                        if a==len(all_account_input[x][aaa][bbb]):
                            flag=False
            if bbb=='credit':
                a=0
                flag=True
                while flag:
                    for zzz in all_account_input[x][aaa][bbb]:#得到所有的账户信息.
                        a+=1
                        if b==0:
                            print(' '*(账号的起始距离-len(aaa)),end='')
                        if b!=0:
                            print(' '* (账号的起始距离),end='')
                        print(zzz,end=' '*(credit的起始距离-len(aaa)-len(zzz)))#zzz是账号
                        print('%s'%all_account_input[x][aaa][bbb][zzz])
                        b+=1
                        if a==len(all_account_input[x][aaa][bbb]):
                            flag=False
        if '描述' in all_account_input[x][aaa]:
            print('交易描述:%s\n' %all_account_input[x][aaa]['描述'])



                            # print('交易记录:%s\n'%all_account_input[x][aaa]['描述'].center(101-len('交易记录:%s'%all_account_input[x][aaa]['描述']),' ' ))
#输入记录器,方便返回.
def recond_it(count_recond,y):
    count_recond+=1
    if count_recond not in type_recond:
        type_recond.setdefault(count_recond,y)
    if count_recond in type_recond:
        type_recond[count_recond]=y

#函数定义区域
all_account_input={'2017.01.01':{'2017.01.01':{'debt':{'cash':10000},'credit':{'equipment':10000},'描述':'测试'},'2017.03.24':{'debt':{'equipment':10000},'credit':{'cash':80000,'account receiable':20000},'描述':'测试'}}}
all_information={'财务报表':{'资产负债表':'','利润表':'','现金流表':''},'账户':{'cash':{'debt':{},'credit':{},'流动性':['流动资产','1'],'属性':'资产'},'notes receiable':{'debt':{},'credit':{},'流动性':['流动资产','2'],'属性':'资产'},'accounts receiable':{'debt':{},'credit':{},'流动性':['流动资产','3'],'属性':'资产'},'supplies':{'debt':{},'credit':{},'流动性':['长期资产','1'],'属性':'资产'},'land':{'debt':{},'credit':{},'流动性':['长期资产','2'],'属性':'资产'},'building':{'debt':{},'credit':{},'流动性':['长期资产','3'],'属性':'资产'},'equipment':{'debt':{},'credit':{},'流动性':['长期资产','4'],'属性':'资产'},'notes payable':{'debt':{},'credit':{},'流动性':['流动负债','1'],'属性':'负债'},'accounts payable':{'debt':{},'credit':{},'流动性':['流动负债','2'],'属性':'负债'},'salaries payable':{'debt':{},'credit':{},'流动性':['流动负债','3'],'属性':'负债'},'capitial stock':{'debt':{},'credit':{},'流动性':['所有者权益排名','1'],'属性':'所有者权益'},'retained earnings':{'debt':{},'credit':{},'流动性':['所有者权益排名','2'],'属性':'所有者权益'}}}
flag_account_edit=False
flag_all_account_edit=False
#计算区域.直接给出计算值,比如net income. 比如所有者权益.


#------------------------------------------主目录区------------------------------------------------
while True:
    while True:
        information=input('[1]日记账模式,[2]单账户操作,[3]生成财务报表,[q]退出程序]:')
        if str(information)=='1':
            flag_all_account_edit=True
            flag_account_edit=False
            break
        if str(information)=='2':
            flag_all_account_edit=False
            flag_account_edit=True
            break
        if information=='q':
            exit('程序已经退出,感谢你的使用,作者"LIN SHIH-WAI,版本0.1v')


    #--------------------------------单账户操作.------------------------
    while flag_account_edit:
        account_add=input('请输入要添加的账号名[q]回到主目录:')#添加帐户名
        if account_add=='q':
            break
        if account_add not in all_information['账户']:
            all_information['账户'].setdefault(account_add, {})

    #----------------------------添加账户和进入账户---------------------------------------
        add_shuxing_and_check(account_add)
        while True:#要不还得重复输入.这里由个while循环
            print_account(account_add)
            information_type=input('%s账户添加输入[1]debt和[2]credit:(退出该账户[q],删除日期[d],清空账户[c])'%account_add)#添加是借还是贷
            if information_type=='c':
                all_information['账户'][account_add]['debt'].clear()
                all_information['账户'][account_add]['credit'].clear()
                print_account(account_add)
                continue
            if information_type=='q':
                break
            while information_type=='d':
                del_type=input('请选择要删除的账号类型[1]debt,[2]credit:返回按[q]')
                if del_type=='q':
                    print_account(account_add)
                    break
                if del_type == '1':
                    del_type = 'debt'
                if del_type == '2':
                    del_type = 'credit'
                del_it(del_type)
            if information_type=='1':
                information_type='debt'
            if information_type=='2':
                information_type='credit'
            if information_type=='debt'or'credit':
                all_information['账户'][account_add].setdefault(information_type,{})
                data_input=input('请输入日期格式2017.01.01:')
                all_information['账户'][account_add][information_type].setdefault(data_input,0)
                how_much=int(input('请输入金额数量:'))
                all_information['账户'][account_add][information_type][data_input]=how_much
            else:
                print('必须输入1和2')

    # ----------------------------------------------日记表输入-------------------------------------------
    # ----------------------------------------------日记表输入-------------------------------------------
    # ----------------------------------------------日记表输入-------------------------------------------
    # ----------------------------------------------日记表输入-------------------------------------------
    # ----------------------------------------------日记表输入-------------------------------------------
    # ----------------------------------------------日记表输入-------------------------------------------
    #----------------------------------------------日记表输入-------------------------------------------

    type_recond={}#只记录二级目录一下的信息
    while flag_all_account_edit:#一级目录 还得有最初的目录
        time_of_start=input('请输入编制日期,如2017.01.01:[q]退出')
        if time_of_start=='q':
            break
        all_account_input.setdefault(time_of_start,{})
        accounting_print(time_of_start)
        while True:#type_recond记录这里的信息.
            account_time=input('请输入日期:[q]退出')
            if account_time=='q':
                break
            all_account_input[time_of_start].setdefault(account_time,{})
            while True:#借贷双向记录
                account_name=input('请输入账号名称:[c]结算(该日期借贷平衡转到下日期)[q]退出')
                if account_name=='q':
                    break
                if account_name=='c':
                    sum_debt=0
                    sum_credit=0
                    for k in all_account_input[time_of_start][account_time]:#进入到了借贷账户.读取的每个子账户的key
                        for v in all_account_input[time_of_start][account_time][k]:#读取具体的金额
                            if k=='debt':
                                sum_debt+=int(all_account_input[time_of_start][account_time][k][v])
                            if k=='credit':
                                sum_credit+=int(all_account_input[time_of_start][account_time][k][v])
                    if '描述'not in all_account_input[time_of_start][account_time]:
                        the_information=input('请输入对这次交易的描述:')
                        all_account_input[time_of_start][account_time].setdefault('描述',the_information)
                        accounting_print(time_of_start)
                    if sum_credit-sum_debt==0:#借贷平衡.
                        break
                    if sum_credit-sum_debt!=0:
                        print('借贷不平衡,不能结算,请检查账户是否输入完整')
                        continue
                account_type=input('请输入[1]debt或者[2]credit:')
                account_money=input('请输入金额:')
                if str(account_type)=='1':
                    account_type='debt'
                if str(account_type)=='2':
                    account_type='credit'
                all_account_input[time_of_start][account_time].setdefault(account_type,{})
                if account_name not in all_account_input[time_of_start][account_time][account_type]:
                    all_account_input[time_of_start][account_time][account_type].setdefault(account_name,account_money)
                if account_name in all_account_input[time_of_start][account_time][account_type]:
                    all_account_input[time_of_start][account_time][account_type][account_name]=account_money
                if account_name not in all_information['账户']:
                    all_information['账户'].setdefault(account_name,{})
                    all_information['账户'][account_name].setdefault('debt',{})
                    all_information['账户'][account_name].setdefault('credit',{})
                if str(account_type)=='debt':
                    if account_time not in all_information['账户'][account_name]['debt']:
                        all_information['账户'][account_name][account_type].setdefault(account_time,int(account_money))
                    if account_time not in all_information['账户'][account_name]['debt']:
                        all_information['账户'][account_name][account_type][account_time]=int(account_money)
                if str(account_type) == 'credit':
                    if account_time not in all_information['账户'][account_name]['credit']:
                        all_information['账户'][account_name][account_type].setdefault(account_time, int(account_money))
                    if account_time not in all_information['账户'][account_name]['credit']:
                        all_information['账户'][account_name][account_type][account_time] = int(account_money)
                    # ------------------------账户属性的添加-----------------------------------------
                add_shuxing_and_check(account_name)
                accounting_print(time_of_start)
#all_information={'财务报表':{'资产负债表':'','利润表':'','现金流表':''},'账户':{'cash':{'debt':{'2015.01.01':300,'2015.03.03':900},'credit':{'2015.01.02':700,'2015.03.03':1200},'流动性':'流动资产','属性':'资产'}}}
