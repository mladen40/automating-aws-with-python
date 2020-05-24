from setuptools import setup

setup(
    name='webotron-80',
    version='0.1',
    author='Mladen5280',
    author_email='mladen40@gmail.com',
    description='Webotron 80 is a tool to deploy static websites to AWS.',
    license='GPLv3+',
    packages=['webotron'],
    url='https://github.com/mladen40/automating-aws-with-python/tree/master/01-webotron',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        webotron=webotron.webotron:cli
    '''
)
