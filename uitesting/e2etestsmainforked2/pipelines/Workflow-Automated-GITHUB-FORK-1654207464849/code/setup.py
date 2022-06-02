from setuptools import setup, find_packages

setup(
    name='Workflow-Automated-GITHUB-FORK-1654207464849',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='Workflow-Automated-GITHUB-FORK-1654207464849',
    install_requires=[
        'pyhocon==0.3.59',
        'prophecy-libs==1.0.2'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    tests_require=['pytest', 'pytest-html']
)
