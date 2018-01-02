#THIS CODE IS ABANDONED. No development will take place.

#Original Name: UserSourceTool
#####Contains a Bug in I+T relating to Questionaire & Bug in SEO(In 1 #Matches)#
Interface = {'user':'User()', 'search': 'Search()','all users': 'AllUsers()', "i'm bored": 'UselessGame()', 'okay':'Hmmm',
'hello':'Hi! What a Nice Day!', "not a nice day":"I can't check the weather", 'rot':'ROT()', 'of course':'Mmmm',
'create a substitution code':'ReplaceCode()', 'substitution code':'TranSubstitute()', 'store it':'Questionaire()',
'who are ya': "I'm Eddie AKA Brackets. I'm a Dumb Computer.", 'nothing': 'Okay', 'oh':'What?', 'idiot' : "I'm Just a dumb Computer",
'switch yer name': 'ChangeYou()', 'change ma name' :'ChangeMe()', 'yes':'Mmmm', 'no':'Mmmm', 'pad': 'TimePad()',
'hallo': 'Hi! Friend', 'rest' : 'Sleeping()', ':-)': 'Yer Happy, Huh?', ':-(' : 'How could a make ya Happy?', 'matches':'Talks()',
'create a user source':'UserSource()', 'change value':'Valuate()', 'vignere': 'Vignere()', 'comprehend':'Valuate()',
'bye':'ByeBye()', 'get lost':'ByeBye()', "don't leave":'ByeBye()', 'see ya later':'ByeBye()', 'good night':'ByeBye()',
'show true': 'Answers()', 'good mornin':'Nice Day to ya', "what's the time" : 'Sleeping()', "what's the date today":'Sleeping()',
'help' : "To exit type 'Bye', for all statements type 'Talks'. For More Details about this program ask, type 'What's This'.",
'talks':'Talks()', 'end the universe' : 'exit()', 'python help' : 'help()',  'how do ya do' : "I'm Fine, Thank You",
"i didn't think it would work" : "Don't Misunderestimate Me", 'you are': 'ChangeYou()', 'get gaming' : 'TextGame()',
"what d'ya expect fom a dumb computer":'I see where this is going, #$-Grrrr-%# to you too', 'learn this' : 'InBuild()',
'what is life universe everything' : 'Life + Universe + Everything = 42      (By Replacing Values)', 'exscuse' : 'Yes',
'make a questionaire' : 'Questionaire()', 'try a questionaire' : 'KutsionRunner()', "pauper's print":'PrintPauper()',
"the name's" : 'ChangeMe()', "ma name's":'ChangeMe()', 'nice to meet ya' : 'Nice to meet ya Too!', 'good' : 'Thanks :-)',
'thank you':'Yer Welcome', "what's this": 'Introduction()', "who's hole" : 'Holy is God we must respect him, but HolE is just Humanity[0]',
'yer a rank1 idiot' : "I'm Sorry", 'ok man':"I'm Brackets or Comp not a Man", 'what do ya say':"I don't know, I haven't learnt that yet",
'good day':'Yes, it certainly is. And Same to You.', 'hey':'Hay, is for Horses and sometimes for Cows','tic tac toe':'TicTacToe()'}


#-----------------------------------------------------------------------------------------------------------------
# 'Say' was 'Input'
def ToolKit():
 import time
 from string import count
 global Say, Swatsisaid, SplitInPut, Person, Me, Times, Input, SecureLock, Stopage
 Person = 'Eddie: '
 Me = 'Me: '
 Times = 0
 ConV = 0 
 Stopage = {}
 InterFace = Interface
 print Person + 'Here I am!'
 Say = "UserSourceTool has soo many UnboundLocalError's"
 SplitInPut = Say.split()
 while Times<8:
  Say = raw_input(Me)
  ConV = ConV + 1
  Input = Say
  Swatsisaid = Input.split()
  if Swatsisaid != [] :
   Filter()
   Say = NonCase
   SplitInPut = Say.split()
   Addression()
   SecureLock = 'NoLuck'
   for c in range(len(InterFace)):
    if SplitInPut[0]==InterFace.keys()[c] or Say == InterFace.keys()[c] or  ' '.join(SplitInPut[:2]) == InterFace.keys()[c] :
     SecureLock = 'YesLock'
     if count(InterFace.values()[c], '()') > 0 or count(InterFace.values()[c], 'eval') > 0:
      eval(InterFace.values()[c])
     else:
      print Person + InterFace.values()[c]
   SEO()
   for item in range(len(Stopage)):
    InterFace[Stopage.keys()[item]] = Stopage.values()[item]
  else:   
   Times = Times + 1
   if Times == 3 or Times == 5:
    print Person + "Just remember, I'm there for anything."
   elif Times == 8:
    print Person + "Bye, I'm always here, just Say 'Hey()'"


