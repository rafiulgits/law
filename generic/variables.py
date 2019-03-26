LOGIN_URL = '/account/login/'
FILE_CHUNK_SIZE = 2500000
PRODUCTS_FILE_PATH = 'media/product'
USER_THUMBNAIL_PATH = 'mediauser'


REACT_GOOD_POINT = 4

MAX_TRENDING_SPACE = 10
MIN_RATE_FOR_SPACE_TRENDING = 5

from time import time
def now_str(mul=1):
	return str(int(time()*(10**mul)))


from uuid import uuid4
from hashlib import md5
def random():
	return str(md5(now_str(2).encode()+uuid4().hex.encode()).hexdigest())
