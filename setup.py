from setuptools import setup

setup(
    name='django-to-native',
    version='0.0.1',
    packages=['django_to_native'],
    entry_points={
        'console_scripts': [
            'wrap=django_to_native.wrapper:wrap_desktop'
        ]
    },
)

