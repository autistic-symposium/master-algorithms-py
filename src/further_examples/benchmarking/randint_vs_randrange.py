# #!/usr/bin/python3

# Bernardo Sulzbach @ 2014
# github.com/mafagafo
# mafagafogigante@gmail.com


from timeit import timeit
randint = timeit('[random.randint(0, 99) for i in range(10)]', setup='import random', number=10000)
randrange = timeit('[random.randrange(100) for i in range(10)]', setup='import random', number=10000)
print('randint:\t', randint, '\n', 'randrange:\t', randrange, sep='')
if randint > randrange:
    print("random.randrange is faster.")
else:
    print("random.randint is faster.")
