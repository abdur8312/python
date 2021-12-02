import os
def getFileName(PATH):

    #onlyfiles = [f for f in listdir(PATH) if isfile(join(PATH, f))]
    a = []
    x= os.listdir(PATH)
    for i in x:
        if(os.path.isfile(PATH+'\\'+i)):
            a.append(i)
    return(a)
        
PATH = r'C:\Users\abdur\Downloads\New folder\New folder'
filename=getFileName(PATH)
print(filename)
