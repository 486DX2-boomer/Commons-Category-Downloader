# Commons-Category-Downloader
## Download all images from a Category: page on Wikimedia Commons to current working directory

I wanted to download all images from a category page on Wikimedia Commons, but I didn't want to manually right click and save over 100 images. This very simple Python script will do the job handily.

## Usage

The script accepts one argument, which is the URL of the category page you want to download images from. For example, https://commons.wikimedia.org/wiki/Category:Costumes_of_All_Nations_(1882) or https://commons.wikimedia.org/wiki/Category:Quality_images_of_sculptures_in_Berlin

It won't work on anything else, and it does not accept multiple arguments.

**This script always downloads to the current working directory.**

### Dependencies
You'll need [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) and [html5lib](https://pypi.org/project/html5lib/).

### To Do

* Support multiple arguments (that is, download multiple category pages sequentially)
* Support a command line argument to allow the user to download to any directory, instead of just CWD
