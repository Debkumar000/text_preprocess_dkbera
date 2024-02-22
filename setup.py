import setuptools

with open('README.md','r') as file:
	long_description=file.read()

setuptools.setup(
	name='text_preprocess_dkbera',
	version = '0.0.4',
	author = 'Debkumar Bera',
	author_email = 'debkumarbera150@gmail.com',
	description = 'This is text preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages=setuptools.find_packages(),
	classifiers = [
	'Programming Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating system :: OS Independent'],
	python_requires = '>=3.10'
	)