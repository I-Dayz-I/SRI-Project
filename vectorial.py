import re
import globals

def processQuery(query):
    curedQuery = re.split(' |\.|\\|\+|\*|\?|\[|\^|\]|\$|\(|\)|\{|\}|\=|\!|\||\:|\-|',query)
    query = globals.query
    