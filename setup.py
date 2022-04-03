#!/usr/bin/env python3

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from pathlib import Path

here = Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="certifier",
    version="0.0.1",
    description="a certificate authority to simplify certificate signing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/amountainram/certifier_py.git",
    author="Umberto Toniolo",
    author_email="amountainram@gmail.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="certs,ca,development,security,https,tls",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3, <4",
    entry_points={
        "console_scripts": [
            "certifier=certifier:main",
        ],
    },
)

# from pathlib import Path
# from project_tws import ca
# from project_tws import arguments
# import yaml

# def init():
#     parsed_arguments = arguments.get_parser().parse_args()
#     try:
#         config = yaml.load(parsed_arguments.config, Loader=yaml.FullLoader)
#     except FileNotFoundError:
#         print("Cannot find a configuration file")
#         exit(1)

#     command = parsed_arguments.command
#     subcommand = parsed_arguments.subcommand

#     if(command == 'ca'):
#         ca.setup(parsed_arguments,config)
#         if(subcommand == 'remove'):
#             ca.remove()
#         if(subcommand == 'create'):
#             ca.create_ca()
#         elif(subcommand == 'sign'):
#             ca.sign_ca()

#     if parsed_arguments.remove:
#         ca.remove()

#     exit(0)

# if __name__ == "__main__":
#     init()