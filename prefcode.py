class TrieNode: 
    def __init__(self): 
        self.l=None
        self.r=None
        self.isEndOfWord = False
  
class Trie: 
    def __init__(self): 
        self.root = self.get() 
  
    def get(self): 
        return TrieNode() 
  
    def insert(self,key): 
        p = self.root 
        length = len(key) 
        for level in range(length): 
            index = key[level]
            if p.isEndOfWord:
                # the prefix condition does not satisfy here
                return True
            if index=='0':
                if p.l==None: 
                    p.l = self.get() 
                p = p.l 
            else :
                if p.r==None:
                    p.r = self.get()
                p = p.r
        if p.isEndOfWord:
            # the prefix condition does not satisfy here
            return True
        p.isEndOfWord = True
        return False

def isprefixcode(codes):
    cl=list(codes.values())
    tr=Trie()
    pref=False
    for code in cl:
        ret = tr.insert(code)
        if ret:
            pref=True
            break

    if not pref:
        print("\n\n―――――――――――――――――――――――――――――――――――――――――――――――")
        print(    " The generated code is a valid prefix code.")
        print(    "―――――――――――――――――――――――――――――――――――――――――――――――")
    else :
        print("\n\n―――――――――――――――――――――――――――――――――――――――――――――――")
        print(    " The generated code is not a valid prefix code.")
        print(    "―――――――――――――――――――――――――――――――――――――――――――――――")