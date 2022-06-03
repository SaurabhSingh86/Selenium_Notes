def wait(func):
    def wrapper(*args, **kwargs):
        instance = args[0]
        locator = args[1]
        wait = WebDriverWait(instance.driver, 10)
        v = _visibility_of_element_located(locator)
        wait.until(v)
        return func(*args, **kwargs)
    return wrapper


class Child:
    def _visibility_
