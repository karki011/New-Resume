import urllib
def read_text():
    quotes = open("/Users/subashkarki/Desktop/quote.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_cruse(contents_of_file)

def check_cruse(txt_to_check):
    connection = urllib.urlopen('http://wdylike.appspot.com/?q='+txt_to_check)
    output = connection.read()
    print(output)
    connection.close()

read_text()
