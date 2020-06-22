bool_deco = True


def decorator_factory(flag):
    def decorator(original_function):
        def wrapper(*args, **kwargs):
            if flag:
                import time
                st = time.time()
                result = original_function(*args, **kwargs)
                et = time.time()
                print(original_function.__name__," took :: ", int((et - st)),"seconds")
                return result
            else:
                return original_function(*args, **kwargs)

        return wrapper

    return decorator


@decorator_factory(bool_deco)
def sample_fun(input_name):
    print("your name is ", input_name)


@decorator_factory(bool_deco)
def heavy_function():
    import time
    print("Doing heavy processing")
    time.sleep(10)
    print("Done !!!")


sample_fun("TinguMan")
heavy_function()
