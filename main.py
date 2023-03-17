from extensions import BadRequest, NoGoodsInStorage, NotEnoughGoods, NotEnoughSpace, MaxUniqueItemsInStorage
from request import Request
from shop import Shop
from storage import Storage


def main():

    print('Отправьте запрос: "Доставить 5 чипсы из склад в магазин"\n')

    while True:
        user_input = input()

        try:
            request = Request(user_input, storages)
        except BadRequest as error:
            print(error.message)
            continue

        delivery_from = storages[request.from_storage]
        delivery_to = storages[request.to_storage]

        try:
            delivery_from.remove(request.product.capitalize(), request.amount)
        except (NoGoodsInStorage, NotEnoughGoods) as error:
            print(error.message)
            continue

        try:
            delivery_to.add(request.product.capitalize(), request.amount)
        except (NotEnoughSpace, MaxUniqueItemsInStorage) as error:
            delivery_from.add(request.product.capitalize(), request.amount)
            print(error.message)
            continue

        print(f'Нужное количество есть в {request.from_storage}')
        print(f'Курьер забрал {request.amount} {request.product} из {request.from_storage}')
        print(f'Курьер везёт {request.amount} {request.product} из {request.from_storage} в {request.to_storage}')
        print(f'Курьер доставил {request.amount} {request.product} в {request.to_storage}\n')
        print('=' * 25)
        print(storage)
        print('=' * 25)
        print(shop)
        print('=' * 25)


if __name__ == '__main__':
    storage = Storage()
    shop = Shop()

    storages = {
        'магазин': shop,
        'склад': storage,
    }

    storage.add('Мука', 8)
    storage.add('Сало', 13)
    storage.add('Чипсы', 10)
    storage.add('Пиво', 24)
    storage.add('Кофе', 11)
    storage.add('Чай', 10)
    storage.add('Шоколад', 7)
    storage.add('Хлеб', 6)

    shop.add('Пиво', 5)
    shop.add('Чипсы', 4)
    shop.add('Сало', 3)

    main()

