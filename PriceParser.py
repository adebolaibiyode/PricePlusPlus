#Author : Adebola Ibiyode
#Language : SCB.Price++

import string
import nltk

Keywords = ["SUM","MINUS","DIVIDE","MULT","SPRICE","PIF","PELSE"]
parents = dict() #Dictionary Key, Value= [keyword,keyword_id]
children = dict() #Dictionary Key, Value= [parent_key,keyword_id]/Value= [parent_key,rule_element]

def checkKeyword(word):
    #check item is string #check keyword used in rule
    if (word.isalpha() and word.upper() in Keywords):     
        return True
    else:
        return False

def Prule(expression):
    pass

def tokeniseRule(expression,isid_words):
    #get indices of square brackets
    openBracket_indices = [index for (index, item) in enumerate(expression) if item == '[']
    closeBracket_indices = [index for (index, item) in enumerate(expression) if item == ']']
    count_openBracket =len(openBracket_indices)
    count_closeBracket =len(closeBracket_indices)

    words = []
    
    words.extend([
                word.lower() for word in
                nltk.word_tokenize(expression)
                if any(c.isalpha() or c.islower() or c.isnumeric() for c in word)
            ]) 
    id_words = []
    i = 0
    for w in words:
        wordtolist =[]
        checkcomma = w.find(',')
        if checkcomma > 0:
            wordtolist = list(w.split(","))
        
        if not w.isnumeric() and (len(wordtolist) <= 0) and checkKeyword(w):
            id_words.append(w + "_" + str(i))
        else:
            id_words.append(w)
        i +=1
    
    if isid_words:
        return id_words
    else:
        return words


def priceparser(rules):  

    lastitem_index = 0
    lastitem = ""
    lastkeyword =""
    currentkeyword = ""
    isnumber = False

    rule_id = tokeniseRule(rules,True)
    rule_nonid = tokeniseRule(rules,False)
    index = 0
    for rule in rule_nonid:        
        currentitem = rule
        #begining of the loop
        if index==0:
            lastitem = currentitem
            lastitem_index =rule_nonid.index(currentitem,index,index + 1)  

        wordtolist =[]
        iscurrentitemKeyword = False
        islastitemKeyword = False

        checkcomma = currentitem.find(',')
        if checkcomma > 0:
            wordtolist = list(currentitem.split(","))
        elif checkcomma == 0:
            currentitem = currentitem[1:]
            try:
                checknumber = float(currentitem)
                isnumber = True
            except ValueError:
                isnumber = False
        
        if checkcomma < 0 or len(wordtolist) <= 0: 
            iscurrentitemKeyword = checkKeyword(currentitem)
            islastitemKeyword = iscurrentitemKeyword 
            if index > 0:  
                islastitemKeyword = checkKeyword(lastitem)            
        
        if islastitemKeyword and lastitem != lastkeyword and index > 0:
            lastkeyword = lastitem

        #set current keyword as a parent
        if iscurrentitemKeyword:
            currentkeyword = currentitem
            #get index of lastitem from rule_id using start and end properties of the index function   
            curentitem_index = rule_nonid.index(currentitem,index,index + 1)  
        else:
            currentkeyword = lastkeyword
            curentitem_index = lastitem_index
        
       #last item is the parent of current item
        if islastitemKeyword and iscurrentitemKeyword:  
            #get id of keyword                     
            lastitem_id = rule_id[lastitem_index]            
            item_id = rule_id[curentitem_index]
                      
            parents[len(parents)] = [currentkeyword, item_id]
            if index > 0:
                #children[len(children)] = [len(parents) - 2, currentkeyword]
                children[len(children)] = [len(parents) - 2, item_id]
        else:
            if len(wordtolist) > 0 :                    
                #check if lastkeyword is in  parent            
                #if lastkeyword in parent, then get all list of lastkeyword in children
                #if lastkeyword not in parent, then  get 
                lastitem_id = rule_id[lastitem_index]   
                lastitem_list = [lastkeyword,lastitem_id]
                lastindex =0
                for key, item in parents.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    item.sort()
                    lastitem_list.sort()
                    if item == lastitem_list:
                        lastindex = key
                
                children[len(children)] = [lastindex,currentitem]
            elif isnumber and not checkKeyword(lastitem):                
                #get parent of last parent
                lastitem_id = rule_id[lastitem_index]  
                lastitem_split =lastitem_id.split("_")              
                
                parentindex =0
                for key, item in children.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if lastitem_id in item:
                        parentindex = item[0]
                        break
     
                if index > 0:
                    children[len(children)] = [parentindex, currentitem]

            elif iscurrentitemKeyword and not checkKeyword(lastitem):
                #this is a parent
                #get parent of last parent
                lastitem_id = rule_id[lastitem_index]  
                lastitem_split =lastitem_id.split("_")              
                
                parentindex =0
                for key, item in parents.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                    if item == lastitem_id:
                        parentindex = key
                        break
                
                item_id = rule_id[curentitem_index]
                        
                parents[len(parents)] = [currentkeyword, item_id]
                if index > 0:
                    children[len(children)] = [parentindex, item_id]

        lastitem = currentitem
        lastkeyword = currentkeyword
        lastitem_index = curentitem_index
        index +=1
    

#parser("Minus[RECCANHYDRO17,0.04]")
#priceparser("Mult[Minus[ProductA,0.04],Minus[ProductB,0.05],SUM[ProductC,0.06]]")
priceparser("Mult[Minus[ProductA,0.04],Minus[ProductB,0.05],SUM[ProductC,0.06],Divide[Sum[ProductD,3.0],5.55]]")
print("Parent Dictionary: " + str(parents))
print("Child Dictionary: " + str(children))  