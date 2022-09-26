This is a Python script to take arbitrary comment URLs from [Reddit](https://reddit.com) and output the comments into CSV files.

Please note that this program requires you to have a Reddit account and access to the Reddit API. It uses PRAW -- the Python Reddit API Wrapper, and instructions for setting up PRAW can be found [here](https://praw.readthedocs.io/en/stable/getting_started/quick_start.html). Once you have that set up, copy the file ```praw.ini.template``` to ```praw.ini```, and edit ```praw.ini``` with your ```client_id``` and ```client_secret```.

The dependencies in the project are handled by [Poetry](https://python-poetry.org/) -- make sure you have an up to date Python 3 and Poetry installed, and then ```poetry install``` to install the depencies. After that, merely put the URLs you want to scrape in ```url-list.csv``` -- be sure to follow the format of URLs separated by commas -- and then run ```poetry run python reddit-extract.py```. The output will be in files named ```file[number].csv``` -- e.g., the first url will be ```file1.csv```, the second ```file2.csv```, and so on.

