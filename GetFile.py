import easygui
import pandas

def getFile():
    filename = easygui.fileopenbox();
    readF = pandas.read_csv(filename);

    if(filename.endswith('.csv')==False):
        easygui.exceptionbox('Enter valid file','File Error')
        return 'none'
    else:
        return filename