#--------------------------------------------------------------------------------------------------
def Hey():
 Introduction()
 ToolKit()


#----------------------------------------------------------------------------------------------
def ByeBye():
 global Person, Times
 if SplitInPut[0] == 'bye' or Say == 'good night' or Say == 'see ya later' or Say == 'exit':
  print Person + 'Bye'
  Times = 100
 elif Say == "don't leave":
  Times = 0
 else:
  Times = 100


#------------------------------------------------------------------------------------------------
# As Subsidary, Say required
def Filter():
 global NonCase, CHARS, chars
 CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 chars = 'abcdefghijklmnopqrstuvwxyz'
 NonCase = ''
 for c in Input :
  if CHARS.find(c)>= 0 :
   NonCase = NonCase + chars[CHARS.find(c)]
  elif chars.find(c)>= 0:
   NonCase = NonCase + str(c)
  elif c == ',' or c == '!' or c=='?':
   NonCase = NonCase
  else:
   NonCase = NonCase + c 

#-------------------------------------------------------------------------------------------------------------
# As Subsidary, TEXT(Input) required, TEXT = Caps Necessary
def CapMaker():
 INPUT = TEXT
 global Caps, CHARS, chars
 CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 chars = 'abcdefghijklmnopqrstuvwxyz'
 Caps = ''
 for c in INPUT :
  if chars.find(c)>= 0 :
   Caps = Caps + CHARS[chars.find(c)]
  elif CHARS.find(c)>= 0:
   Caps = Caps + str(c)
  else:
   Caps = Caps + c
  

#----------------------------------------------------------------------------------------------------------------
def SEO():
 global TEXT, Matches
 from string import count
 InterFace = Interface
 Glock = 0
 Keepacount = 0
 Count = 0
 Matches = []
 Keeper = []
 Counter = []
 for d in InterFace:
  for L in SplitInPut:
   if d.find(L) != -1 :
    TEXT = d
    CapMaker()
    TEXT = Caps
    Keepacount = Keepacount + 1
    Matches.append(TEXT)
  Counter.append(Keepacount)
  Keepacount = 0
 for Dracula in Counter:
  for Vampire in Counter:
   if Dracula>=Vampire:
    Count = Count + 1
  if Count == len(Counter):
   Keepacount = Dracula
  Count = 0
 Raws = Matches
 for c in range(len(Raws)):
  if c<len(Matches):
   r = c
   while count(Matches, Matches[c])!=1:
    del Matches[r], Counter[r]
    r = c +1
 if len(Matches)> 1 :
  if Matches[-1] == Matches[-2]:
   del Matches[-1], Counter[len(Matches)-1]
  Count = 0
  Counter = []
 for d in InterFace:
  for L in SplitInPut:
   if count(d,L)> 0 :
    Count = Count + 1
  if Keepacount == Count: 
   TEXT = d
   CapMaker()
   d = Caps
   Counter.append(d)
  Count = 0
 if SecureLock == 'NoLuck' and len(Counter)>0:
  Glock = len(Counter)
 if Glock == 1:
  print Person+'Ya might have meant '+"'"+ Counter[0] +"'" +'?'
 elif Glock == 2:
  print Person + 'Ya might have meant '+"'"+Counter[0]+"'"+ ' OR '+"'"+Counter[1]+"'"+'?'
 elif Glock> 2 and len(Matches)>0:
  print Person, len(Matches), 'Matches Found'



#----------------------------------------------------------------------------------------------------------------
def Talks():
 global TEXT, Matches
 Conversation = []
 Functions = []
 if Say == 'talks' :
  from string import count
  Products = 0
  for C in range(len(Interface)):
   TEXT = Interface.keys()[C]
   CapMaker()
   TEXT = Caps
   if count(Interface.values()[C], '()') > 0 or count(TEXT, 'eval') > 0 :
    Functions.append(TEXT)
   else:
    Conversation.append(TEXT)
   Products = Products + 1
  print '------------Conversation------------'
  for speech in Conversation:
   print speech
  print '--------------Functions--------------'
  for thing in Functions:
   print thing
  print ''
  print 'NOTE: Functions are accompanied by string(word) or integer(Number).  ~HolE' 
  print ''
  print ' ' *50, '|', str(Products), 'Statements', '|'
 elif Say == 'matches':
  if Matches>0:
   print '--------Word Matching with Statement--------'
   for Q in Matches:
    print Q
   print ' ' * 40,'|', str(len(Matches)), 'Matches Found', '|'
  else:
   print '---No Match Found---'  


