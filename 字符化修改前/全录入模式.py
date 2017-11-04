#__author:"LIN SHIH-WAI"
#date:  2017/10/31
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
        print(aaa,end=' '*(账号的起始距离-len(aaa)))#打印开头的日期并且对距离做出修正.
        for bbb in all_account_input[x][aaa]:#由于日期下面的是借贷.而借贷下面才是账号.#bbbshi借贷信息.只用于判断
            if bbb=='debt':
                a=0
                flag=True
                while flag:
                    for zzz in all_account_input[x][aaa][bbb]:#得到所有的账户信息.
                        a+=1
                        print(zzz,end=' '*(debt的起始距离-len(aaa)-len(zzz)))#zzz是账号
                        print('%s'%all_account_input[x][aaa][bbb][zzz])
                        if a==len(all_account_input[x][aaa][bbb]):
                            flag=False
            if bbb=='credit':
                a=0
                flag=True
                while flag:
                    for zzz in all_account_input[x][aaa][bbb]:#得到所有的账户信息.
                        a+=1
                        print(' '*(账号的起始距离-len(aaa)),end='')
                        print(zzz,end=' '*(credit的起始距离-len(aaa)-len(zzz)))#zzz是账号
                        print('%s'%all_account_input[x][aaa][bbb][zzz])
                        if a==len(all_account_input[x][aaa][bbb]):
                            flag=False
                            # print('交易记录:%s\n'%all_account_input[x][aaa]['描述'].center(101-len('交易记录:%s'%all_account_input[x][aaa]['描述']),' ' ))
#输入记录器,方便返回.
def recond_it(count_recond,y):
    count_recond+=1
    if count_recond not in type_recond:
        type_recond.setdefault(count_recond,y)
    if count_recond in type_recond:
        type_recond[count_recond]=y





all_information={'财务报表':{'资产负债表':'','利润表':'','现金流表':''},'账户':{'cash':{'debt':{'2015.01.01':300,'2015.03.03':900},'credit':{'2015.01.02':700,'2015.03.03':1200},'流动性':'流动资产','属性':'资产'}}}
all_account_input={'2017.01.01':{'2017.01.01':{'debt':{'cash':10000},'credit':{'equipment':10000},'描述':'测试'},'2017.03.24':{'debt':{'equipment':10000},'credit':{'cash':80000,'account receiable':20000},'描述':'测试'}}}
accounting_print('2017.01.01')
type_recond={}#只记录二级目录一下的信息
while True:#一级目录 还得有最初的目录
    time_of_start=input('请输入编制日期,如2017.01.01:')
    all_account_input.setdefault(time_of_start,{})
    accounting_print(time_of_start)
    while True:#type_recond记录这里的信息.
        account_time=input('请输入日期')
        all_account_input[time_of_start].setdefault(account_time,{})
        while True:#借贷双向记录
            account_name=input('请输入账号名称:[c]结算(该日期借贷平衡转到下日期)')
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
                    all_information['账户'][account_name][account_type].setdefault(account_time,account_money)
                if account_time not in all_information['账户'][account_name]['debt']:
                    all_information['账户'][account_name][account_type][account_time]=account_money
            if str(account_type) == 'credit':
                if account_time not in all_information['账户'][account_name]['credit']:
                    all_information['账户'][account_name][account_type].setdefault(account_time, account_money)
                if account_time not in all_information['账户'][account_name]['credit']:
                    all_information['账户'][account_name][account_type][account_time] = account_money
            accounting_print(time_of_start)





