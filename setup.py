import setuptools

with(open("README.md","r",encoding="utf-8")) as f:
    long_description = f.read()

__version__ ="0.0.0.0"
REPO_NAME = "https://github.com/AyushSonuu/IBSProject"
AUTHOR_USER_NAME = "Ayush"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sonuayush55@gamil.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer NLP Application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=REPO_NAME,
    packages=setuptools.find_packages(),
     
)