from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='__pip_name__',
      version='0.1',
      description='__pip_description__',
      long_description=long_description,
      long_description_content_type="text/markdown",
      scripts=['bin/__pip_name__'] ,
      url='__pip_url__',
      author='__author__',
      author_email='__author_email__',
      license='MIT',
      packages=setuptools.find_packages(),
      zip_safe=False,
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ],
      install_requires=[
            'coloredlogs'
      ])