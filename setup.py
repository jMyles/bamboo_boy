from setuptools import setup, find_packages
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README = read('README.md')
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
    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
    keywords = ["python", "django", "testing", "factory_boy"],
)
