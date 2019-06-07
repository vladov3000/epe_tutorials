from mileage import convert_mileage
from nose.tools import *

assert_equal (convert_mileage(20),11.76)
assert_equal (convert_mileage(40),5.88)
