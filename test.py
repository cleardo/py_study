__author__ = 'Administrator'

import io
import cof.file

# error
print cof.file.expand_links('./test.py')

print cof.file.expand_links('test.py')
print cof.file.expand_links('E:/temp/test.py')
print cof.file.expand_links('E:\\temp\\test.py')


print cof.file.get_app_loc()

print "hello"
