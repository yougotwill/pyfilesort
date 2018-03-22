from setuptools import setup
setup(
    name="pyfilesort",
    version="0.1",
    url="http://github.com/yougotwill/pyfilesort",
    author="William Grant",
    author_email="grnwil006@myuct.ac.za",
    packages=['pyfilesort'],
    install_requires=[
        'torrentool',
        'click',
    ],
    license='MIT',
    long_description=open('README.md').read(),
    keywords='python file clean cleanup downloads desktop clutter files sort',
    zip_safe=False
)
