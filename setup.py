from setuptools import setup, find_packages

setup(
    name="jupyter-chatgpt-magics",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "openai",
        "ipython",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: IPython",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.6',
)
