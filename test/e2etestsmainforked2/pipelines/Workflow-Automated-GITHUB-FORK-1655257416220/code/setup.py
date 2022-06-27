from setuptools import setup, find_packages

setup(
    name='Workflow-Automated-GITHUB-FORK-1655257416220',
    version='1.0',
    packages=find_packages(include=('job*',)),
    description='Workflow-Automated-GITHUB-FORK-1655257416220',
    install_requires=[
        'prophecy-libs==1.1.1'
    ],
    entry_points={
        'console_scripts': [
            'main = job.pipeline:main',
        ],
    },
    tests_require=['pytest', 'pytest-html']
)