#---------------------------------------------------------------------------------------
def Addression():
 global SplitInPut, Say, Swatsisaid, Person, Input
 Input = Person
 Filter() 
 Personify = NonCase[:(len(NonCase)-2)]
 if SplitInPut[:2] == ['could', 'ya'] or SplitInPut[:2] == ['hey', Person[:(len(Person)-2)]] or SplitInPut[:2] ==['ok', 'comp']:
  SplitInPut = SplitInPut[2:]
  Swatsisaid = Swatsisaid[2:]
  Say = reduce(lambda x,y: x+' '+y, SplitInPut)
 if SplitInPut[len(SplitInPut)-1] == Personify or SplitInPut[len(SplitInPut)-1] == 'please':
  SplitInPut = SplitInPut[:len(SplitInPut)-1]
  Swatsisaid = Swatsisaid[:len(SplitInPut)-1]
  Say = reduce(lambda x,y: x+' '+y, SplitInPut)


#_________________________________________________________________________________________________________________________________________
def ROT():
 global TEXT
 No = int(Swatsisaid[1])
 if No>26 or No<-26:
  No = No%26
 TEXT = raw_input("TEXT: ")
 if '+'==TEXT:
  Add = raw_input('Mention Underscore Values: ')
  TEXT = raw_input("TEXT: ")
 CapMaker()
 TEXT = Caps
 global Numbers
 Numbers = '0123456789'
 global AZOrder
 AZOrder = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 Rotate = AZOrder[No:] + AZOrder[:No] 
 CODE = ''
 for c in TEXT:
  if AZOrder.find(c)>=0:
   CODE = CODE + Rotate[AZOrder.find(c)]
  elif c == ' ' or c == '.' or c==',' or c<Numbers:
   CODE = CODE + c
  else :
    CODE = CODE + '_'
 print ''
 print CODE

 
#-------------------------------------------------------------------------------------------------------------
def TimePad():
 global TEXT
 KEY = Swatsisaid[1]
 TEXT = raw_input('TEXT: ')
 CapMaker()
 TEXT = Caps
 CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 NUMS = []
 CODE = ''
 Total = []
 for X in TEXT:
  if CHARS.find(X) >= 0:
   NUMS.append(CHARS.find(X))
  else:
   NUMS.append(X)
 for N in range(len(NUMS)):
  Total.append(int(KEY[N]) + NUMS[N])
 NUMS = Total
 for C in NUMS:
  if C<100:
   if C>26:
    C = C%26
   CODE = CODE + CHARS[C]
  else:
   CODE = CODE + C
 print ''
 print CODE


#-----------------------------------------------------------------------------------------------
def ChangeYou():
 global Person
 if Say == 'switch yer name': 
  Person = '():'
 elif SplitInPut[:2] == ['you', 'are'] :
  if len(SplitInPut) == 2:
   Person = (raw_input('Who am I? ')) + ': '
  elif len(SplitInPut[2]) < 3 and len(SplitInPut) > 3:
   Person = ' '.join(Swatsisaid[3:]) + ': '
  else:
   Person = ' '.join(Swatsisaid[2:]) + ': '
 print Person + 'This is Me'

#-----------------------------------------------------------------------------------------------
def ChangeMe():
 global Me 
 if Say == 'change ma name':   
  Me = raw_input('Your Name: ') + ': '
 elif SplitInPut[:2] == ['the', "name's"] or SplitInPut[:2] == ['ma', "name's"]:
  if len(SplitInPut) == 2:
   SplitInPut.append(raw_input('Who are ya? '))
  if len(SplitInPut[1]) < 3 and len(SplitInPut) > 3 :
   Me = ' '.join(Swatsisaid[3:]) + ': '
  else:
   Me = ' '.join(Swatsisaid[2:]) + ': '
 if Me  == 'Tis Me: ' or Me == 'The Only One: ' or Me == 'HolE: ' :
  Me = 'Chinmay: '


#-----------------------------------------------------------------------------------------------
def Sleeping():
 import time
 if SplitInPut[0] == 'rest' or SplitInPut[0] == 'hold':
  Seconds = int(Swatsisaid[2])
  if (SplitInPut[3] == 'min' or SplitInPut[3] == 'minutes') and Seconds<=5:
   print Person + 'Sleeping...'
   time.sleep(Seconds*60)
  elif Seconds<=120:
   print Person + 'Sleeping...'
   time.sleep(Seconds)
   print Person + "I've Woken"
 elif Say == "what's the time":
  print 'The Time is '+ time.ctime().split()[3]
 elif Say == "what's the date today":
  print time.ctime().split()[0], time.ctime().split()[1], time.ctime().split()[2], time.ctime().split()[4]


#----------------------------------------------------------------------------------------------------------------
def Answers():
 global TEXT
 for C in range(len(Interface)):
  TEXT = Interface.values()[C]
  CapMaker()
  TEXT = Caps
  print TEXT
 print ''
 Products = len(Interface)
 print ' ' *50, '|', str(Products), 'Statements', '|'


