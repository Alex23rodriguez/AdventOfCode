from contextlib import contextmanager
from datetime import datetime


### timing funcs
@contextmanager
def timed():
    start_time = datetime.now()
    yield
    print(f"took {datetime.now() - start_time}")
