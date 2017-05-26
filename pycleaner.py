# Python Downloads Cleaner
# William Grant
# 26 May 2017

# TODO
# For now Torrents will only collect .torrent files eventually it will grab the torrent download as well by name matching with the .torrent file

# os -  used for operating system manipulation such as reading or writing to a file
# shutil - used for file operations such as move, copy and delete
# sys - provides variables and methods controlled by the interpreter

import os, shutil, sys

# master_folder = "/Users/William/Downloads"
master_folder = "/Users/William/Downloads"
folder_dic = {"Images": [".png", ".jpg", ".jpeg", ".gif"], "Music": [".mp3", ".wav", ".flac", ".m4a", ".ogg", ".mid", ".asd", ".m3u", ".pls", ".alp"], "Torrents": [".torrent"], "Books": [".epub", ".mobi"], "Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json"], "Videos": [".mkv", ".mp4", ".mov", ".mpeg", ""], "Programs": [".dmg", ".exe", ".sh"], "Zipped": [".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz"]}

# check extension of file and returns matching folder from folder_dic
def get_folder(value):
    for k,v in folder_dic.items():
        # print "value = " + value + " v = " + str(v)
        if value in v: # check if the extension is in this folder list
            return k
    # if extension not found
    return "NA"

# returns the file extension given a file name
def get_extension(value):
    ext = value[value.index("."):]
    return ext

def process_files():
    for filename in os.listdir(master_folder):
        # check if filename is a file and not a directory
        if(os.path.isdir(master_folder + "/"+ filename)):
            print filename + " is a folder"
        else:
            if filename.find(".") != -1:
                ext =get_extension(filename)
                # print "ext = " + ext
                folder = get_folder(ext)
                # print "folder = " + folder
                if folder!="NA":
                    folder_path = master_folder + "/" + folder
                    # check if a sorting folder directory exists
                    if os.path.exists(folder_path) == False:
                        os.mkdir(folder_path)
                    #move file to sorting folder
                    try:
                        shutil.move(master_folder + "/"+ filename, folder_path)
                        print "moved " + filename + " to " + folder
                    except:
                        print "transfer error: " + filename
                else:
                    print ext + " file not supported"

def main():
    print "Organizing Files..."
    print "-------------------"
    process_files()
    print "-------------------"
    print "Done"

if __name__ == '__main__':
    main()