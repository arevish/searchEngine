# Search Engine ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Program take a query string as an input from the user and pull out the sentences matching in the listor file and give the results for most relevant sentence is the one with the maximum number of matching words with the query. and tells how many similar titles it have founded, in how much time .

#### Example
```
search here : python

Out of( 4 searches) Result found!
 Result found in 5.192508697509766 miliseconds
 "python tutes": maches with 1
 "python intermediate": maches with 1
 "python for absolute bigners": maches with 1
 "python flask ": maches with 1

```
## Customization
Want to specify your own list of words ? Simply overwrite that list or make a  with a file with your list of titles in it and you can inport that file to in the program. Compound words with spaces involved work, too (eg., ice cream).

You can also add new words onto the included list to be used in the search. Words can be added at any place in the file or list .

### Module used
python modules
```
import time
```

## PRE-REQUISITES
Your laptop with 3.7.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/searchEngine.git
2. In source folder, run `python3 'searchengine.py'` to start program, optionally, run with `--help` argument to see other runtime options.

### ThankYou!