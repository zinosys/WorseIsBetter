import json
import shit
import sys

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
def query_for_tag(query_key, query_tag, query_type=contains, transform=identity, loc=yelp_dataset_path):
    with open(yelp_dataset_path) as Data:
        query_data = []
        for line in Data:
            parsed_line = json.loads(line)
            if (query_key in parsed_line.keys() and query_type(query_tag, transform(parsed_line[query_key]))):
                query_data.append(parsed_line)
    
    return query_data

def main(*args):
    biz_id = sys.argv[1]
    reviews = query_for_tag("business_id", biz_id, equals)
    # now do interesting things with them!
    avgsent = 0
    count = 0
    avgsvc = 0
    avgfood = 0
    avgamb = 0
    for review in reviews:
        cursent = analyze_review_sentiment(review["text"])
        if cursent:
            avgsent += cursent
            count += 1

        foodidx = review["text"].find("food")
        foodstr = review["text"][foodidx - 2:foodidx + 2]
        food = analyze_review_sentiment(foodstr)
        if food:
            avgfood += food

        serviceidx = review["text"].find("service")
        servicestr = review["text"][serviceidx - 2:serviceidx + 2]
        service = analyze_review_sentiment(servicestr)
        if service:
            avgsvc += service

        ambianceidx = review["text"].find("surprise")
        ambiancestr = review["text"][ambianceidx - 2:ambianceidx + 2]
        ambiance = analyze_review_sentiment(ambiancestr)
        if ambiance:
            avgamb += ambiance

        
    avgfood /= count
    avgsvc /= count
    avgamb /= count
    avgsent /= count
    print("Food score: " + str(avgfood * 100))
    print("Service score: " + str(avgsvc * 100))
    print("Quality score: " + str(avgamb * 100))
    print("Average sentiment: " + str(avgsent * 100))
    print("Average enthusiasm per star: " + str((avgsent * 5 / 4.5) * 100))

    print("\nSuch analytics. Very D3. Wow.")

    shit.plot("Food", int(avgfood * 100), 10)
    shit.plot("service", int(avgsvc * 100), 10)
    shit.plot("Location", int(avgamb * 100), 10)
    shit.plot("Sentiment", int(avgsent * 100), 10)


if __name__ == '__main__':
    main()


# ID 1:   mQfT3JYu18HN22DVylcE7A
# ID 2:   tl9XIP5trlkcuSfTQqe5jg
