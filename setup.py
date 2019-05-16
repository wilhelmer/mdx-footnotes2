#! /usr/bin/env python


from setuptools import setup
setup(
    name='mdx-footnotes2',
    version='0.1.0',
    author='Lars Wilhelmer',
    author_email='lars@wilhelmer.de',
    description='The official Python markdown "footnotes" extension, with additional options.',
    url='https://github.com/wilhelmer/mdx-footnotes2',
    py_modules=['footnotes2'],
    install_requires=['Markdown>=2.0',],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)
