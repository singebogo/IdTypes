import random
import string


def getchecknum(code): ##定义企业注册码校验码计算函数
    n = 10
    for i in range(len(code)):
        n = (int(code[i]) + n ) % 10
        if n == 0:
            n = 10
        n = n* 2 % 11
    if n == 0:
        s = 1
    elif n == 1:
        s = 0
    else:
        s = 11 - n
    return str(s)


# 前六位为行政区代码，中间8位顺序编码，最后一位为根据ISO 7064:1983.MOD 11-2校验码计算出来的检验码
def iIndustrialCode(region):
    sort = ''.join(random.choices(string.digits, k=8))
    code = region+str(sort)
    return code + getchecknum(code)
