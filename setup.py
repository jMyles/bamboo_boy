from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import os


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.rst')
CHANGES = read('CHANGES.md')

setup(
    name = "Bamboo Boy",
    packages = find_packages(),
    version = "0.5",
    author = "Justin Myles Holmes",
    author_email = "justin@justinholmes.com",
    url = "https://github.com/jMyles/bamboo_boy",
    description = "Reuse python setup and teardown logic between tests, deployments, and development environments.",
    long_description = "\n\n".join([README, CHANGES]),
    tests_require=['pytest'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    extras_require={
        'testing': ['pytest'],
    },
    keywords = ["python", "django", "testing", "factory_boy"],
)