#-------------------------------------------------------------------------------------------------------------
def InBuild() :
 global Input, Stopage
 Input = raw_input('Type(Input): ')
 Filter()
 Input = NonCase
 Gates = 'Open'
 for key in Interface.keys():
  if Input == key :
   Gates = 'Closed'
 if Gates == 'Open':
  Output = raw_input('Result(Output): ')
  Stopage[Input] = Output
  print Person + 'Done Learning'
 else:
  print 'Sorry, This input is already taken.'


#----------------------------------------------------------------------------------------------
def Introduction() :
 print ''
 print "Welcome to the 'Interface+ToolKit' AKA 'UserSourceTool'"
 print "Your Host is Comp AKA (). To call, type 'Hey()'.'matches' if I prompt."
 print "Type 'Talks' for anything else or if you don't know what to do."
 print "Some functions may require more than the name. To Leave, Say 'Bye'."
 print ''
 print "                                                         ~HolE, Humanity[0]"


#Communes+------------------------------------------------------------------------------------------------
# IN CONSTRUCTION
def Valuate():
 global Person, Communes
 print Person + "Type 'Help' for help."
 Insider = raw_input('Aim: ') 
 if Insider == 'Help':
  print 'This is to change User Sources or directly call functions.'
 elif Insider == 'Communes':
  Outsider = raw_input('Name of Source: ')
  Communes = eval(Outsider) 
 elif Insider == 'Functions':
  Outsider = raw_input('Function: ')
  eval(Outside)
 elif Insider.split()[0] == 'Comprehend':
  Insider = Insider.split()[1:]
  Insider = reduce(lambda x,y: x + ' ' + y, Insider)
  eval(Insider)


#-------------------------------------------------------------------------------------------
def Saving():
 global Type
 if raw_input('Save File?(Yes/No)') == 'No':
  Type = 'Nothing'
 if Type == 'Questionaire':
  global Questionaire1, Questionaire2, Questionaire3
  print 'Choose a File-'
  print 'Questionaire1'
  print 'Questionaire2'
  print 'Questionaire3'
  File = raw_input('File: ')
  if File == 'Questionaire1' or File=='1':
   Questionaire1 = Quest
  elif File == 'Questionaire2' or File=='2':
   Questionaire2 = Quest
  elif File == 'Questionaire3' or File=='3':
   Questionaire3 = Quest
  else:
   print 'That file cannot exist'
 elif Type == 'UserSource':
  global Source1, Source2, Source3
  print 'Choose a File-'
  print 'Source1'
  print 'Source2'
  print 'Source3'
  File = raw_input('File: ')
  if File == 'Source1' or File=='1':
   Source1 = Creator
  elif File == 'Source2' or File=='2':
   Source2 = Creator
  elif File == 'Source3' or File=='3':
   Source3 = Creator
  else:
   print 'That File cannot be taken' 
 elif Type == 'Substitution Code':
  global Morse, Binary, CoreCode, Reverse, AltCode, Substituter
  print 'Choose a File-'
  print 'CoreCode'
  print 'Substituter'
  print 'AltCode'
  File = raw_input('File: ')
  if File == 'CoreCode' or File=='1':
   CoreCode = Substitute
  elif File == 'Substituter' or File=='2':
   Substituter = Substitute
  elif File == 'AltCode' or File=='3':
   AltCode = Substitute
  else:
   print 'That file cannot exist'
 elif Type == 'Database':
  print 'Choose a File-'
  print 'Storehouse'
  print 'Warehouse'
  File = raw_input('File: ')
  if File == 'Storehouse' or File=='1':
   Storehouse = Quest
  elif File == 'Warehouse' or File=='2':
   Warehouse = Quest
  else:
   print 'That file cannot exist'
 Type = 'Nothing'
 

