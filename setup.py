try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name="cif-http-client",
    version="0.1",
    description="Client for the CIF HTTP API",
    long_description="",
    url="https://github.com/JustinAzoff/cif-http-client-python",
    license='MIT',
    classifiers=[
        "Topic :: System :: Networking",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
    ],
    keywords='CIF',
    author="Justin Azoff",
    author_email="justin.azoff@gmail.com",
    py_modules = ["cif_http_client"], 
    install_requires = [
        "requests>=2.0"
    ],
    entry_points = {
        'console_scripts': [
        ]
    },
)
