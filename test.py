import pysikuli_img as sikuli
import time
import base64

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
    #
    #with open("./test_data/screen.png", "rb") as image_file:
    #    encoded_string = base64.b64encode(image_file.read())
    #
    #finder = sikuli.Finder(encoded_string, len(encoded_string))
    finder = sikuli.Finder("./test_data/screen.png")
    finder.find("./test_data/gmail.png", 0.9)

    if finder.has_next():
        result = finder.next()
        print(result.x, result.y, result.w, result.h)

test_find()