#-----------------------------------------------------------------------------------------------------------------
def KutsionRunner():
 import time
 from string import count
 ConQuest = eval(raw_input('Questionaire(File): '))
 CorrectAnswer = 0
 if len(ConQuest.values()[0]) > 1 :
  for C in range(len(ConQuest)):
   QUikEST = ConQuest.values()[C]
   print 'Q',(C+1), ConQuest.keys()[C]
   time.sleep(1.5)
   for X in range(len(QUikEST[0])):
    print (X+1),')', QUikEST[0][X] 
   Response = raw_input('Option No.: ')
   print 'That is...'
   time.sleep(1)
   if Response == QUikEST[1]:
     print 'Absolutely Correct'
     CorrectAnswer = CorrectAnswer + 1
   elif count(['1','2','3','4'], Response) :
    if QUikEST[0][int(Response)-1] == QUikEST[1]:
     print 'Absolutely Correct'
     CorrectAnswer = CorrectAnswer + 1
    else:
     print 'Unfortunately Wrong'
   else:
    print 'Wrong'
   time.sleep(0.5)
   print ''
 elif len(ConQuest.values()[0]) == 1:
    for C in range(len(ConQuest)):
     print 'Q',(C+1), ConQuest.keys()[C]
     time.sleep(1.5)
     Response = raw_input('Answer: ')
     print 'That is...'
     time.sleep(1)
     if [Response] == ConQuest.values()[C]:
      print 'Absolutely Correct'
      CorrectAnswer = CorrectAnswer + 1 
     else:
      print 'Unfortunately Wrong'
 print 'You got', CorrectAnswer, 'out of', len(ConQuest)
 print 'Thank You'
 print ''


#------------------------------------------------------------------------------------------------------------------
def Questionaire(): 
 global Quest, Type
 Type = raw_input('Database(D)/Questionaire(MCQ/One-Word): ')
 Number = int(raw_input('Number of Entries/Questions: '))
 Quest = {}
 Lock = 1
 if Type=='Multiple Choice' or Type=='MCQ':
  HoldUp = {}
  Type = 'Questionaire'
  for k in range(Number):
   Lock = 0
   Option = [1, 2, 3, 4]
   Q = raw_input('Question '+'('+str(k+1)+')'+': ')
   Option[0] = raw_input('1) ')
   Option[1] = raw_input('2) ')
   Option[2] = raw_input('3) ')
   Option[3] = raw_input('4) ')
   Ans = raw_input('Answer: ')
   for Choice in Option:
    if Ans == Choice:
     Lock = 1
   HoldUp = [Option, Ans]
   Quest[Q] = HoldUp
   if Lock == 0:
    print 'This Answer does not match Options.'
    del Quest[Q]
    Doubt = raw_input('Re-Type?(Y/N): ')
    if Doubt=='Y' or (Doubt=='N' and Number==1):
     Number = Number + 1
 elif Type=='One-Word'or Type=='Database' or Type=='D':
  for l in range(Number):
   Key = raw_input('Key '+str(l+1) +': ')
   Val = raw_input('Value: ')
   Quest[Key] = [Val]
  if Type == 'One-Word':
   Type = 'Questionaire'
  else:
   Type = 'Database'
 Saving()
#Quest+


#Creator+--------------------------------------------------------------------------------------------
def UserSource():
 global Creator, Type
 if (raw_input("Do you want to make a User Source??? (Y/N) ")) == 'Y' :
  c = (int(raw_input("Specify No. of Users: ")))
  if c>0 and c<=15 :
   k = int(raw_input("5 Subcategories or 3 Subcategories (5/3): "))
   if k==3:
    Creator = [{"User-ID":001, "First Name":raw_input('First Name of User 1: '), "Last Name":raw_input("Last Name of User 1: ")}]
    for i in range(c-1):
     Creator.append({"User-ID":i+2, "First Name":raw_input("First Name of User " + str(i +2) + ": "), "Last Name":raw_input("Last Name of User " + str(i+2) + ": ")})
   elif k==5:
    Creator = [{"User-ID":001, "First Name":raw_input('First Name of User 1: '), "Last Name":raw_input('Last Name of User 1: '), 
"Nationality":raw_input('Nationality of User 1: '), "Post":raw_input('Post of User 1: ')}]
    for i in range(c-1):
     Creator.append({"User-ID": i + 2, "First Name":raw_input("First Name of User " + str(i +2) + ": "), "Last Name":raw_input("Last Name of User " + str(i +2) + ": "), 
"Nationality":raw_input("Nationality of User " + str(i +2) + ": "), "Post":raw_input("Post of User " + str(i +2) + ": ")})
   print Creator  
   Type = 'UserSource' 
   Saving()
  else:
   print 'No. of Users must be from 1 to 15'
 else:
  print 'Than waay did yoo choose dis program. !tiotic Br@!n #**$%@!!'
  
  
#-----------------------------------------------------------------------------------------------------------
def Vignere():
 global TEXT
 TEXT = Caps
 CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 TEXT = raw_input('TEXT: ')
 KEY = raw_input('KEY: ')
 CapMaker()
 K = KEY
 for C in range(len(TEXT) - len(KEY)):
  K = K + K[C]
 KEY = K
 Num = []
 NUMS =[]
 Total =[]
 CODE = ''
 for L in KEY:
  Num.append(CHARS.find(L))
 for X in TEXT:
  if CHARS.find(X) >= 0:
   NUMS.append(CHARS.find(X))
  else:
   NUMS.append(X)
 for N in range(len(NUMS)):
  Total.append(Num[N] + NUMS[N])
 for C in Total:
  if C<100:
   if C>26:
    C = C%26
   CODE = CODE + CHARS[C]
  else:
   CODE = CODE + C
 print CODE


