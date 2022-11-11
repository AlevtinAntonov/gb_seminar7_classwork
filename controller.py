# User interface, соединяет пользователя, фронт и бэк

import view
import model


def run():
    while True:
        input('Вычитаем, введите А: ', a)
        input('Вычитаем, введите Б: ', b)
        result = model.divide(a, b)
        view.show(a, b, result)
        logger.calculation_logger(a, b, result)
