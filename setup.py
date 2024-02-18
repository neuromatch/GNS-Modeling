from setuptools import find_packages, setup

setup(
    name='gns',
    packages=find_packages(),
    package_data={
        'gns': ['model_saves/*.pt'],
    },
    include_package_data=True,
)
