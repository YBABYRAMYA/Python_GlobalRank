# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
class HTMLParser1(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]
        
html = '\n'.join([input() for _ in range(int(input()))])
parser = HTMLParser1()
parser.feed(html)
parser.close()
