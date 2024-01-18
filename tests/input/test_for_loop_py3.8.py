"""
test_for_loop_3.8.py -- source test
For-loops have changed in python 3.8. The test and PR
(https://github.com/zrax/pycdc/pull/270) add some support.
It also fixes a problem with nested if- and for blocks.

This source is part of the decompyle test suite.

decompyle is a Python byte-code decompiler
See http://www.goebel-consult.de/decompyle/ for download and
for further information
"""


print('block1')
for _ in 'foo':
    print('block2')
