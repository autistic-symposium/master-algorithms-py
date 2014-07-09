import sys
print("System version:", sys.version, '\n')

try:
    import numpy
    print("\nNumpy version:", numpy.__version__)
except ImportError as e:
    print(e)

try:
    import matplotlib
    print("\nMatplotlib version:", matplotlib.__version__)
except ImportError as e:
    print(e)

try:
    import pandas
    print("\nPandas version:", pandas.__version__)
except ImportError as e:
    print(e)
