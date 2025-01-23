from time import time
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Автоматически логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки.
    """
    def my_decorator(function: Any) -> Any:

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                t_start = time()
                result = function(*args, **kwargs)
                t_stop = time()
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{function.__name__} ok, start: {t_start}, stop: {t_stop}" + '\n')
                else:
                    print(f"start: {t_start}")
                    print(result)
                    print(f"stop: {t_stop}")
            except Exception as e:
                t_stop = time()
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{function.__name__} error: {e} Inputs: {args}, {kwargs} "
                                   f"start: {t_start}, stop: {t_stop}")
                else:
                    print(f"{function.__name__} error: {e} Inputs: {args}, {kwargs} "
                          f"start: {t_start}, stop: {t_stop}")
                raise e

            return result

        return wrapper

    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
