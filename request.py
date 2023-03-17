from base_storage import BaseStorage
from extensions import BadRequest


class Request:
    """
    Запрос от пользователя
    """

    def __init__(self, request: str, storages: dict[str, BaseStorage]):
        match request.split():
            case _, amount, product, _, from_, _, to_:
                pass
            case _:
                raise BadRequest()

        if amount.isdigit() and from_ in storages and to_ in storages:
            self.amount = int(amount)
            self.from_storage = from_
            self.to_storage = to_
            self.product = product
        else:
            raise BadRequest()

