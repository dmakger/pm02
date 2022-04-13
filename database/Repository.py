def safe_call(func_to_decorator):
    def wrapper(self, data):
        try:
            return func_to_decorator(self, data)
        except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL:", _ex)

    return wrapper


class Repository:

    def __init__(self, datasource):
        self.datasource = datasource

    # def get_education_quality(self, ):
