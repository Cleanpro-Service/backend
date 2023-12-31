from drf_spectacular.utils import OpenApiExample

ORDER_POST_SERIALIZER_SCHEMA: dict[str, any] = {
    'exclude_fields': (
        'creation_date',
        'creation_time',
    ),
    'examples': [
        OpenApiExample(
            'Заказ №1',
            description='Пример заказа',
            value={
                "user": {
                    "username": "Иван Иванович",
                    "email": "ivanstar@email.com",
                    "phone": "+7 777 777 77 77",
                },
                "comment": "Дома много шерсти, у меня собака.",
                "total_sum": 1000000,
                "total_time": 80,
                "cleaning_type": 1,
                "services": [
                    {
                        "id": 1,
                        "amount": 2,
                    },
                    {
                        "id": 3,
                        "amount": 1,
                    }
                ],
                "rooms_number": 1,
                "bathrooms_number": 3,
                "address": {
                    "city": 11,
                    "street": 11,
                    "house": 15,
                    "entrance": 15,
                    "floor": 15,
                    "apartment": 15,
                },
                "cleaning_date": "2023-11-12",
                "cleaning_time": "15:30",
            },
        ),
    ],
}

ORDER_RATING_SERIALIZER_SCHEMA: dict[str, any] = {
    'examples': [
        OpenApiExample(
            'Отзыв на заказ',
            description='Пример отзыва на выполненный заказ.',
            value={
                "text": "string",
                "score": 5,
            },
        ),
    ],
}

RATING_SERIALIZER_SCHEMA = {
    'examples': [
        OpenApiExample(
            'Отзывы',
            description='Отзывы клиентов.',
            value={
                "id": 0,
                "username": "string",
                "pub_date": "2023-10-25T13:06:37.319Z",
                "text": "Замечательно и быстро убрали квартиру!",
                "score": 5,
            },
        ),
    ],
}