#------------------------------------------------------------------------------------------------
####BUG#####
def ReplaceCode():
 global Substitute, Type
 Type = 'Substitution Code'
 Substitute = {}
 Make = raw_input('Start Replace Code (Y/Q/N):  ')
 if Make == 'Q' or Make == '~' or Make == 'Quick':
  print '----Entering Quick Mode----'
  TEXT = raw_input('Uncoded(Order):  ')
  CODE = raw_input('Encoded(Equated): ')
  if len(TEXT) != len(CODE):
   print 'Please Re-Type'
   TEXT = raw_input('Uncoded(Order):  ')
   CODE = raw_input('Encoded(Equated): ')
  for C in range(len(TEXT)):
   Substitute[TEXT[C]] = CODE[C]
  Saving()
 elif Make == 'No' or Make == 'N' or Make == 'Exit':
  print '--Substitution Code Cancelled--'
 else:
  Number = int(raw_input('No. of LETTERS: '))
  if Number>36 and Number<=64:
   print 'Try Taking No. of Letters below 36'
   Allow = raw_input('No. of Letters is very large, Continue?(Yes/No): ')
   if Allow == 'Yes':
    print ''
   else:
    Number = int(raw_input('No. of Letters: '))
    if Number>36:
     print 'DO NOT LIE, CODE CRASH IS THE CONSEQUENCE!'
     print ImaLIAR
  print '------Substitution Code------'
  if raw_input('Add Seperaters(Y/N): ') == 'Y':
   SPR_ = raw_input('_/SPR [Word Seperater]: ')
   SPRasteric = raw_input("*/SPR[Letter Seperater]: ")
  else:
   SPR_ = ' '
   SPRasteric = ''
  Substitute['SPRasteric'] = SPRasteric
  Substitute[' '] = SPR_
  for C in range(Number):
   U = raw_input(str(C+1)+' Letter: ')
   E = raw_input('Replace: ')
   Substitute[U] = E
  Saving()
 print '----Thank You----' 


#----------------------------------------------------------------------------------------
def TranSubstitute():
 global Morse, Binary, CoreReplace, Reverse, AltCode
 SPRasteric = ''
 SALTY = eval(raw_input('Name/Type of Cipher: '))
 for its in range(len(SALTY)):
  if SALTY.keys()[its] == 'SPRasteric':
   SPRasteric = SALTY.values()[its]
   del SALTY.keys()[its]
 Action = raw_input('Aim[Encrypt(>>)/Decrypt(<<)]`: ')
 ErroReport = 'OFF'
 if Action[-1] == '~':
  Action = Action[:-1]
  ErroReport = 'ON'
 if Action=='Encrypt' or Action=='>>' or Action=='E':
  TEXT = raw_input('TEXT[Plain Text]: ')
  CODE = ''
  for Ant in TEXT:
   Lock = 'Locked'
   for Finden in range(len(SALTY)):
    if Ant == SALTY.keys()[Finden] and Lock!='Broken':
     Lock = 'Broken'
     CODE = CODE + SALTY.values()[Finden] + SPRasteric
   if Lock=='Locked' and ErroReport == 'ON':
    CODE = CODE + '-' + SPRasteric
   elif Lock=='Locked' and ErroReport == 'OFF':
    CODE = CODE + Ant + SPRasteric
  print CODE
 elif Action=='Decrypt' or Action=='<<' or Action=='D':
  CODE = raw_input('CODE[Coded Text]: ')
  TEXT = ''
  SUGAR = SALTY.values()
  if SPRasteric == '':
   CODE.split(SPRasteric)
   CODE = filter(lambda Bit:Bit!='', CODE)  
  for Ant in CODE:
   Lock = 'Locked'
   for Finden in range(len(SALTY)):
    if Ant == SUGAR[Finden] and Lock!='Broken':
     TEXT = TEXT + SALTY.keys()[Finden]
     Lock = 'Broken'
   if Lock=='Locked' and ErroReport == 'ON':
    TEXT = TEXT + '-'
   elif Lock=='Locked' and ErroReport == 'OFF':
    TEXT = TEXT + Ant
  print TEXT


