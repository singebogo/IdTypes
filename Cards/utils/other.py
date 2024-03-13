from faker import Faker

from utils.socialCreditCode import generate_uniform_credit_code


class Other():

    def __init__(self, model):
        if model == 0:
            self.fake = Faker(locale='zh_CN')
        else:
            self.fake = Faker()

    def address(self):
        return self.fake.address()

    def name(self):
        return self.fake.name()

    def company(self):
        return self.fake.company()

    def credit_code(self):
        return generate_uniform_credit_code()