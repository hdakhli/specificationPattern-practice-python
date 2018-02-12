from specification_core.specification import Specification

class SamsungPhoneSpecification(Specification):

    def is_satisfied_by(self, phone):
        return phone['brand'] == 'SAMSUNG'