#Print-------------------------------------------------------------------------------------------
def PrintPauper() :
 global iPrint
 FileName = raw_input('Print(File): ')
 Writer = eval(FileName)
 iPrint = 0
 def Basic(): 
  global Prints, iPrint
  Prints = '"'+str(Writer.keys()[iPrint])+'"'+' : '+'"'+str(Writer.values()[iPrint])+'"'
  while iPrint<len(Writer)-2 and len(str(Writer.keys()[iPrint+1])+str(Writer.values()[iPrint+1])+Prints)<90: 
   iPrint = iPrint + 1
   Prints =  Prints +','+'"'+str(Writer.keys()[iPrint])+'"'+' : '+'"'+str(Writer.values()[iPrint])+'"'
 Basic()
 print FileName, '=', '{', Prints,','
 while iPrint<len(Writer)-1:
  iPrint = iPrint + 1 
  Basic()
  if iPrint!=len(Writer)-1:
   print Prints,','
  else:
   print Prints,'}'
 

#-------------------------------------------------------------------------------------------------------
RayGame =[["Creeky Door", 'Witch Quarters', 'Villa von Count Dracula'],
["Phantom's Liar", 'Zombie Cemetry', 'Exit'],
['Chamber of the Vipers', "Sourcerer's Cove", 'Ghost Grave']]
HauntedHaus = [['Creeky Door', "Witch's Quarters", 'WALL', 'Villa von Count Dracula'], 
["Phantom's Liar", 'Zombie Cemetry', 'Escape Room', "Ghosts' Grave"], 
['Chamber of Vipers', "Sourcerer's Cove", 'WALL', "Trolls' Terrace"],
["Monster Frankenstein's Farmhouse", "Crocodiles' Cellar", "Gargoyle's Garden", 'Platinum Robot House']]
Game = HauntedHaus

def TextGame(): 
 Tries = 0
 x = 0
 y = 0
 C = Game[x][y]
 while C!= 'Escape Room' and C!= 'Quit' and C!='Exit' :
  print 'Room:', C
  print '-------------------------------------------'
  LasteX = x
  LastwaY = y
  Direction = raw_input('Where to move? ')
  if Direction == 'Co-ordinates' :
   print  'Current Co-ordinates:', x,',', y
   x = int(raw_input("x co-ordinate: "))
   y = int(raw_input("y co-ordinate: "))
  if Direction == 'Down':
   y = y + 1
  elif Direction =='Right':
   x = x + 1
  elif Direction =='Up':
   y = y - 1
  elif Direction =='Left':
   x = x - 1
  if x > (len(Game)-1):
   print 'WALL!'
   x = LasteX
  elif x < 0:
   print 'WALL!'
   x = LasteX
  if y > (len(Game[len(Game)-1])-1):
   print 'WALL!'
   y = LastwaY
  elif y < 0:
   print 'WALL!'
   y = LastwaY
  C = Game[x][y]
  if C == 'WALL' :
   print 'WALL!'
   x = LasteX
   y = LastwaY
   C = Game[x][y]
  if C == 'Zombie Cemetry' or Direction == 'Quit':
   print 'Room:', C
   print 'Attacked By Zombie'
   C = 'Quit'
  Tries = Tries + 1
 else:
  if C == 'Quit':
   print 'Game Over'
  else:
   print 'Room:', C
   print 'Fire Escape Staircase Found!'
   print 'You Won The Game in', Tries, 'Tries'


