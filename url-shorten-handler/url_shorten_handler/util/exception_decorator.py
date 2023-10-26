import traceback


def exception_traceback(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print("Exception occurred!")
            print(traceback.format_exc())  # Print full stack trace
            raise  # Re-raise the exception

    return wrapper
