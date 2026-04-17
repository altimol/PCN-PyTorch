from setuptools import setup, find_packages

setup(
    name="pcn_pytorch",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "pcn_pytorch ": [
            "*.cu",
            "*.cpp",
            "*.h",
            "*.cuh",
            "*.sh",
            "*.txt",
            "*.yaml",
            "*.pth",
            "**/*.cu",
            "**/*.cpp",
            "**/*.h",
            "**/*.cuh",
            "**/*.sh",
            "**/*.txt",
            "**/*.yaml",
            "**/*.pth",
        ]
    },
)
