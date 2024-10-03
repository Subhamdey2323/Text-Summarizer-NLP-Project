import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()


setuptools.setup(
    name="text-summerizer",
    version="0.0.0",
    author="Subham Dey",
    author_email="subhamdey2323@gmail.com",
    description="Text Summarizer app using NLP",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/Subhamdey2323/Text-Summarizer-NLP-Project",
    project_urls={
        "Bug Tracker":f"https://github.com/subhamdey2323/Text-Summarizer-NLP-Project",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)