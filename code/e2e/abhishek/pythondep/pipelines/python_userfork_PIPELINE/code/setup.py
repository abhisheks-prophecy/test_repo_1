from setuptools import setup, find_packages
setup(
    name = 'python_userfork_PIPELINE',
    version = '1.0',
    packages = find_packages(include = ('job*', )),
    description = 'workflow',
    install_requires = ['matplotlib==3.5.2', 'pandas>=1.4.2', 'numpy==1.22.*', 'requests~=2.28.0', 'torch==1.11.0', 'prophecy-libs==1.1.1'],
    entry_points = {
'console_scripts' : [
'main = job.pipeline:main', ], },
    tests_require = ['pytest', 'pytest-html', 'pytest-cov']
)
