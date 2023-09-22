# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: 计算各产品各二级单位融资利率
@time: 2022/4/13 9:34
"""

import datetime



class RateUtil:

    def rate_util(self,str1,str2,amount,loan):
        date1 = datetime.datetime.strptime(str1[0:10], "%m/%d/%Y")
        date2 = datetime.datetime.strptime(str2[0:10], "%m/%d/%Y")
        num = (date1 - date2).days
        rate=(amount-loan)*360/num/amount

        return rate



if __name__ == '__main__':

    rate=RateUtil().rate_util('3/20/2024','9/21/2023',781141.58,770930.32)
    print("上海E信通融资利率"+str(rate))

    rate = RateUtil().rate_util('3/15/2024', '9/19/2023', 948782.66, 936585.53)
    print("西南公司E信通融资利率" + str(rate))

    rate = RateUtil().rate_util('9/18/2024', '9/21/2023', 7590188.52, 7391199.08)
    print("集采公司E信通融资利率" + str(rate))

    rate = RateUtil().rate_util('12/29/2023', '9/21/2023', 1541854.39, 1529982.11)
    print("西南公司保理e融资利率" + str(rate))

    rate = RateUtil().rate_util('2/21/2024', '8/31/2023', 1500000.00, 1475350.00)
    print("新疆公司保理e融资利率" + str(rate))

    rate = RateUtil().rate_util('1/24/2024', '7/28/2023', 500000.00, 491500.00)
    print("新疆公司保理e融资利率" + str(rate))

    rate = RateUtil().rate_util('5/23/2024', '8/25/2023', 500000.00, 487911.12)
    print("商砼信融e融资利率" + str(rate))

    rate = RateUtil().rate_util('1/18/2024', '7/25/2023', 1000000.00, 986233.34)
    print("西南信融e融资利率" + str(rate))


