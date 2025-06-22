def count_retweets_by_username(tweet_list):
    """ (list of tweets) -> dict of {username: int}
    Returns a dictionary in which each key is a username that was 
    retweeted in tweet_list and each value is the total number of times this 
    username was retweeted.
    """
    
    if tweet_list is None:
        return
    
    #create a list to hold all usernames we find
    usernames = []
    for tweet in tweet_list:
        words = tweet.split()
        for i in range(len(words)):
            if words[i] == "RT":
                name = words[i + 1][1:-1]
                if len(name) > 1 and len(name) < 14:
                    usernames.append(name)
    #dictionary comprehension to count the users in usernames
    res = {user: usernames.count(user) for user in set(usernames)}

    return res


def display(deposits, top, bottom, left, right):
    """display a subgrid of the land, with rows starting at top and up to 
    but not including bottom, and columns starting at left and up to but
    not including right."""


    cols = right - left
    rows = bottom - top

    #intialize board
    board  = [['-' for _ in range(cols)] for _ in range(rows)]

    if deposits is None:
        return

    for i, j, _ in deposits:
        if left <= i < right and top <= j < bottom:
            y = j - top
            x = i - left
            board[x][y] = "X"

    lines = [" ".join(row) for row in board]
    return "\n".join(lines)



def tons_inside(deposits, top, bottom, left, right):
    """Returns the total number of tons of deposits for which the row is at least top,
    but strictly less than bottom, and the column is at least left, but strictly
    less than right."""
    # Do not alter the function header.  

    tons = 0

    if deposits is None:
        return

    for i, j, e in deposits:
        if left <= i < right and top <= j < bottom:
            tons += e
    return tons


def birthday_count(dates_list):
    """Returns the total number of birthday pairs in the dates_list"""
    freq = {}
    count = 0
    for date in dates_list:
        seen = freq.get(date, 0)
        count += seen
        freq[date] = seen + 1
 
    return count