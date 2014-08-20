#!/usr/bin/python3
# mari von steinkirch @2013
# steinkirch at gmail

import pickle

def export_pickle(data, filename='test.dat', compress=False):
    """ simple example of how to use pickle to export files """
    fh = None
    try:
        if compress:
            fh = gzip.open(filename, "wb") # write binary
        else:
            fh = open(filename, "wb") # compact binary pickle format	
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)	
			
    except(EnvironmentError, pickle.PickingError) as err:
        print("{0}: export error: {1}".format(os.path.basename(sys.argv[0], err)))
        return False
    
    finally:
        if fh is not None:
            fh.close()
            

def test_export_pickle():
    mydict = {'a': 1, 'b': 2, 'c': 3}
    export_pickle(mydict)

         
            
if __name__ == '__main__':
    test_export_pickle()
