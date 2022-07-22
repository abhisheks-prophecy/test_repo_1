from setuptools import setup, find_packages

setup(
    name='py_gitPeruserfork',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='py_gitPeruserfork',
    install_requires=[
        'prophecy-libs==1.1.11'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    extras_require={
        'test': ['pytest', 'pytest-html'],
    }
)
