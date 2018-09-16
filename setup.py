import codecs
from setuptools import setup

VERSION = '0.1.0.dev13'

setup(
    name='fragmuffin_pypitest',
    version=VERSION,
    url='https://github.com/fragmuffin/pypi-test',
    license='MIT',
    author='Peter Boin',
    author_email='peter.boin@gmail.com',
    description='Test package',
    long_description=codecs.open('README.rst', 'rb', 'UTF-8').read(),
    packages=['fragmuffin_pypitest'],
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ]
)
