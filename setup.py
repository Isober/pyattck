from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

setup(
    name='pyattck',
    version='3.0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package to interact with the Mitre ATT&CK Frameworks',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['att&ck', 'mitre', 'swimlane'],
    url='https://github.com/swimlane/pyattck',
    author='Swimlane',
    author_email='info@swimlane.com',
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*,!=3.3.*, !=3.4.*, !=3.5, <4',
    package_data={
        'pyattck':  ['data/actors/*.png']
    },
    entry_points={
          'console_scripts': [
              'pyattck = pyattck.__main__:main'
          ]
    },
)
