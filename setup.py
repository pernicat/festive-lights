from setuptools import setup

setup(name='festive-lights',
	version='0.1',
	description='Script that runs an LED RGB light strip from a raspberry PI',
	url='https://github.com/pernicat/festive-lights',
	author='Tony Pernicano',
	author_email='pernicat@gmail.com',
	license='GNU',
	packages=['festive-lights'],
	dependency_links=['https://github.com/jgarff/rpi_ws281x'])