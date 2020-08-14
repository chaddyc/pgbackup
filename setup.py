from setuptools import find_packages, setup

with open('README.d', 'r') as f:
    long_description =f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Chad Crouch',
    author_email='crouch0013@gmail.com',
    description='A utility for backing up PostgreSQL databases',
    long_description=long_description,
    long_description_content_type'text/markdown',
    url='https://github.com/chaddyc/pgbackup',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.sli:main'
        ],
    }
)