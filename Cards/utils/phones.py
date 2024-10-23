# 手机号码段
import random
from .areaCode import AreaCode_inland
# 国内电话长度 11
# 3位网号+4位HLR号+4位的个人代码
PHONE_LEN = 11
PERSON_LEN = 4

country_code = '0086'

mobie_segment = {
    '中国移动号码段': [["134(0-8)", "13(5-9)", "147", "15(0-2)", "15(7-9)", "198"],
                ["17(2,8)", "18(2-4)", "18(7-8)"]],  # 中国移动号码段
    '中国联通号码段': ["13(0-2)", "145", "15(5-6)", "166", "17(1,5,6)", "18(5-6)"],  # 中国联通号码段
    '中国电信号码段': ["133", "149", "153", "17(3, 7)", "18(0,1,9)", "19(1,2,3,9)"],  # 中国电信号码段
    # '中国广电号段': []  # 中国广电号段
}

# 虚拟号码段
vritual_segment = {
    '中国移动': ['167', '170(4,7,8,9)', '171'],
    '中国联通': ['162', '170(0-2)'],
    '中国电信': ['165', '170(3,5,6)'],
}

# 物联网号码段
iot_segment = {
    '中国移动': ['1400', '146'],
    '中国联通': ['1410'],
    '中国电信': ['1440', '148'],  #
}

# 卫星电话号段
satellite_segment = {
    '中国电信': ['1349', '174(00-05)'],  # 电信
    '工信部应急通信': ['174(06-12)'],  # 工信部应急通信
    '海事卫星通信': ['1749'],  # 海事卫星通信
}

category = {
    "手机号码段": mobie_segment,
    "虚拟号码段": vritual_segment,
    "物联网号码段": iot_segment,
    "卫星电话号段": satellite_segment,
}


def basic_num():
    return ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def paser(phone):
    phone = str(phone)
    # ()
    # -  ,
    if '(' in phone and ')' in phone:
        lbracket = phone.find('(')
        rbracket = phone.find(')')
        head = phone[:lbracket]
        bracket = phone[lbracket + 1:rbracket]
        segment = []  # 号码段
        if ',' in bracket:
            segment = [i.strip() for i in bracket.split(',')]
        elif '-' in bracket:
            sections = bracket.split('-')
            segment = [i for i in range(int(sections[0]), int(sections[1]) + 1)]
        else:
            pass
        phone = [head + str(i) for i in segment]
        return phone
    else:
        return [phone, ]


# Home Location Register
def gener(segment, aeraCode, country):
    HLR_l = PHONE_LEN - PERSON_LEN - len(aeraCode) - len(str(segment))
    HLR = "".join(random.choice(basic_num()) for i in range(HLR_l))
    person = "".join(random.choice(basic_num()) for i in range(PERSON_LEN))
    if country:
        return  country_code + '-' + str(segment) + aeraCode + HLR + person
    return str(segment) + aeraCode + HLR + person


def random_phone(country):
    keys = [key for key in category.keys()]
    c_key = random.choice(keys)
    value = category[c_key]
    ikeys = [key for key in value.keys()]
    i_key = random.choice(ikeys)
    value = value[i_key]
    c_segment = random.choice(value)
    # 可能是个list
    if isinstance(c_segment, list):
        c_segment = random.choice(c_segment)
    segments = paser(c_segment)


    akeys = [key for key in AreaCode_inland.keys()]
    a_key = random.choice(akeys)
    a_value = AreaCode_inland[a_key]
    subkeys = [key for key in a_value.keys()]
    sub_key = random.choice(subkeys)
    aeraCode = a_value[sub_key]
    if aeraCode.find('-') > 0:
        aeraCode = aeraCode.split('-')
        aeraCode = random.choice(aeraCode)
    return gener(segments[0], aeraCode[1:], country)



