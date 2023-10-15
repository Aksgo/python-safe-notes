#Taking the input of a list or a note.
import dataf as dt,os,encryption as ec,sys
from time import sleep
def viewer():
    dt.loader()# loading whole list
    #viewer and finder of note inside loader()
    print("------------------------")
    print("1.Go back to main screen")
    print("2.Go back to list")
    print("3.Exit")
    print("------------------------")
    step=int(input("Enter your choice: "))
    os.system('cls')
    if step==1:
        main()
    elif step==2:
        viewer()
    else:
        sys.exit()#closing the application
def main():# main module
    print("1.Make a new note")# providing options to view notes or create new notes
    print("2.View note list")##
    print("3.Exit")
    a=input("Enter your choice: ")
    if a=="1":# !!!=======if user choose to make new note=========!!!!!!!
        #print("Great choice!!!, a note will be created")
        print("Please wait! Opening a new note")#loading
        sleep(1.5)
        os.system('cls')# screen cleared
        print("==============Whenever you feel like ending your note type 'save' and press enter=============")# accepting input unitl 'save' is typed
        print("===========!User is suggested to write the title initially for easy identification!===========")
        L=[]
        while True:
            c=input()#adding each line inside a list
            if c[-4:]=='save':
                L.append(c[:-4])
                break
            else:
                L.append(c)
                
        
        index=dt.indexer()#finding out the serial number
        n={index:L}#adding the note to dictionary  {'S.no':['notes are here','note2','note3']}
        dt.upload(n)# uploading the dictionary to file 'dataf.dat'
        print("=====File Saved Successfully!! Taking you back! Please Wait=====")
        sleep(3)
        os.system('cls')#clearing the screen and taking back to original screen by calling main()
        main()
    elif a=="2":
        print("...Loading the list...")# animation if possible
        sleep(0.7)
        os.system('cls')
        viewer()
    else:
        sys.exit()



if __name__ == "__main__":
    main()
