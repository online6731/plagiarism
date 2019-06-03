import urllib.request
from googlesearch import search
from inscriptis import get_text
from rake_nltk import Rake





# search and get first url from google
def get_url(term):
    url = ""
    for i in search(term, stop=1):
        url = i
    return url

# find keyword from lists of terms
def find_keyword(terms):
    r = Rake(min_length = 1 , max_length = 2)
    r.extract_keywords_from_text(terms)
    result = r.get_ranked_phrases()
    return result

# this function finds web page and fetches and
# writes its content in a file
def fetch_result(term):
    url = get_url(term) 
    html = urllib.request.urlopen(url).read().decode('utf-8')
    text = get_text(html)
    with open("result_of_search.txt" , "w") as f:
        f.write(text)
    return url



def lcs(X, Y, m, n): 
    L = [[0 for x in range(n+1)] for x in range(m+1)] 
    index = L[m][n] 
    lcs = ""  
    i = m 
    j = n   

    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0: 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1] + 1
            else: 
                L[i][j] = max(L[i-1][j], L[i][j-1]) 
  
    while i > 0 and j > 0: 
        if X[i-1] == Y[j-1]: 
            lcs += X[i-1]
            i-=1
            j-=1
        elif L[i-1][j] > L[i][j-1]: 
            i-=1
        else: 
            j-=1
    lcs = lcs[::-1]
    return lcs



def read_file(f):
    string = ""
    for i in f:
        string += i
    return string


def main():

    with open("str.txt" , "r") as f1:
        str1 = read_file(f1)
        keyword = find_keyword(str1)
        word = keyword[0]
        print("key: ",word)
        url = fetch_result(word)
        print("url: ",url)

        with open("result_of_search.txt", "r") as f2:
            str2 = read_file(f2)
            l1 = len(str1)
            l2 = len(str2)

            result = lcs(str1, str2, l1, l2)
            # prints the result of the lcs
            print(result)   



if __name__ == '__main__':
    main()
