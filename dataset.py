#!/bin/env python

if __name__ == '__main__':
    import sys
    import urllib.request

    name = sys.argv[1]
    urllib.request.urlretrieve(f"https://raw.githubusercontent.com/arpanganguli/ISLP/master/Data/{name}.csv", f"data/{name}.csv")
