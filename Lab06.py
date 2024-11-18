import phantom_tollbooth
#Function to return new list of words minus the unwanted ones
def filter_words(words, unwanted_words):
        #Filters out unwanted words from a list of words
        return list(filter(lambda words: words not in unwanted_words, words))

def main():
    #Open book,convert to Lowercase, remove all returns, double quotes, comas, and periods then split book on spaces 
    book = phantom_tollbooth.get_text().lower().replace(chr(34), "").replace("\n", "").replace(",","").replace(".","").split(" ")
    #Create list of unwanted words
    unwanted_words = { "the", "is", "a", "it", "of", "and", "in", "to", "by", "an", "on", "for", "with", 
            "as", "at", "this", "he", "she", "they", "them", "his", "her", "their", "i", "you", 
            "we", "us", "me", "my", "our", "like", "oh", "but", "so", "or", "and", "if", 
            "then", "because", "that", "which", "who", "whom", "be","was", "be", "were", "be", 
            "him", "way", "would", "where", "been", "that", "why", "well", "out","should", "could",
            "your", "into", "all", "had", "from", "up",} 

    #Call the filtered book command
    filtered_book = filter_words(book, unwanted_words)  
    #Create an empty dictionary  
    thisdict = {}
    #Populate the dictionary with works and value of how many times they happen
    for item in filtered_book: 
        if item != "": thisdict[item.strip()] = filtered_book.count(item.strip())
    #Sort the dictionary on the value from least to most used  
    sorted_by_values = dict(sorted(thisdict.items(), key=lambda item: item[1]))
    #Find the total amount of words
    Total_keys = len(sorted_by_values)
    #Remove 50 from total amount so you know when to start populating results
    Start_Key  = Total_keys - 50
    #Set varible to 0 to count current word
    Row = 0
    #list off last 50 words in the dictionary
    for item in sorted_by_values:
        Row = Row + 1  
        if Row >= Start_Key:print(str(item) + " " + str(sorted_by_values.get(item)))
if __name__ == '__main__':
    main()