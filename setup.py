from setuptools import setup, find_packages

setup(
    name='conjure',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    license='LICENSE',
    description='An example Python package for creating keyboard macros.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        "pyautogui",
        # Add other dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)