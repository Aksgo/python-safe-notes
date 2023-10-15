import encryption as ec,sys,os,pickle
from time import sleep

cwd=os.getcwd()
dirc=cwd+'\\data.dat'



''' data storage format:

each line contains one dictionary to loaded and dumped
each dictionary contains the serial number of the respective note as the key
the value of dictionary is a list containing as nested list with each encrypted line as element
the second element of the maine list is the list of decryption values associated with each line respectively

'''

##below is intializing note which is default note in application
wl=['Welcome NOTE', 'Welcome to notes locker v1.0!!', 'You can type your notes here with endless number of lines.', '--PRIVACY--', 'Your notes are kept end-to-end encrypted with our highest security level.', "So keep your notes safe and to decrypt use your decryption key '123456'.", 'THANK YOU for using our application!!!']
############################

def upload(l):#uploading the notes inside the file
    with open(dirc,'ab') as f:
        for i in l:
            txt,enkeys=ec.encrypt(l[i])
        l[i]=[txt,enkeys]
        pickle.dump(l,f)


def indexer():# finiding latest serial number
    try:
        f=open(dirc,'rb')#only read
        con=True
        while con==True:#checking each dictionary for each note
            try:
              data1=pickle.load(f)#reading each dictionary
              for i in data1:
                var=i
            except EOFError:
              break
        var=int(var)
        var+=1
        
        return str(var)
    except FileNotFoundError:#if file is deleted, creating a default wecome note
        var=1#welcome note added to file
        d={str(var):wl}
        with open(dirc,'ab') as f:
            pickle.dump(d,f)
        var+=1    
        return str(var)

def finder(s):#finding a particular note by S.no
    with open(dirc,'rb') as f:# viewing the note
        con=True
        while con==True:#checking each dictionary for each note
            try:
                data1=pickle.load(f)#reading each dictionary
                for i in data1:
                    var=i#extracting the key of dict
                if s==var:#checking if key is same as given s.no
                    if s=='1':
                        note_l=data1[s]#its data1 not data !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        for j in note_l:
                            print(j)
                            flag=0
                    else:
                        note_l=data1[s][0]#storing the the list of lines
                        keys=data1[s][1]#storing the decryption keys
                        for j in note_l:
                            print(j)#print each line of the requested note
                            flag=1
                    con=False
            
                    
                
            except EOFError:
                print("Note not found!")
                flag=0
                break
        #implementing code for key -- 123456
        if flag==1:
            key_d=input("Enter decryption key:")
            if key_d=='123456':#!!!!!!decryption key!!!!!!!!!!!!
                print("---------Decrypting the notes---------")
                for i in range(1,33):# loading bar code
                    sleep(0.1)
                    print('\r',str(i*3)+'% loaded ',end='')
                    print('\r',('■'*i),end='')
                os.system('cls')
                print('\r')
                print("============Your NOTE=============")##decrpyted notes
                print() 
                note_l=ec.decrypt(note_l,keys)#decryption function
                for i in note_l:
                    print(i)
                print("\n")
            else:
                print("Incorrect key!!!")

def loader():# printing the list of notes   
    try:##trying if file exist
        with open(dirc,'rb') as f:#reading the file
            print("------------------Your notes are end-to-end encrypted-------------------")
            con=True
            while con==True:
                try:
                    data1=pickle.load(f)#reading each dictionary
                    for i in data1:
                        if i!='1':
                            keys=data1[i][1]
                            head=data1[i][0]
                            dc_l=ec.decrypt(head,keys)
                            title=dc_l[0]
                        else:
                            title=data1[i][0]
                        if len(title)<15:
                            print(i," : ",title)#printing notes
                        else:
                            print(i," : ",title[:11]+"....")
                except EOFError:#reaching file end
                    break
        ch=input("Enter the note you want to open(or enter 'q' to exit):").lower()#checking if user want exit or view the notes
        if ch=='q':#if exit
            sys.exit()
        else:
            print("...Loading you note...")
            sleep(0.7)
            os.system('cls')
            finder(ch)#running note viewer
    except FileNotFoundError:#else restart (if file not found)
        var=1
        d={str(var):wl}#appending welcome note initially
        with open(dirc,'ab') as f:
            pickle.dump(d,f)
        loader()

def updater(l):######updating the notes by given line
    try:
        f=open(dirc,'rb+')
    except FIleNotFoundError:
        return 'No Records found'
    
    try:
        while True:
            record=pickle.load(f)
            for i in record:
                pass#!!rewrite the code for updation from here
    except:
        pass#!!!rewrite the code for updation from here
    
'''
Welcome NOTE!\nWelcome to notes locker!!\nYou can type your notes here with endless number of lines.\n--PRIVACY--\nYour notes are kept end-to-end encrypted with our highest security level.\nSo keep your notes safe and to decrypt use your decryption key '123456'.\nTHANK YOU for using our application!!!
'''
