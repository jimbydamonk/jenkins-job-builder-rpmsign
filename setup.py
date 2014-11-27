import os
from setuptools import setup,find_packages
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "jenkins-job-builder-rpmsign",
    version = "0.0.4",
    author = "Mike Buzzetti",
    author_email = "mike.buzzetti@gmail.com",
    description = ("Jenkins-job-builder that adds support for Jenkins RPMSign plugin"),
    license = "OSI",
    keywords = "jenkins, plugin",
    url = "http://github.com/jimbydamonk/jenkins-job-builder-rpmsign",
    packages=find_packages(),
    long_description=read('README.md'),
    install_requires=["jenkins-job-builder>=0.6.0"],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python'
    ],
    entry_points={
        'jenkins_jobs.publishers': [
            'rpmsign=rpmsign:rpmsign',
        ],
    }
)
