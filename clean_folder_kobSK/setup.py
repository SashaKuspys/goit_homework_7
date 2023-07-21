from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder_kobSK",
    version="0.0.3",
    description="organizes folders and files",
    author="Oleksandr Kuspys",
    author_email="sashakuspys@gmail.com",
    packages=find_namespace_packages(),
    entry_points={"console_scripts": ["clean_folder=clean_folder_kobSK.main:start"]},
)
