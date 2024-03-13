# 统一社会信用代码
# -*- coding: utf-8 -*-
# 统一社会信用代码中不使用I,O,Z,S,V
"""
"""
import random
import string


def generate_uniform_credit_code():

    code =  random.choice(string.digits + string.ascii_uppercase)
    code +=  random.choice(string.digits + string.ascii_uppercase)
    code +=  ''.join(random.choices(string.digits, k=6))
    code +=  ''.join(random.choices(string.digits, k=9))
    code +=  random.choice(string.digits + string.ascii_uppercase)

    return code


class SocialCreditCode():
    """
    社会统一信用代码
    """

    def __init__(self, countyCode):
        self.countyCode = countyCode

    def getSocialCode(self):
        """
        :return:随机生成统一社会信用代码
        """
        deptCode = self.registrationDepartment()
        institutionCode = self.institutionalCategory(deptCode=deptCode)
        organizationCode = self.organizationCode()
        socialCode = deptCode + institutionCode + self.countyCode + organizationCode
        checkCode = self.unioncode_checknum(socialCode)
        socialCode = socialCode + checkCode

        return socialCode

    def checkSocialCode(self, socialCode):
        '''
        :param socialCode:
        :return: 校验是否正确
        '''
        if len(socialCode) == 18:
            realCheckNum = socialCode[17]
            checkNum = self.unioncode_checknum(socialCode[0:17])
            if checkNum == realCheckNum:
                return '校验通过'
            else:
                return '校验未通过'
        else:
            return '校验未通过，长度不为18位'

    def registrationDepartment(self):
        """
        :return:登记管理部门
        """
        """
        统一社会信用代码的第1位：登记管理部门代码，使用阿拉伯数字或英文字母表示。分为:
        1机构编制；
        2外交；
        3司法行政；
        4文化；
        5民政；
        6旅游；
        7宗教；
        8工会；
        9工商；
        A中央军委改革和编制办公室；
        N农业；
        Y其他。
        """
        SOCIAL_CREDIT_CHECK_CODE_LIST = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'Y']

        return random.choice(SOCIAL_CREDIT_CHECK_CODE_LIST)

    def institutionalCategory(self, deptCode):
        """
        :return:机构类别
        """
        """
        统一社会信用代码的第2位：机构类别代码，使用阿拉伯数字表示。分为：
　　      1机构编制：1机关，2事业单位，3中央编办直接管理机构编制的群众团体，9其他；
　　      2外交：1外国常住新闻机构，9其他；
　　      3司法行政：1律师执业机构，2公证处，3基层法律服务所，4司法鉴定机构，5仲裁委员会，9其他；
　　      4文化：1外国在华文化中心，9其他；
　　      5民政：1社会团体，2民办非企业单位，3基金会，9其他；
　　      6旅游：1外国旅游部门常驻代表机构，2港澳台地区旅游部门常驻内地（大陆）代表机构，9其他；
         7宗教：1宗教活动场所，2宗教院校，9其他；
　　      8工会：1基层工会，9其他；
　　      9工商：1企业，2个体工商户，3农民专业合作社；
　　      A中央军委改革和编制办公室：1军队事业单位，9其他；
　　      N农业：1组级集体经济组织，2村级集体经济组织，3乡镇级集体经济组织，9其他；
　　      Y其他：不再具体划分机构类别，统一用1表示。
        """
        deptCode = str(deptCode)
        if deptCode == '1':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '3', '9']
        elif deptCode == '2':
            INSTITUTIONAL_CODE_LIST = ['1', '9']
        elif deptCode == '3':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '3', '4', '5', '9']
        elif deptCode == '4':
            INSTITUTIONAL_CODE_LIST = ['1', '9']
        elif deptCode == '5':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '3', '9']
        elif deptCode == '6':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '9']
        elif deptCode == '7':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '9']
        elif deptCode == '8':
            INSTITUTIONAL_CODE_LIST = ['1', '9']
        elif deptCode == '9':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '3']
        elif deptCode == 'A':
            INSTITUTIONAL_CODE_LIST = ['1', '9']
        elif deptCode == 'N':
            INSTITUTIONAL_CODE_LIST = ['1', '2', '3', '9']
        else:
            INSTITUTIONAL_CODE_LIST = ['1']

        return random.choice(INSTITUTIONAL_CODE_LIST)

    def organizationCode(self):
        """
        :return: 组织机构code
        """
        weights = [3, 7, 9, 10, 5, 8, 4, 2]  # 加权因子
        CODE_DICT = {
            '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19, 'L': 20, 'M': 21,
            'N': 22, 'P': 23, 'Q': 24,
            'R': 25, 'T': 26, 'U': 27, 'W': 28, 'X': 29, 'Y': 30}
        total = 0
        organizationCode = ""
        for i in range(8):
            organizationCode += random.choice(list(CODE_DICT))
        for i in range(len(organizationCode)):
            ci = organizationCode[i]
            total += CODE_DICT[ci] * weights[i]

        checkNum = 11 - (total % 11)
        if checkNum == 10:
            checkNum = 'X'
        else:
            if checkNum == 11:
                checkNum = '0'
            else:
                checkNum = str(checkNum)
        organizationCode = organizationCode + checkNum

        return organizationCode

    def unioncode_checknum(self, code):
        """
        :param code:
        :return:校验位
        """
        weights = [1, 3, 9, 27, 19, 26, 16, 17, 20, 29, 25, 13, 8, 24, 10, 30, 28]
        CODE_DICT = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
            'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'J': 18, 'K': 19, 'L': 20, 'M': 21,
            'N': 22, 'P': 23, 'Q': 24,
            'R': 25, 'T': 26, 'U': 27, 'W': 28, 'X': 29, 'Y': 30}
        total = 0
        for i in range(len(code)):
            ci = code[i]
            if ci in ['I', 'O', 'Z', 'S' 'V']:
                return
            total += CODE_DICT[ci] * weights[i]

        pos = 31 - (total % 31)
        if pos == 31:
            pos =0
        for k, v in CODE_DICT.items():
            if v == pos:
                return k

