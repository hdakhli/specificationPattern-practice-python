from specification_core.specification import Specification

class PremiumPhoneSpecification(Specification):

    def is_satisfied_by(self, phone):
        return phone['cost'] >= 400 and phone['type'] != 'BASIC'
