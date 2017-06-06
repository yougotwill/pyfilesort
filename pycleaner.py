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
master_folder = "/Users/William/Downloads"
folder_dic = {
"Images": [".png", ".jpg", ".jpeg", ".gif"],
"Music": [".mp3", ".wav", ".flac", ".m4a", ".ogg", ".mid", ".asd", ".m3u", ".pls", ".alp", ".asx"],
"Torrents": [".torrent"], "Books": [".epub", ".mobi"],
"Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json"],
"Videos": [".mkv", ".mp4", ".mov", ".mpeg", ""],
"Programs": [".dmg", ".exe", ".sh", ".app"],
"Zipped": [".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz"],
"Web": [".html", ".css", ".js"]
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
    return ext

def process_files(base_folder):
    for filename in os.listdir(base_folder):
        # check if filename is a file and not a directory
        if(base_folder == master_folder):
            if(os.path.isdir(base_folder + "/"+ filename)):
                special = False
                for k in folder_dic.keys():
                    if(filename==k):
                        special = True
                        break
                if(not special):
                    print filename + " is a folder"
            else:
                if filename.find(".") != -1:
                    ext = get_extension(filename)
                    # print "ext = " + ext
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
                            print "moved " + filename + " to " + folder
                        except:
                            print "transfer error: " + filename
                    else:
                        print ext + " file not supported"

def main():
    print "Organizing Files..."
    print "-------------------"
    process_files(master_folder)
    print "-------------------"
    print "Done"

if __name__ == '__main__':
    main()