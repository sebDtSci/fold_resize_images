from setuptools import setup, find_packages

setup(
    name="fold_resize_images",
    version='{{VERSION_PLACEHOLDER}}',
    description="A simple tool to resize images in a directory.",
    author="Tadiello Sébastien",
    author_email="sebastientadiello@gmail.com",
    homepage="https://github.com/sebastientadiello/fold-resize-images",
    # license="MIT License",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        "Pillow"
    ],
    entry_points={
        'console_scripts': [
            'fold-resize-images=src.fold_resize_images:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
