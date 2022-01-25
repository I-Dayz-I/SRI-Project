import random


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
        self.lastWordIn.nextWord.append(lookingNode)
        self.lastWordIn = lookingNode
        
    
    def Search(self,Word:str)->bool:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode.children.keys():
                return 0
            lookingNode = lookingNode.children[letter]
        
        if lookingNode.endOfWord is True:
            return lookingNode.wordCount
        
    def SearchFinalNode(self,Word:str)->bool:
        lookingNode = self.root
        
        for letter in Word:
            if letter not in lookingNode.children.keys():
                return 0
            lookingNode = lookingNode.children[letter]
        
        if lookingNode.endOfWord is True:
            return lookingNode
    
    def SearchClosestWord(self,Word):
        lookingNode = self.root
        randomWord = ""
        
        for letter in Word:
            if letter not in lookingNode.children.keys():
                if lookingNode == self.root:
                    return ""
                else:
                    return randomWord+ self.CompleteRandomWord(lookingNode)
            else:
                randomWord+=letter
                lookingNode = lookingNode.children[letter]

        
        if lookingNode.endOfWord is True:
            return randomWord

    def CompleteRandomWord(self,node):
        lookingNode = node
        completion =""
        while lookingNode.endOfWord != True:
            Rrange = random.randint(0,len(lookingNode.children)-1)
            Rkeys =  random.choice(list(lookingNode.children.keys()))
            completion += Rkeys
            lookingNode = lookingNode.children[Rkeys]
        
        return completion
    

        
        