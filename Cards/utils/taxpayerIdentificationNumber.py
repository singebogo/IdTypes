import random
import re
import string
from utils.organization import organizationCode, organizationDigitsCode

def nsrsbh_15():
    return ''.join(random.choices(string.digits + string.ascii_uppercase, k=15))


def nsrsbh_18(region):
    # - 18 位纳税人识别号由 6 位行政区划码、9 位组织机构代码、1 位校验码组成；
    organCode = organizationDigitsCode()
    code = random.choice(string.digits)
    return region + organCode + code.upper() if isinstance(code, str) else str(code)


def nsrsbh_20(region):
    organCode = organizationDigitsCode()
    return region + organCode + ''.join(random.choices(string.digits, k=5))
