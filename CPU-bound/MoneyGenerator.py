from hashlib import md5
from random import choice
import concurrent.futures


def find_token():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)
            break


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=61):
        find_token()


if __name__ == '__main__':
    main()
