#!/usr/bin/env python


__author__ = "Mari Wahl"
__email__ = "marina.w4hl@gmail.com"


""" an example of using pickle for importing data from files """


import pickle

def import_pickle(filename):
    fh = None
    try:
        fh = open(filename, "rb")
        mydict2 = pickle.load(fh)
        return mydict2

    except (EnvironmentError) as err:
        print ("{0}: import error: {0}".format(os.path.basename(sys.arg[0]), err))
        return false

    finally:
        if fh is not None:
            fh.close()


def test_import_pickle():
    pkl_file = 'test.dat'
    mydict = import_pickle(pkl_file)
    print(mydict)


if __name__ == '__main__':
    test_import_pickle()
