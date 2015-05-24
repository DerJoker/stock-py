import os

debug = True
debug = False

'''
Configuration
'''

_fn_container = 'container'
_f_stocks_txt = 'stocks.txt'

# path
_path = os.path.abspath('.')
if (debug): print _path

# path container
_path_container = os.path.join(_path, _fn_container)
if (debug): print _path_container

# path stocks.txt
_path_stocks_txt = os.path.join(_path_container, _f_stocks_txt)
if (debug): print _path_stocks_txt