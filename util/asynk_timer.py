import functools
import time
from typing import Callable, Any


def async_timed():
    def wrapper(
            func: Callable) -> Callable:  # Callable использует типизацию, чтобы указать, что принимает функцию и возвращает другую функцию
        @functools.wraps(func)
        async def wrapped(*args,
                          **kwargs) -> Any:  # Any - для указания на то, что функция может вернуть любое значение.
            print(f'выполняется {func}')
            start = time.time()
            try:
                return await func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')

        return wrapped

    return wrapper


def timed():
    def wrapper(
            func: Callable) -> Callable:  # Callable использует типизацию, чтобы указать, что принимает функцию и возвращает другую функцию
        @functools.wraps(func)
        def wrapped(*args,
                          **kwargs) -> Any:  # Any - для указания на то, что функция может вернуть любое значение.
            print(f'выполняется {func}')
            start = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                end = time.time()
                total = end - start
                print(f'{func} завершилась за {total:.4f} с')

        return wrapped

    return wrapper
