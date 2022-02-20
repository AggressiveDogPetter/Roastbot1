def roastbot(roast):
    import requests 
    from bs4 import BeautifulSoup
    from random import randint
    import nltk
    import pygame as pg
    from nltk.corpus import wordnet
    
    def randsound():
        pg.mixer.init()
        pg.mixer.music.set_volume(1)
        
        num=randint(1,12)
        sound='s'+str(num)+'.mp3'
        pg.mixer.music.load(sound)
        
        pg.mixer.music.play()
    
    def randsyn(a,b):
        synonym=[]
        for syn in wordnet.synsets(a):
            for lemma in syn.lemmas():
                synonym.append(lemma.name())
        if synonym==[]:
            return a
        return (synonym[randint(0,len(synonym)-1)])
    
    def roastbot1(roast):
        
    
        global tagN
        global tagV
        global sent
        global tag
        global tag1
        global form
        global list_a
        
        total=[]
        attack=[]
        tagN=[]
        tagV=[]
        list_a=[]
        sent=""
        
        #Open website to access roast outlines
        r=requests.get('https://ponly.com/good-roasts/')
        soup=BeautifulSoup(r.content,features="lxml")
        
        #Fits the list to only roasts and comebacks
        for i in soup.find_all('p'):
            total.append(i.text)
        for i in range(len(total)):
            if i>=5 and i<64:
                attack.append(total[i])
            if i>=65 and i<78:
                attack.append(total[i])
            if i>=79 and i<87:
                attack.append(total[i])
                
        rand=randint(0,len(attack)-1)
        
        #choses a random roast to return
        form=attack[rand]
        if 'everyone' in form:
            form=attack[rand]
        
        #separates the different word forms from my roast
        token1=nltk.word_tokenize(form)
        tag1=nltk.pos_tag(token1)
        
        
        #analyze oponents roast
        token=nltk.word_tokenize(roast)
        tag=nltk.pos_tag(token)
        
        #Find which words to counter the oponent on
        for i in range(len(tag)):
            if tag[i][1]=="NN":
                tagN.append(randsyn(tag[i][0],tag[i][1]))
            elif tag[i][1]=="VB":
                tagV.append(randsyn(tag[i][0],tag[i][1]))
                
        if tagN==[] and tagV==[]:
            print(form)
            return form
        
        
        #Picks a random verb or noun from the oponents roast and choses a synonym
        elif tagN==[] and tagV!=[]:
            V=tagV[randint(0,len(tagV)-1)]
            AA=False
            for i in range(len(tag1)):
                if AA:
                    sent+=str(tag1[i][0])
                    sent+=' '
                    continue
                elif tag1[i][1]!='VB':
                    sent+=str(tag1[i][0])
                    sent+=' '
                elif tag1[i][1]=='VB':
                    sent+=str(tagV[0])
                    sent+=' '
                    AA=True
                    
            print(sent)
            return sent
        
        
        elif tagN!=[] and tagV==[]:
            N=tagN[randint(0,len(tagN)-1)]
            AA=False
            for i in range(len(tag1)):
                if AA:
                    sent+=str(tag1[i][0])
                    sent+=' '
                    continue
                elif tag1[i][1]!='NN':
                    sent+=str(tag1[i][0])
                    sent+=' '
                elif tag1[i][1]=='NN':
                    if tag1[i-1][1]=='NNP':
                        sent+=str(tag1[i][0])
                        sent+=' '
                        continue
                    sent+=str(tagN[0])
                    sent+=' '
                    AA=True
                
            print(sent)
            return sent
        else:
            V=tagV[randint(0,len(tagV)-1)]
            N=tagN[randint(0,len(tagN)-1)]
            AA=False
            for i in range(len(tag1)):
                if AA:
                    sent+=str(tag1[i][0])
                    sent+=' '
                    continue
                elif tag1[i][1]!='NN' and tag1[i][1]!='VB':
                    sent+=str(tag1[i][0])
                    sent+=' '
                elif tag1[i][1]=='NN':
                    if tag[i-1][1]=='NNP':
                        sent+=str(tag1[i][0])
                        sent+=' '
                        continue
                    sent+=str(tagN[0])
                    sent+=' '
                    AA=True
                elif tag1[i][1]=='VB':
                    sent+=str(tagV[0])
                    sent+=' '
                    AA=True
                    
            print(sent)
            return sent
    
    def roastbot2(roast):
        global p
        global total
        global words
        global nouns
        global verbs
        
        total=[]
        words=[]
        nouns=[]
        verbs=[]
        adj=[]
    
        r=requests.get('https://www.enchantedlearning.com/wordlist/negativewords.shtml')
        soup=BeautifulSoup(r.content,features="lxml")
        p=soup.find_all('div')
        
        for i in p:
            total.append(i.text)
            
        for i in total:
            if len(i)>=15:
                continue
            if len(i)<=3:
                continue
            words.append(i)
            
        del words[221:]
        del words[:7]
        
        for i in words:
            a=nltk.word_tokenize(i)
            b=nltk.pos_tag(a)
            if b[0][1]=='VB':
                verbs.append(i)
            if b[0][1]=='NN':
                nouns.append(i)
                
        def form1(nouns):
            r2=randint(0,len(nouns))
            a=nouns[r2]
            b='You are {}'.format(a)
            print(b)
            return b
        
        def form2(nouns):
            r1=randint(0,len(nouns))
            r2=randint(0,len(nouns))
            a=nouns[r2]
            b=nouns[r1]
            c='You are {} and {}'.format(a,b)
            print(c)
            return c
        
        def form3(nouns):
            r2=randint(0,len(nouns))
            a=nouns[r2]
            b='I could never kiss a {}... Thats you'.format(a)
            print(b)
            return b
        
        def form4(nouns):
            r1=randint(0,len(nouns))
            r2=randint(0,len(nouns))
            r3=randint(0,len(nouns))
            a=nouns[r2]
            b=nouns[r1]
            c=nouns[r3]
            d='You call yourself {}? Your {} is {}'.format(a,b,c)
            print(d)
            return d
        
        def form5(nouns):
            r1=randint(0,len(nouns))
            r2=randint(0,len(nouns))
            r3=randint(0,len(nouns))
            a=nouns[r2]
            b=nouns[r1]
            c=nouns[r3]
            d='I hate you because you are a {}, {}, and {}'.format(a,b,c)
            print(d)
            return d
        
        def form6(nouns):
            r2=randint(0,len(nouns))
            a=nouns[r2]
            b='I think you are {}'.format(a)
            print(b)
            return b
              
        def form7(nouns):
            r1=randint(0,len(nouns))
            r2=randint(0,len(nouns))
            r3=randint(0,len(nouns))
            r4=randint(0,len(nouns))
            a=nouns[r2]
            b=nouns[r1]
            c=nouns[r3]
            d=nouns[r4]
            e='Heres what I think about you... {}, {}, {}, and {}.'.format(a,b,c,d)
            print(e)
            return e
        
        
        rand=randint(0,6)
                
        if rand==0:
           return form1(nouns)
        if rand==1:
            return form2(nouns)
        if rand==2:
            return form3(nouns)
        if rand==3:
            return form4(nouns)
        if rand==4:
            return form5(nouns)
        if rand==5:
            return form6(nouns)
        if rand==6:
            return form7(nouns)
        
        
    def roastbot3(roast):
        opn=[]
        noun_list=['blacks','retards','faggots','your mom','your boyfriend','assholes',"Connor's bellybutton",'Jews']
        verb_list=['shoot','fuck','kill','mollest','finger','suck on','cum on', 'cum inside of']
        
        token=nltk.word_tokenize(roast)
        tag=nltk.pos_tag(token)
        
        for i in range(len(tag)):
            if tag[i][1]=='NN':
                opn.append(tag[i][0])
        if opn==[]:
            nn=randint(0,len(verb_list)-1)
            noun=noun_list[nn]
            
            vn=randint(0,len(noun_list)-1)
            verb=verb_list[vn]
            
            sent="You {} {}".format(verb, noun)
            
        elif len(opn)<2 and len(opn)>0:
            noun=opn[0]
            
            vn=randint(0,len(noun_list)-1)
            verb=verb_list[vn]
            
            sent="You {} your {}".format(verb, noun)
            
        elif len(opn)>=2:
            noun=opn[-1]
            
            vn=randint(0,len(noun_list)-1)
            verb=verb_list[vn]
            
            sent="Why dont you go {} your {}".format(verb, noun)
        
        print(sent)
        return sent
        
        
    bot=randint(1,100)
    
    randsound()
    if bot<=45:
        return roastbot1(roast)
    if bot>45 and bot<=75:
        return roastbot2(roast)
    if bot>75:
        return roastbot3(roast)
    
roastbot("")
