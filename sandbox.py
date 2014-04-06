import json

def get_sentiment_data():
    word_sentiments = {}
    for line in open('sentiment_data/sentiments.csv', encoding='utf8'):
        word, score = line.split(',')
        word_sentiments[word] = float(score.strip())
    return word_sentiments
    
word_sentiments = get_sentiment_data()

yelp_dataset_path = 'yelp_data/yelp_academic_dataset_user.json'

contains = lambda x, y: x in y
equals = lambda x, y: x == y
def query_for_tag(query_key, query_tag, query_type=contains):
    with open(yelp_dataset_path) as Data:
        query_data = []
        for line in Data:
            parsed_line = json.loads(line)
            if (query_key in parsed_line.keys() and query_type(query_tag, parsed_line[query_key].lower())):
                query_data.append(parsed_line)
    
    return query_data

def main():
    print(query_for_tag("name", "eldon", contains))


if __name__ == '__main__':
    main()
