#Diccionario de documentos: key = Filename , value = Trie
CorpusDict = {}

#Cantidad de veces que aparece cada palabra en cada corpus: key = [word][file] , value = int
WordCorpusCount = {}

#Cantidad de documentos que constienen cada palabra key = Word ,  value = int
CorpusInDoc = {}

#La palabra de la query más repetida
MostRepeatedValue = {}

#Cuantos documentos contienen la palabra:
WordInDocuments = {}
ContainsWord ={}

#Tabla de frecuencia final por palabra 
Frequency = {}

FrequencyQuery = {}
TrieQuery= -1


LinkValueOfDoc ={}


TrieList= []
#Resultados finales
FinalDocumentList = []

#Palabras cercanas a las no encontradas
wordsNotFound ={}
wordsNotFounList =[]
wordsList = []

Expelled=["el","la","los","las","Un","uno","unos","una","unas","lo","al","yo","me",
          "mi","conmigo","tu", "te", "ti", "contigo","usted" ,"vos","el","lo" ,"le" ,
          "se" ,"si" ,"consigo" ,"ella" , "la", "ellos", "lo", "nosotros", "nos",
          "nosotras","vosotros","vosotras" , "os", "ustedes","Ellos", "ellas", 
          "los", "las", "les", "se", "si", "consigo","somebody","enough","mine",
          "somewhat","whatever","wherein","whereof","any","ourself","I","herself",
          "neither","everyone","whatnot","anybody","that","some","nothing","one","there",
          "it","something","such","both","whereto","whether","itself","he","where","nobody"
          ,"whom","several","our","its","theirself","naught","wherever","whomever","whomso",
          "this","thee","whomsoever","whose","everything","when","whosesoever","theirselves",
          "anyone","whosever","them","whosoever","you","whichsoever","your","wherefrom","him",
          "yourselves","which","her","whereinto","whereunto","who","me","none","what","those",
          "hers","other","ourselves","these","themself","many","ought","as","anything","someone",
          "my","whence","themselves","everybody","whoever","another","wherewith","she","few"
          ,"himself","whereby","we","ours","aught","wherewithal","suchlike","us","whatsoever",
          "their","all","either","his","myself","wheresoever","most","others","they","theirs",
          "whichever","each","yours","of","yourself","idem","be"]
BanWords = False

fnamesList = []
filedirection = {}

QueryList = []
alphaValue = 0.4
returnMinValue = 0.1
