from distutils.core import setup, Extension

module1 = Extension('myasync',
                    sources = ['myasyncmodule.c', 'threadedcode2.c'],
                    )

setup (name = 'TestAsync',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
