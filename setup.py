import setuptools


setuptools.setup(
    name='inherit',
    version='0.0.1',
    author='RimoChan',
    author_email='the@librian.net',
    description='inherit',
    long_description=open('readme.md', encoding='utf8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RimoChan/inherit',
    packages=[
        '继承法',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'jieba>=0.42.1',
    ],
)