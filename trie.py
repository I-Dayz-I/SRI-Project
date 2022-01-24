
class Node:
    def __init__(self)->None:
        self.children = {}
        self.endOfWord = False
        self.wordCount = 0
        self.nextWord = []

class Trie:
    def __init__(self, Document)->None:
        self.nodes = []
        self.root = Node()
        self.lastWordIn = self.root
        self.document = Document

    
    
    def InsertWord(self, Word:str)->None:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode.children.keys():
                lookingNode.children[letter] = Node()
            lookingNode = lookingNode.children[letter]
        lookingNode.wordCount +=1
        lookingNode.endOfWord =True
        self.LastWordIn.nextWord.append(lookingNode)
        self.LastWordIn = lookingNode
        
    
    def Search(self,Word:str)->bool:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode.children.keys():
                return 0
            lookingNode = lookingNode.children[letter]
        
        if lookingNode.endOfWord is True:
            return lookingNode.wordCount

    
    

        
        