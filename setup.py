from setuptools import setup

setup(
    name='wazpo',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'myscript=wazpo:wazpo'
        ]
    }
)
