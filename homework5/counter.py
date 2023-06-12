"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до sbrosa
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    # Создаем счетчик экземпляров класса и инициализируем его значением 0
    cls.__instances_count = 0

    # Функция-обертка, которая будет вызываться при создании нового экземпляра класса
    def wrapper(*args, **kwargs):
        # Вызываем оригинальный конструктор класса с помощью super()
        instance = super(cls, cls).__new__(cls)
        # Увеличиваем значение счетчика экземпляров класса
        cls.__instances_count += 1
        # Вызываем оригинальный метод __init__ для инициализации экземпляра
        instance.__init__(*args, **kwargs)
        # Возвращаем созданный экземпляр класса
        return instance

    # Заменяем оригинальный конструктор класса на функцию-обертку
    cls.__new__ = wrapper

    # Метод класса для получения количества созданных экземпляров
    @classmethod
    def get_created_instances(cls):
        # Возвращаем значение счетчика экземпляров класса
        return cls.__instances_count

    # Добавляем метод get_created_instances в класс
    cls.get_created_instances = get_created_instances

    # Метод класса для сброса счетчика экземпляров
    @classmethod
    def reset_instances_counter(cls):
        # Получаем текущее значение счетчика экземпляров
        count = cls.__instances_count
        # Сбрасываем счетчик экземпляров, устанавливая его в значение 0
        cls.__instances_count = 0
        # Возвращаем значение счетчика до сброса
        return count

    # Добавляем метод reset_instances_counter в класс
    cls.reset_instances_counter = reset_instances_counter

    # Возвращаем измененный класс
    return cls


@instances_counter
class User:
    pass


if __name__ == '__main__':
    # Проверяем, что вначале количество созданных экземпляров равно 0
    User.get_created_instances()  # 0

    # Создаем несколько экземпляров класса User
    user1, user2, user3 = User(), User(), User()

    # Проверяем, что количество созданных экземпляров стало равно 3
    User.get_created_instances()  # 3

    # Сбрасываем счетчик экземпляров и получаем значение до сброса
    user1.reset_instances_counter()  # 3

