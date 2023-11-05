# API - Advanced
 
This directory, the Reddit API will be used to perform various tasks with the goal of:
   
* How to reading API documentation to find the endpoints you're looking for
* How to using an API with pagination
* How to parsing JSON results from an API
* How to making a recursive API call
* How to sorting a dictionary by value
  
## Directory Files
* [0-subs.py](0-subs.py) - a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.
* [1-top_ten.py](1-top_ten.py) - a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit. 
* [2-recurse.py](2-recurse.py) - a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None
* [100-count.py](100-count.py) -a recursive function that queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords (case-insensitive, delimited by spaces. Javascript should count as javascript, but java should not).
* [tests](tests) - contains the main test files

