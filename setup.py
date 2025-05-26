from setuptools import setup, find_packages

setup(
    name='pytector',
    version='0.1.2',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    install_requires=[
        'transformers>=4.0.0',
        'validators',
        'torch',
        'groq'
    ],
    extras_require={
        'gguf': ['llama-cpp-python>=0.2.0'],
        'test': ['pytest>=8.0'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
    ],
    python_requires='>=3.9',
)
