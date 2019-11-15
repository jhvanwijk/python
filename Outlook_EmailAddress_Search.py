#import win32com.client

#outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

#inbox = outlook.GetDefaultFolder(6) # "6" refers to the index of a folder - in this case,
                                    # the inbox. You can change that number to reference
                                    # any other folder
#messages = inbox.Items
#message = messages.GetLast()
#body_content = message.body
#print body_content

import win32com
import win32com.client
import string
import os

def findFolder(folderName,searchIn):

    try:
        lowerAccount = searchIn.Folders
        for x in lowerAccount:
            if x.Name == folderName:
                print 'found it %s'%x.Name
                objective = x
                return objective
        return None
    except Exception as error:
        print "Looks like we had an issue accessing the searchIn object"
        print (error)
        return None
def main():

    outlook = win32com.client.Dispatch("Outlook.Application")

    ons = outlook.GetNamespace("MAPI")

    #this is the initial object you're accessing, IE if you want to access
    #the account the Inbox belongs too
    one = 'jan-hendrik.vanwijk@moore.co.za'

    #Retrieves a MAPIFolder object for your account 
    #Object functions and properties defined by MSDN at 
    #https://msdn.microsoft.com/en-us/library/microsoft.office.interop.outlook.mapifolder_members(v=office.14).aspx
    Folder1 = findFolder(one,ons)

    #Now pass you're MAPIFolder object to the same function along with the folder you're searching for
    Folder2 = findFolder('Junk E-Mail',Folder1)

    #This call returns a list of mailItem objects referring to all of the mailitems(messages) in the specified MAPIFolder
    messages = Folder2.Items
    
    #Iterate through the messages contained within our subfolder
    for xx in messages:
        try:
           #Treat xx as a singular object, you can print the body, sender, cc's and pretty much every aspect of an e-mail
           #In my case I was writing the body to .txt files to parse...
            print xx.Subject,xx.Sender,xx.Body
           #Using move you can move e-mails around programatically, make sure to pass it a 
            #MAPIFolder object as the destination, use findFolder() to get the object
            #xx.Move(Folder3)


        except Exception as err:
            print "Error accessing mailItem"
            print err       

            
if __name__ == "__main__":
    main()


import win32com.client
import active_directory
session = win32com.client.gencache.EnsureDispatch("MAPI.session")
win32com.client.gencache.EnsureDispatch("Outlook.Application")
outlook = win32com.client.Dispatch("Outlook.Application")
mapi = outlook.GetNamespace('MAPI')
inbox =  mapi.GetDefaultFolder(win32com.client.constants.olFolderInbox)
print '\n'.join(dir(inbox))