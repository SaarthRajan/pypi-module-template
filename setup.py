from setuptools import setup, find_packages

setup(
    name='package_name',
    version='0.0.1',    
    description='short description',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/user/repository',
    author='Author_Name',
    author_email='name@example.com',
    license='MIT',
    packages=find_packages(),  # Automatically discover packages
    keywords=['Python'],
    install_requires=[
        "opencv-python>=4.0.0,<5.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
