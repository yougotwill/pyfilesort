# Python Downloads Cleaner
# William Grant
# 26 May 2017

# TODO
# For now Torrents will only collect .torrent files eventually it will grab the torrent download as well by name matching with the .torrent file
# Classify folders when possible - now ignores download folders


# os -  used for operating system manipulation such as reading or writing to a file
# shutil - used for file operations such as move, copy and delete
# sys - provides variables and methods controlled by the interpreter

import os, shutil, sys

# master_folder = "/Users/William/Downloads"
clean_folder = ""
master_folder = "/Users/William/Downloads"
folder_dic = {
"_Images": [".png", ".jpg", ".jpeg", ".gif", ".xcf", ".stl", ".blend"],
"_Music": [".mp3", ".wav", ".flac", ".m4a", ".ogg", ".mid", ".asd", ".m3u", ".pls", ".alp", ".asx", ".bfxrsound"],
"_Torrents": [".torrent"],
"Books": [".epub", ".mobi"],
"_Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json", ".ods", ".log", ".xls"],
"_Videos": [".mkv", ".mp4", ".mov", ".mpeg", ""],
"_Programs": [".dmg", ".exe", ".sh", ".app", ".pkg"],
"_Zipped": [".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz"],
"_Web": [".html", ".css", ".js"],
"_Scripts": [".py", ".java", ".class", ".sh"]
}

# check extension of file and returns matching folder from folder_dic
def get_folder(value):
    for k,v in folder_dic.items():
        # print "value = " + value + " v = " + str(v)
        if value in v: # check if the extension is in this folder list
            return k
    # if extension not found
    return "NA"

# returns the file extension given a file name
#finds last occurance of "." for extension
def get_extension(value):
    ext = value[value.rfind("."):]
    ext = ext.lower()
    # print "ext " + ext
    return ext

def process_files(base_folder):
    for filename in os.listdir(base_folder):
        # check if filename is a file and not a directory
        if(base_folder == clean_folder):
            if(os.path.isdir(base_folder + "/"+ filename)):
                special = False
                for k in folder_dic.keys():
                    if(filename==k):
                        special = True
                        break
                if(not special):
                    if filename.find(".") != -1:
                        # probably an application container still needs to be sorted
                        # print filename + "is an application container"
                        transfer_files(filename, base_folder)
                    else:
                        print filename + " is a folder"
                        # would try and run process_files(current_folder) and then based on the file contents classify the directory
                        # when classifying the directory if there is another directory inside then ask the user to classify it for you
                        # there should be a flag to allow the user to specify smart directory sorting or manual directory sorting


            else:
                transfer_files(filename, base_folder)

def transfer_files(filename, base_folder):
    if filename.find(".") != -1:
        ext = get_extension(filename)
        folder = get_folder(ext)
        # print "folder = " + folder
        if folder!="NA":
            folder_path = base_folder + "/" + folder
            # check if a sorting folder directory exists
            if os.path.exists(folder_path) == False:
                os.mkdir(folder_path)
            #move file to sorting folder
            try:
                shutil.move(base_folder + "/"+ filename, folder_path)
                # print "moved " + filename + " to " + folder
            except:
                print "transfer error: " + filename
        else:
            print ext + " file not supported"

def clean_files(clean_folder):
    if(os.path.isdir(clean_folder)):
        print "Cleaning up..."
        print "-------------------"
        process_files(clean_folder)
        print "-------------------"
        print "Done"

def main():
    print "Welcome to PyCleaner"
    global clean_folder
    flag = raw_input("Where do you want to clean?\n[D]ownloads\n[De]sktop\n[Doc]umnets\n[O]ther\n")
    #need to search for directory intelligently
    if(flag == "D"):
        clean_folder = "/Users/William/Downloads"
        clean_files(clean_folder)
    elif(flag == "De"):
        clean_folder = "/Users/William/Desktop"
        clean_files(clean_folder)
    elif(flag == "Doc"):
        clean_folder = "/Users/William/Documents"
        clean_files(clean_folder)
    elif(flag == "O"):
        clean_folder = raw_input("Enter the file path you want cleaned:\n")
        clean_files(clean_folder)
    else:
        print "Invalid option please run PyCleaner again"
        sys.exit()

if __name__ == '__main__':
    main()