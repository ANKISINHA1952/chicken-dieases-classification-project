from setuptools 

with open("README.md", "r", encoding="utf-8") as f:
    long_description =f.read()

# ---------------- Constants ----------------
REPO_NAME = "chicken-dieases-classification-project"
AUTHOR_USER_NAME = "ANKISINHA1952"
SRC_REPO = "cnn_classifier"
AUTHOR_EMAIL = "ankitsinha1952@gmail.com"
__version__="0.0.0"


# ---------------- Setup ----------------
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)