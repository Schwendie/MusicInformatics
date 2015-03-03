# Problem
We would like to be able to let people's Tweets influence a playlist.

# Question
1. How do we grab live Tweets from Twitter in python?

# Resources
1. [TwitterSearch]

### Mini-abstract and relevance of [TwitterSearch]
[TwitterSearch] is a Python-based interface to Twitter's 1.1 Search API.  Once a user has obtained a consumer key, consumer secret, access token, and access token secret from [twitter developers], then they can get information by searching Twitter.  This can be information on a user, such as all their Tweets, or Tweets on all of Twitter containing a kewyword or keywords, to name a few.
The module TwitterSearch must be installed to your version of Python (the [github] for TwitterSearch) and imported at the start of the program.
```python
from TwitterSearch import *
```
This module provides an easy way to retrieve live Tweets straight from Twitter.

[TwitterSearch]: https://twittersearch.readthedocs.org/en/latest/index.html
[twitter developers]: https://dev.twitter.com/
[github]: https://github.com/ckoepp/TwitterSearch
