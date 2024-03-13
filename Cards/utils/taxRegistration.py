import random
import string

from utils.IDCards import generate_id
from utils.organization import organizationDigitsCode


def companyTaxRegistration(region):
    organCode = organizationDigitsCode()
    return region + organCode


def TaxRegistration(region):
    # 生成年份(4位数)
    year = str(random.randint(1949, 2022))
    # 生成月份(2位数)
    month = str(random.randint(1, 12)).rjust(2, '0')
    # 生成日期(2位数)
    day = str(random.randint(1, 28)).rjust(2, '0')

    return generate_id(region, year + month + day, ''.join(random.choice(string.digits))) + "00"
