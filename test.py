import pysikuli_img as sikuli
import time

def timeit(f):    
    def timed(*args, **kw):
        ts = time.time()
        result = f(*args, **kw)
        te = time.time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % (f.__name__, args, kw, te-ts))
        return result
    return timed

@timeit
def test_find():
    for i in range(0, 1000):
        finder = sikuli.Finder("./test_data/screen.png")
        finder.find("./test_data/gmail.png", 0.9)

test_find()

