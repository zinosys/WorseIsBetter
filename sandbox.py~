import json

def load_sentiments():
    word_sentiments = {}
    for line in open('sentiment_data/sentiments.csv', encoding='utf8'):
        word, score = line.split(',')
        word_sentiments[word] = float(score.strip())
    return word_sentiments
    
word_sentiments = load_sentiments()

def get_word_sentiment(word):
    """Return a sentiment representing the degree of positive or negative
    feeling in the given word.
    """
    # Learn more: http://docs.python.org/3/library/stdtypes.html#dict.get
    return word_sentiments.get(word)

def extract_words(text):
    """Return the words in a tweet, not including punctuation.

    >>> extract_words('anything else.....not my job')
    ['anything', 'else', 'not', 'my', 'job']
    >>> extract_words('i love my job. #winning')
    ['i', 'love', 'my', 'job', 'winning']
    >>> extract_words('make justin # 1 by tweeting #vma #justinbieber :)')
    ['make', 'justin', 'by', 'tweeting', 'vma', 'justinbieber']
    >>> extract_words("paperclips! they're so awesome, cool, & useful!")
    ['paperclips', 'they', 're', 'so', 'awesome', 'cool', 'useful']
    >>> extract_words('@(cat$.on^#$my&@keyboard***@#*')
    ['cat', 'on', 'my', 'keyboard']
    """
    list_words = ''
    for char in text:
        if not char.isalpha():
            char = ' '
        list_words += char
    return list_words.split()

def analyze_review_sentiment(text):
    """ Return a sentiment representing the degree of positive or negative
    sentiment in the given review, averaging over all the words in the review
    that have a sentiment value.

    If no words in the review have a sentiment value, return None.
    """
    # You may change any of the lines below.
    word_list = extract_words(text)
    sentiment_list = []
    for word in word_list:
        word_sentiment = get_word_sentiment(word)
        if word_sentiment:
            sentiment_list.append(word_sentiment)
    
    list_length = len(sentiment_list)
    if list_length == 0:
        return None # No numerical sentiments.
    
    average = sum(sentiment_list)
    return average / list_length

yelp_dataset_path = 'yelp_data/yelp_academic_dataset_review.json'

contains = lambda x, y: x in y
equals = lambda x, y: x == y
identity = lambda x: x
lowercase = lambda x: x.lower()
def query_for_tag(query_key, query_tag, query_type=contains, transform=identity):
    with open(yelp_dataset_path) as Data:
        query_data = []
        for line in Data:
            parsed_line = json.loads(line)
            if (query_key in parsed_line.keys() and query_type(query_tag, transform(parsed_line[query_key]))):
                query_data.append(parsed_line)
    
    return query_data

def main():
    print(analyze_review_sentiment("love like"))
    reviews = query_for_tag("business_id", "mQfT3JYu18HN22DVylcE7A", equals)
    # now do interesting things with them!
    avgsent = 0
    count = 0
    for review in reviews:
        cursent = analyze_review_sentiment(review["text"])
        if cursent:
            print("Review sentiment: " + str(cursent))
            avgsent += cursent
            count += 1
        else:
            print("No sentiment for this review.")
    
    print("Average sentiment: " + str(avgsent))


if __name__ == '__main__':
    main()
