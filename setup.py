from setuptools import setup, find_packages

with open('README.rst', 'r') as open_file:
    readme = open_file.read()

setup(
        name='hr',
        version='0.1.0',
        description='CLI user management tool',
        long_description=readme,
        author='Micah Wong',
        author_email='mswong76@gmail.com',
        packages=find_packages('src'),
        package_dir={'':'src'},
        install_requires=[]
)
