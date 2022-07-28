from setuptools import setup, find_packages
setup(
    name = 'Workflow-Automated-GITHUB-FORK-1659031644337',
    version = '1.0',
    packages = find_packages(include = ('workflowautomatedgithubfork*', )),
    description = 'workflow',
    install_requires = [
'prophecy-libs==1.1.14'],
    entry_points = {
'console_scripts' : [
'main = workflowautomatedgithubfork.pipeline:main', ], },
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
