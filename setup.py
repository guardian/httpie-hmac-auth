from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='httpie-hmac-auth',
    description='HMAC Auth plugin for HTTPie.',
    long_description=open('README.rst').read().strip(),
    version='0.2.3',
    author='Nick Satterly',
    author_email='nick.satterly@theguardian.com',
    license='MIT',
    url='https://github.com/guardian/httpie-hmac-auth',
    download_url='https://github.com/guardian/httpie-hmac-auth',
    py_modules=['httpie_hmac_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_hmac_auth = httpie_hmac_auth:HmacAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
