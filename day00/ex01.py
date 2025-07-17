import time
from time import gmtime, strftime
from datetime import datetime

seconds = time.time()
print("second since january 1 , 1970: ", seconds ," or ",f"{seconds:.3e}  in a scientific notation", )
print(time.ctime(seconds))