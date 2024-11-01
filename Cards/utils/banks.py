import random


# 银行卡一般为16位或者19位
# BIN  中间位   校验位
# Bank Identification Number。BIN由6位数字表示，出现在卡号的前6位
# 　4　卡号长度及结构
# 　银行卡的卡号长度及结构符合ISO 7812-1有关规定，由13-19位数字表示，具体由以下几部分组成：
# 　9  XXXXX 　　　　　　X……X 　　　　X　　　发卡行标识代码 　　　 自定义位 　　 校验位
# 　5　发卡行标识代码
# 　发卡行标识代码标识发卡机构，由6位数字表示，第一位固定为“9”，后5位由BIN注册管理机构分配。
# 　6　自定义位
# 　发卡行自定义位，由6-12位数字组成。
# 　7　校验位
# 　卡号最后一位数字，根据校验位前的数字计算得到。计算方法见附录A。

# Major Industry Identifier  行业标识
MII = {
    0: "ISO/TC 68 和其他行业使用",
    1: "航空",
    2: "航空和其他未来行业使用",
    3: "运输、娱乐和金融财务",
    4: "金融财务",
    6: "商业和金融财务",
    5: "金融财务",
    7: "石油和其他未来行业使用",
    9: "由本国标准机构分配",
    8: "医疗、电信和其他未来行业使用",
}

# 不同卡号对应的发行机构
ISSUER = {

}

def bank():
    pass

def getLastcode( bankNumNoLastcode):
    sum = 0
    for i in bankNumNoLastcode[-1::-2]:
        for m in str(int(i) * 2):
            sum = sum + int(m)
    for j in bankNumNoLastcode[-2::-2]:
        sum = sum + int(j)
    if sum % 10 == 0:
        lastCode = '0'
    else:
        lastCode = str(10 - sum % 10)
    return lastCode