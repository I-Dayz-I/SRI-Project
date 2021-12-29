
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.wordCount = 0

class Trie:
    def __init__(self, Document):
        self.nodes = []
        self.root = Node()
        self.document = -1
    
    
    def InsertWord(self, Word:str)->None:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode:
                lookingNode.children[letter] = Node()
            lookingNode = lookingNode.children[letter]
        lookingNode.endOfWord =True
        lookingNode.wordCount +=1
    
        
    
    def Search(self,Word:str)->bool:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode:
                return False
            lookingNode = lookingNode.children[letter]
        
        if lookingNode.endOfWord is True:
            return True
        else:
            return False
    
    

        
        