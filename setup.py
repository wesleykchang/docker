from setuptools import setup, find_packages

setup(
    name='docker',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyyaml'
    ],
    author='Gunnar Thorsteinsson',
    author_email='gunnar.thorsteinsson@example.com',
    description='Automatically generate docker-compose.yaml from a list of containers',
    url='https://github.com/steingartlab/docker',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)