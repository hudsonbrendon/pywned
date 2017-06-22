from setuptools import setup, find_packages


setup(name='ppwned',
      version='0.2.1',
      description='Check if you have an account that'
      'has been compromised in a data breach',
      url='https://github.com/hudsonbrendon/pwned',
      author='Hudson Brendon',
      author_email='contato.hudsonbrendon@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['tests*']),
      install_requires=[
          'requests',
      ],
      entry_points={'console_scripts': ['pwned = pwned:main']},
      zip_safe=False)
