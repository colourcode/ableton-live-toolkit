from setuptools import setup
from ableton import __version__

setup(
    name='ableton',
    version=__version__,
    author='Colour Code',
    author_email='colour-code@live.com',
    description='Ableton Live Toolkit',
    long_description=open('Readme.rst').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    packages=["ableton"],
    scripts=["bin/ableton-tool"],
    install_requires=open('requirements.txt').readlines()
)
