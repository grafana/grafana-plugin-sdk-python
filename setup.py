from setuptools import setup, find_packages

entry_points = {}

setup(
    name='grafana-plugin-sdk',
    description='Grafana plugin SDK',
    author='Justin Hunthrop',
    author_email='justin.hunthrop@grafana.com',
    packages=find_packages(),
    package_data={},
    include_package_data=True,
    version='0.0.2',
    install_requires=[
        'bump2version',
        'pandas >= 1.0.3',
        'pyarrow >= 0.17.0'
    ],
    entry_points=entry_points
)
