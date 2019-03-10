from setuptools import setup

setup(
	name='webotron-80',
	version='0.1',
	author='Vikas Durgale',
	author_email='vikas@example.com',
	description='Webotron 80 is a tool to deploy static websites to AWS.',
	license='GPLv3+',
	packages=['webotron'],
	url='https://github.com/VikasDurgale/automating-aws-with-python/tree/master/01-webotron',
	install_requires=[
		'boto3',
		'click'
	],
	entry_points='''
		[console_scripts]
		webotron=webotron.webotron:cli
	'''
)