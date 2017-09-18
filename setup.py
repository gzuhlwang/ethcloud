"""
 A cli tool too launch, manage and use ethereum client on the cloud
"""
from setuptools import find_packages, setup

dependencies = ['click', 'ansible', 'PyYaml', 'boto3']

setup(
    name='ethcloud',
    version='0.0.1',
    url='https://github.com/kgritesh/ethcloud',
    license='BSD',
    author='Ritesh Kadmawala',
    author_email='k.g.ritesh@gmail.com',
    description=' A cli tool too launch, manage and use ethereum client on the cloud',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'ethcloud = ethcloud.cli:main',
        ],
    },
    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
