"""
update-github-clone
----

A small Flask application to keep a github clone up to date.

If you have a clone of a github repo on some remote server somewhere, you
can keep that cloned repo up to date by using this app and github's webhook
API.

"""
from setuptools import setup


setup(
    name='update-github-clone',
    version='0.1',
    url='https://github.com/drivet/update-github-clone/',
    license='MIT',
    author='Desmond Rivet',
    author_email='desmond.rivet@gmail.com',
    description='A small Flask application to keep a github clone up to date.',
    long_description=__doc__,
    py_modules=['update-github-clone'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Software Development :: Version Control',
    ],
)
