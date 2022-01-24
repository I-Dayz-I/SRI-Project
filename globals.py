#Diccionario de documentos: key = Filename , value = Trie
CorpusDict = {}

#Cantidad de veces que aparece cada palabra en cada corpus: key = [word][file] , value = int
WordCorpusCount = {}

#Cantidad de documentos que constienen cada palabra key = Word ,  value = int
CorpusInDoc = {}

#La palabra de la query más repetida
MostRepeatedValue = {}

#Tabla de frecuencia final por palabra 
Frequency = {}

#Resultados finales
FinalDocumentList = []


fnamesList = []
TrieList= []
QueryList = []
alphaValue = 0.4
returnMinValue = 0.1