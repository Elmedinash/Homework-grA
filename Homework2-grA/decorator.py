import time

def time_logger(func):   # decorator function
    def wrapper():
        start = time.time()        # start time
        
        func()                     # run the original function
        
        end = time.time()          # end time
        print("Execution time:", end - start)
    
    return wrapper

