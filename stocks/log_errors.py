import sys
import traceback

def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            # Execute the function
            return func(*args, **kwargs)

        except FileNotFoundError as fnf_error:
            # Open the log.txt file in append mode
            with open('log.txt', 'a') as f:
                # Log the error message to the file
                traceback.print_exc(file=f)
            # Re-raise the exception to propagate it further
            raise

        except Exception as e:
            # Open the log.txt file in append mode
            with open('log.txt', 'a') as f:
                # Log the error message to the file
                traceback.print_exc(file=f)
            # Re-raise the exception to propagate it further
            raise

    return wrapper

