# 导入random模块
import random

# 生成一个随机的身份证号码
import string


def generate_id(region_code, yearmonthday, sex):
    # 生成顺序码(2位数)
    order = str(random.randint(1, 99)).rjust(2, '0')
    # 生成校验码(1位数)
    check_code = get_check_code(region_code + yearmonthday + order + sex)
    # 拼接身份证号码并返回
    return region_code + yearmonthday + order + sex + check_code


# 计算校验码
def get_check_code(id17):
    # 系数列表
    factor_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    # 校验码列表
    check_code_list = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
    # 根据前17位计算出校验码
    check_code = 0
    for i in range(len(id17)):
        check_code += int(id17[i]) * factor_list[i]
    check_code %= 11
    return check_code_list[check_code]


def passport():
    # 护照
    return random.choice('HM') + random.choice('TSLGDQ') + ''.join(
        random.choices(string.digits + string.ascii_uppercase, k=8)) \
           + ''.join(random.choices(string.digits + string.ascii_uppercase, k=2))


def military():
    # 护照
    return ''.join(random.choices(string.digits + string.ascii_uppercase, k=6)) + ''.join(
        random.choices(string.digits + string.ascii_uppercase, k=2))


def taiwan():
    # 8位数台胞证号码由台胞终身号、签发次数和签发机关代码组成。前六位数字是终身号，用于唯一标识持证人。后两位数字表示签发次数
    return 'L' + ''.join(random.choices(string.digits, k=6)) + ''.join(random.choices(string.digits, k=2))


def hangkangAomen():
    # 通行证证件号码共11位。第1位为字母，“H”字头签发给香港居民，“M”字头签发给澳门居民；第2位至第11位为数字
    return random.choice('HM') + ''.join(random.choices(string.digits, k=10))
