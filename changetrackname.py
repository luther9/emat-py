#!/usr/bin/env python3

import pickle
import sys

# To ensure we can safely unpickle and repickle, we need to import the relevent
# data type exactly as it is in emat.
from datetime import date as Date


def main(argv):
    filename = argv[0] + '.emat'
    oldName, newName = argv[1:]
    try:
        with open(filename, 'rb') as f:
            db = pickle.load(f)
    except FileNotFoundError:
        print(f'File {filename} not found')
        return 1
    with open(filename, 'wb') as f:
        pickle.dump(
            dict(
                {k: v for k, v in db.items() if k != oldName},
                **{newName: db[oldName]},
            ),
            f,
        )


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
