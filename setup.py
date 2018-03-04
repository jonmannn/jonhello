from setuptools import setup

setup ( name='jonhello',
       version='0.1',
       description='This module greets the user.  ',
       url='',                # usually a github URL
       author='Jon Mann',
       author_email='jonmannn@gmail.com',
       license='MIT',
       packages=['jonhello'],
       install_requires=[ ],
       zip_safe=False,
       test_suite='pytest',
        setup_requires = ['pytest-runner'],
        tests_require = ['pytest']
        )