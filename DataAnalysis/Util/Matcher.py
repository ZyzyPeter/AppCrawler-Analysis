import re

matcherType={
    'singleActivity':r"\([^()]+\([^()]+\)\)",
    'date':'[A-Z][a-z]{2} [0-3][0-9]',
    'pricePair':"[0-9]{1,3}\.[0-9]{2}.+[0-9]{1,3}\.[0-9]{2}",
    'price':'[0-9]{1,3}\.[0-9]{2}'
}

class Matcher(object):
    def getPattern(self,type):
        regex=matcherType.get(type)
        return re.compile(regex)
    def getPatterText(self,type):
        return matcherType.get(type)
