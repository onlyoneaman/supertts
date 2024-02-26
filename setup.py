from setuptools import setup, find_packages

setup(
    name='supertts',
    version='0.0.1',
    author='Aman Kumar',
    author_email='2000.aman.sinha@gmail.com',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    extras_require={
        'openai': ['openai'],
    },
    description='A super TTS package supporting multiple providers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
