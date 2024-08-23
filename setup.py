import json
import os.path
from setuptools import find_packages, setup

dirname = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(dirname, 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(dirname, 'options.json')) as f:
    options = json.load(f)

with open(os.path.join(dirname, 'requirements.txt')) as f:
    install_requires = f.readlines()

with open(os.path.join(dirname, 'test-requirements.txt')) as f:
    test_requires = f.readlines()

with open(os.path.join(dirname, 'release-requirements.txt')) as f:
    release_requires = f.readlines()

setup(name=options['projectName'],
      version=options['packageVersion'],
      description="SensorPush Public API",
      long_description=long_description,
      long_description_content_type='text/markdown',
      author_email="support@sensorpush.com",
      url="https://www.sensorpush.com/gateway-cloud-api",
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: Other/Proprietary License',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      license='SensorPush License',
      keywords=["Swagger", "SensorPush Public API"],
      install_requires=install_requires,
      extras_require={
          'test': test_requires,
          'release': release_requires
      })
