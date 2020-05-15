import os
from setuptools import setup, find_packages


path = os.path.dirname(os.path.realpath(__file__))


entry_points = {}

setup(
    name='grafana-plugin-sdk',
    description='Grafana plugin SDK',
    author='Justin Hunthrop',
    author_email='justin.hunthrop@grafana.com',
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    version='0.0.1',
    install_requires=[
        'bump2version',
        'pandas >= 1.0.3',
        'pyarrow >= 0.17.0'
    ],
    entry_points=entry_points
)