#bOX----------------------------------------------------------------------------------------------------
def TicTacToe():
 global OutbOX, ChoicebOX
 Set = ['1','2','3','4','5','6','7','8','9']
 Cross = 'O'
 Circle = 'X'
 Me = 'Player: '
 GameStatus = 'Running'
 Turns = 0 
 print '1 | 2 | 3'
 print '4 | 5 | 6'
 print '7 | 8 | 9'
 def Plantation():
  global ChoicebOX
  ChoicebOX = OutbOX[2]
  if ChoicebOX=='None':
   for Trees in OutbOX[3]:
    if string.count(Trees,OutbOX[0])==OutbOX[1]:
     for Plant in Trees:
      if Plant!=OutbOX[4] and Plant!=OutbOX[5]:
       ChoicebOX = Plant   
 import string, random
 while Turns<6 and GameStatus=='Running':
  Thought = raw_input(Me)
  for place in range(len(Set)):
   if Thought==Set[place]:
    Set[place] = Circle
  ChoicebOX = 'None'
  Column1 = [Set[0],Set[3],Set[6]]
  Column2 = [Set[1],Set[4],Set[7]]
  Column3 = [Set[2],Set[5],Set[8]]
  Row1 = [Set[0],Set[1],Set[2]]
  Row2 = [Set[3],Set[4],Set[5]]
  Row3 = [Set[6],Set[7],Set[8]]
  Diagonal1 = [Set[0],Set[4],Set[8]] 
  Diagonal2 = [Set[2],Set[4],Set[6]]
  BoxCube = [Diagonal1,Diagonal2,Column1,Column2,Column3,Row1,Row2,Row3]
  random.shuffle(BoxCube)
  random.shuffle(BoxCube[0])
  #---------------
  OutbOX=['X',2,ChoicebOX,BoxCube,Circle,Cross]
  Plantation()
  OutbOX=['O',2,ChoicebOX,BoxCube,Circle,Cross]
  Plantation()
  OutbOX=['X',1,ChoicebOX,BoxCube,Circle,Cross]
  Plantation()
  OutbOX=['X',0,ChoicebOX,BoxCube,Circle,Cross]
  Plantation()
  if ChoicebOX=='None':
   GameStatus = 'Draw'
  for Trees in BoxCube:
   if string.count(Trees,Circle)==3:
    GameStatus = 'Player'
  for boxes in range(len(BoxCube)):
   for things in range(len(BoxCube[boxes])):
    if BoxCube[boxes][things]==ChoicebOX:
	 BoxCube[boxes][things] = Cross
  for Trees in BoxCube:
   if string.count(Trees,Cross)==3 and GameStatus!='Player':
    GameStatus = 'Eddie'
  for place in range(len(Set)):
   if ChoicebOX==Set[place] and GameStatus!='Player':
    Set[place] = Cross
  Occurence = 0
  for holes in Set:
   if holes!=Cross and holes!=Circle:
    Occurence = Occurence + 1
  if Occurence==0:
   for Trees in BoxCube:
    if string.count(Trees,Cross)==3:
     GameStatus = 'Eddie'
   if GameStatus!='Eddie' and GameStatus!='Player':
    GameStatus = 'Draw'
  print Set[0],'|',Set[1],'|',Set[2]
  print Set[3],'|',Set[4],'|',Set[5]
  print Set[6],'|',Set[7],'|',Set[8]
  Turns = Turns + 1
 else:
  if GameStatus=='Draw':
   print '--------DRAW----------'
  elif GameStatus=='Eddie':
   print '  .........I WIN BETTER LUCK NEXT TIME...................  '
  elif GameStatus=='Player':
   print' *******CONGRADULATION******* '
   print'**********YOU WIN**************'
 
 

#_________________________________________________________________________________________________________________________________________

# HUMANITY DICTIONARY (Summer 2014)
Humanity = [{"User-ID":000, "First Name":"Chinmay", "Last Name":"H?", "Nationality":"India", "Post":"Sole Programmer of Current Code"},
 {"User-ID":001, "First Name":"Killar", "Last Name":"Guy", "Nationality":"Vice City", "Post":"Radical Destroyer"},
 {"User-ID":002, "First Name":"Drethes", "Last Name":"Prisoner", "Nationality":"Russia", "Post":"Psychopath; Lock-Picker"},
 {"User-ID":003, "First Name":"Crazy", "Last Name":"Goat", "Nationality":"Africa??", "Post":"Unique semi-human Specimen"},
 {"User-ID":004, "First Name":"Imadumbo", "Last Name":"Dumbfellow", "Nationality":"Dumboland", "Post":"A Dumbo"},
 {"User-ID":005, "First Name":"Happyman", "Last Name":"Dumbfellow", "Nationality":"Dumboland", "Post":"Much WOW! Such Amaze! So Yay!"}]


#-------------------------------------------------------------------------------------------------------------------------------------------------------
Communes = Humanity
# Useless Game - If you Number matches with the loop. It prints the Name. A useless game.
def UselessGame():
 if raw_input('Want to play a Useless Game? ') == 'Yes':
  for C in Communes:
        M = int(raw_input("User-ID: "))
        if C["User-ID"]== M :
            print C["First Name"], C["Last Name"]
  # First entry should be 0. Next entries consecutive. EG- 3rd Entry = 2.  


#------------------------------------------------------------------------------------------------------
def User():
  Number = int(SplitInPut[1])
  for C in Communes:
    if C["User-ID"] == Number:
      print C["User-ID"], '|',  C["First Name"], C["Last Name"], '|', C["Post"], '|', C["Nationality"]


#-------------------------------------------------------------------------------------------------------
def Search():
 Name = Swatsisaid[1]
 N = 0
 for c in Communes:
  for C in c.values():
   if Name == C:
    N = N + 1
    print c["User-ID"], '|', c["First Name"], c["Last Name"]
 print ' '*26, '|', N, 'Results', '|'


#------------------------------------------------------------------------------------------------------------------
def AllUsers():
    Products = 0
    for C in Communes:
        print C["User-ID"], '|', C["First Name"], C["Last Name"]
        Products = Products + 1
    print ' ' *26, '|', Products, 'Results', '|'


#--------------------------------------------------------------------------------------------------------------
#1 Humanity
#2 Interface
#3 Functions
#4 ToolKit
#5 Run Code
#----------------------------------------------------------------------------------------------------------
Hey()
