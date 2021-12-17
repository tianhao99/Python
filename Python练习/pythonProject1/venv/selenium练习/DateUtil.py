###############################################################
# 本文件存放日期处理的工具类
# 
# 周宏成为东北财经的教学而编写的演示程序
###############################################################
import numpy as np
import datetime,calendar
from dateutil.relativedelta import relativedelta

def getOptLastTradeDate( deliveryMonth ):
    '''
    根据期货交割月计算出期权的到期日( 交割月前一个月的第10个交易日）
    :param deliveryMonth:'yyMM'
    :return:  datetime
    '''

    # 获得交割月的前一个月的第1天
    strFirstDayOfDyMonth = str(20000000 + np.int64(deliveryMonth) * 100 + 1);
    firstDayOfDyMonth = datetime.datetime.strptime(strFirstDayOfDyMonth, '%Y%m%d')
    firstDayOfLastMonth= firstDayOfDyMonth + relativedelta(months=-1)

    # 获得交割月前一个月份的第10个交易日
    oneday = datetime.timedelta(days=1)
    currentDate = firstDayOfLastMonth
    num = 1;
    while( num <= 10 ):
        currentDate += oneday
        if(currentDate.weekday() != calendar.SATURDAY and currentDate.weekday()!= calendar.SUNDAY):
            num = num + 1
    return currentDate


if __name__ == '__main__':
    deliveryMonth = '2004'
    xxx = getOptLastTradeDate(deliveryMonth)
    print( xxx )
