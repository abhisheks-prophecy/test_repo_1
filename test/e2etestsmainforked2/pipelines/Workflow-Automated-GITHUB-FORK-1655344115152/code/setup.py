from setuptools import setup, find_packages

setup(
    name='Workflow-Automated-GITHUB-FORK-1655344115152',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='Workflow-Automated-GITHUB-FORK-1655344115152',
    install_requires=[
        'prophecy-libs==1.1.3'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    tests_require=['pytest', 'pytest-html']
)
