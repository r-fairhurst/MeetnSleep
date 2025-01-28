# Yippee i love python
from tqdm import tqdm
import time

# Example of a progress bar we could use for a cool backend something
# Number of total percent
def progressBar(func):
    for i in tqdm (range (100), 
                desc="Loading…", 
                ascii=False, ncols=75):
        func()
        
    print("Complete.")

def example():
    time.sleep(0.01)

def main():
    print("Minute Meet Backend")
    progressBar(example)

main()