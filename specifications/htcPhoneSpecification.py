from specification_core.specification import Specification

class HtcPhoneSpecification(Specification):

    def is_satisfied_by(self, phone):
        return phone['brand'] == 'HTC'
