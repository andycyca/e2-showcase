# E2 stats utility

2021-07-25: A utility to extract and format data from writeups on everything2

## Motivation

Since there's no good, easy way to extract *extensive* writeup data from e2, I decided to create my own. Maybe there's a better way for those who know perl, too bad!

## Prerequisites

- A text editor
- A modern web browser
- Ability to read and extract information from written words
- Working knowledge of the English language, particularly in its written form. 
- Python 3.x (you can [download it for free])
- Water to stay hydrated

## Getting the data

1. Log in. **This is crucial** because you get more information when logged in and this utility assumes you will extract data only available to you.
2. Perform a user search with the following URL:

   `https://everything2.com/node/superdoc/Everything+User+Search?perpage=500?node_id=1223826&usersearch=andycyca&orderby=node.reputation+ASC&submit=submit`

   ...but please note that you should use your own username in the part that says `usersearch=`. Also, this url only returns 500 writeups per page. I don't know the technical limitations of the database, but I wouldn't push it too far. Also, it's sorted by reputation ascending for a reason.
3. Copy **all** of the table, starting with the header "C!s" and ending with the last publish date of the last writeup on the page.
4. Paste everything **on a text editor, not a word processor**. This is because the utility will try to find some special characters (`\t`) to align and split the data. Then erase the header lines (there should be 2, I think)
5. If you have more than 500 writeups, go to the next page and repeat steps 3-4 until you have a list of all your writeups.
6. Save this file as `e2stats.csv` with utf-8 encoding. If you don't know how to do this, you can save it as `e2stats.txt` with whatever encoding, but you'll need to update the python script to reflect these changes. [If you're not smart enough to figure this out on your own, you shouldn't be doing it].
7. Save the `e2stats.py` to the same folder where the previous file is.
8. Run `e2stats.py`. Only tested with Python 3.something, but requires nothing more than `re`.
9. If it finishes without errors, you should now have two more files: `e2stats_preprocessing.csv` and `e2stats_final.csv`. Feel free to delete the former.
10. ???
11. Profit!? Now you have a nicely formatted file that you can play around with, even in (ew) Excel (EWWWWW)

More thorough analysis and discussion to come, but that will require you to also install other Python tools, namely numpy, matplotlib and pandas (also known as the infamous trinity of all data science in Python, so you should have these anyway)

[download it for free]: https://www.python.org/downloads/

[If you're not smart enough to figure this out on your own, you shouldn't be doing it]: https://everything2.com/title/If+you%2527re+not+smart+enough+to+figure+this+out+on+your+own%252C+you+shouldn%2527t+be+doing+it
