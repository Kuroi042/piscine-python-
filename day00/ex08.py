from time import sleep
from tqdm import tqdm

import sys

import sys
from time import sleep

def ft_tqdm(lst: range) -> None:
    total = len(lst)
    for i , item in enumerate(lst):
        percent = int((i + 1) * 100 / total)
        bar_length = 30
        filled = int(bar_length * (i + 1) / total)
        bar = '█' * filled + '-' * (bar_length - filled)
        sys.stdout.write(f'\r[{bar}] {i ,"/",lst }%')
        sys.stdout.flush()
        yield item
        
        
for elem in ft_tqdm(range(333)):
    sleep(0.005)



print()

for elem in tqdm(range(333)):
    sleep(0.005)