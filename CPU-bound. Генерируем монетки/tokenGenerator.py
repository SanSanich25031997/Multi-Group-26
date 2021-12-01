from hashlib import md5
from random import choice
import concurrent.futures

with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
