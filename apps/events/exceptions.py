
class UseCaseException(Exception):
    pass


class AplicationNotFoundUseCase(UseCaseException):
    pass


class CategoryNotFoundUseCase(UseCaseException):
    pass


class CategoryWithoutStandardUseCase(UseCaseException):
    pass