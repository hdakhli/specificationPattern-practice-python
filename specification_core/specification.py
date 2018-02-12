class Specification:

    def __init__(self):
        pass

    def is_satisfied_by(self, candidate):
        raise Exception("not implemented")

    def and_(self, spec):
        return AndSpecification(self, spec)

    def or_(self, spec):
        return OrSpecification(self, spec)

    def not_(self):
        return NotSpecification(self)


class NotSpecification(Specification):

    def __init__(self, first_spec):
        self._first_spec = first_spec

    def is_satisfied_by(self, candidate):
        return not self._first_spec.is_satisfied_by(candidate)


class AndSpecification(Specification):

    def __init__(self, first_spec, second_spec):
        self._first_spec = first_spec
        self._second_spec = second_spec

    def is_satisfied_by(self, candidate):
        return self._first_spec.is_satisfied_by(candidate) and self._second_spec.is_satisfied_by(candidate)


class OrSpecification(Specification):

    def __init__(self, first_spec, second_spec):
        self._first_spec = first_spec
        self._second_spec = second_spec

    def is_satisfied_by(self, candidate):
        return self._first_spec.is_satisfied_by(candidate) or self._second_spec.is_satisfied_by(candidate)
