from setuptools import setup, find_packages

__version__ = 0.1

requires = [
    'requests==2.4.3'
]

extras_require = {
    'test': [
        'nose',
        'coverage',
        'flake8',
        'mock',
    ]
}

setup(
    name='tinypng',
    version='0.1.0',
    description='A TinyPNG python client',
    url='http://github.com/kelvintaywl/tinypng',
    download_url='http://github.com/kelvintaywl/tinypng/tarball/{version}'.format(version=__version__),
    author='Kelvin Tay',
    author_email='kelvintaywl@gmail.com',
    keywords='image compression api',
    packages=find_packages(),
    include_package_date=True,
    zip_safe=False,
    test_suite='tinypng',
    install_requires=requires,
    extras_require=extras_require
)