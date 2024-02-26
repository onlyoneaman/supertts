from setuptools import setup, find_packages

setup(
    name='supertts',
    version='0.0.4',
    author='Aman Kumar',
    author_email='2000.aman.sinha@gmail.com',
    packages=find_packages(),
    install_requires=[
        'openai==1.12.0'
    ],
    description='A super TTS package supporting multiple providers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
)
