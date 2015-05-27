from interwiki.rules import StartsWithTranslator
import re


class Xkcd(StartsWithTranslator):
    begin = 'xkcd.com/'

    def __call__(self, url):
        number = re.search(r'https?://xkcd.com/(.*)/', url)

        if number:
            return 'http://explainxkcd.com/%s/' % (number.group(1))
        else:
            return 'http://explainxkcd.com/'
