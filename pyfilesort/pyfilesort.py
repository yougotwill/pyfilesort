# Python Downloads Cleaner
# William Grant
# 26 May 2017

# TODO
# Make sure everything runs smoothly on Linux and Windows
# Classify folders that don't just have one type of file in them - picking where to move a folder is very buggy
    # use a string and concatenate the _folder for each item in the directory. Then check the nnumber of occurences for the _folder in the string. The one with the most occurences is then chosen
# add flag to sort the primary files from the command line i.e. clean dowinloads, desktop, etc.
# make flags work with sys.argv
# Make separate config file that will be read into the program. Will contain folder_dic and folder flag and other possible settings.

# os -  used for operating system manipulation such as reading or writing to a file
# shutil - used for file operations such as move, copy and delete
# sys - provides variables and methods controlled by the interpreter

import os, shutil, sys
from torrentool.api import Torrent # library used to read torrent meta data so the folder can be classified along with the torrent file

# master_folder = "/Users/William/Downloads"
clean_folder = ""
master_folder = "/Users/William/Downloads"
folder_dic = {
"_Books": [".epub", ".mobi"],
"_Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json", ".ods", ".log", ".xls"],
"_Images": [".png", ".jpg", ".jpeg", ".gif", ".xcf", ".stl", ".blend"],
"_Music": [".mp3", ".wav", ".flac", ".m4a", ".ogg", ".mid", ".asd", ".m3u", ".pls", ".alp", ".asx", ".bfxrsound"],
"_Programs": [".dmg", ".exe", ".sh", ".app", ".pkg"],
"_Scripts": [".py", ".java", ".class", ".sh"],
"_Torrents": [".torrent"],
"_Videos": [".mkv", ".mp4", ".mov", ".mpeg"],
"_Web": [".html", ".css", ".js"],
"_Zipped": [".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz"]
}
folder_order = {
"_Images": 1,
"_Music": 2,
"_Torrents": 3,
"_Books": 4,
"_Documents": 5,
"_Videos": 6,
"_Programs": 7,
"_Zipped": 8,
"_Web": 9,
"_Scripts": 10
}

folder_torrent = [] #stores folders of .torrent files that need to be sorted

#stats
move_count = 0
folder_count = 0

# check extension of file and returns matching folder from folder_dic
def get_folder(value):
    for k,v in folder_dic.items():
        # print "value = " + value + " v = " + str(v)
        if value in v: # check if the extension is in this folder list
            return k
    # if extension not found
    return "NA"

# check extension of file and returns matching folder from folder_dic
def get_folder2(value):
    for k,v in folder_order.items():
        # print "value = " + value + " v = " + str(v)
        if value==v: # check if the extension is in this folder list
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

def print_sort_folder_options(): # prints out the _sorting folders with an allocated number flag
    output = ""
    options = len(folder_order)
    for v in range(options):
        output = output + "[" + str(v+1) + "]" + get_folder2(v+1) + " "
    return output

def process_folder(sort_folder, base_folder): #sort_folder is the folder I am classifying
    global move_count
    global folder_torrent
    if(len(folder_torrent) != 0 and sort_folder in str(folder_torrent)): #if the torrent folder array isn't empty and if the directory matches with a .torrent file
        folder_torrent.remove(sort_folder)
        folder = "_Torrents"
        folder_path = base_folder + "/" + folder
        # check if a sorting folder directory exists
        if os.path.exists(folder_path) == False:
            os.mkdir(folder_path)
        #move file to sorting folder
        try:
            shutil.move(base_folder + "/" + sort_folder, folder_path)
            move_count+=1
            # print "moved " + filename + " to " + folder
        except:
            print "\nERROR: Folder transfer error: " + sort_folder + "\n"
    else:
        sort_folder = base_folder + "/" + sort_folder
        if(os.path.isdir(sort_folder)):
            sameExt = True
            previousExt = "" #stores the previous files extension
            for filename in os.listdir(sort_folder):
                # check if filename is not a directory and is a file
                if(not os.path.isdir(sort_folder + "/"+ filename)):
                    if filename.find(".") != -1:
                        ext = get_extension(filename)
                        # print "ext = "
                        if(not ext==".ds_store"):
                            if(previousExt==""):
                                previousExt = ext
                            if(not ext==previousExt): # means the folder cannot be classified easily
                                sameExt = False
                                break
                    # do nothing because it is a sub-directory of the directory we are checking
            if(sameExt): # if we can classify the folder
                folder = get_folder(previousExt)
                # print "folder = " + folder
                if folder!="NA":
                    folder_path = base_folder + "/" + folder
                    # check if a sorting folder directory exists
                    if os.path.exists(folder_path) == False:
                        os.mkdir(folder_path)
                    #move file to sorting folder
                    try:
                        shutil.move(sort_folder, folder_path)
                        move_count+=1
                        # print "moved " + filename + " to " + folder
                    except:
                        print "\nERROR: Folder transfer error: " + sort_folder + "\n"
                # else:
                    # print ext + " file not supported"
            #folder can't be classfied bring up message to make the user classify it themselves
            else:
                print sort_folder + " cannot be sorted. Would you like to move it? [y/n]"
                flag = raw_input()
                if(flag=='y'):
                    print "Where would you like to move " + sort_folder + "?"
                    flag = int(raw_input(print_sort_folder_options()+"\n"))
                    folder = get_folder2(flag)
                    if(flag!="NA"): #should tab this part correctly
                        folder_path = base_folder + "/" + folder
                    # print folder_path
                    shutil.move(sort_folder, folder_path)
                    move_count +=1

def process_files(base_folder):
    dirlist = os.listdir(base_folder) #order the files before the directories
    dirlist.sort(reverse=True)
    for filename in dirlist:
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
                        process_folder(filename, base_folder)

            else:
                transfer_files(filename, base_folder)

def transfer_files(filename, base_folder):
    if filename.find(".") != -1:
        ext = get_extension(filename)
        # torrent file check
        if(ext==".torrent"): #add to torrent watch folder which will be checked when processing directories
            torrent_folder = Torrent.from_file(base_folder + "/" + filename).name.encode('ascii') #convert name property of torrent file to a normal string
            global folder_torrent
            folder_torrent.append(torrent_folder)
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
                global move_count
                move_count+=1
                # print "moved " + filename + " to " + folder
            except:
                print "\nERROR: File transfer error: " + filename + "\n"
        # else:
            # print ext + " file not supported"

def clean_files(clean_folder):
    if(os.path.isdir(clean_folder)):
        print "Processing..."
        print "-------------------"
        process_files(clean_folder)
        print "SUMMARY"
        print "Moved " + str(move_count) + " files"
        print "Folders " + str(folder_count) + " folders"
        print "-------------------"
        flag = raw_input("Quit pyfilesort? [y/n]\n")
        if(flag=='y'):
            print "----end program-----\n"
            sys.exit()
        else:
            main()

    elif(clean_folder == 'c'):
        main()
    else:
        print "\nERROR: Directory doesn't exist\n"
        main()

def main():
    print "----pyfilesort-----\n"
    global clean_folder
    flag = raw_input("Where do you need sorting?\n[1]Downloads\t[2]Desktop\t[3]Documents\t[4]Other\t[q]Quit\n")
    #need to search for directory intelligently
    if(flag == "1"):
        clean_folder = "/Users/William/Downloads"
        clean_files(clean_folder)
    elif(flag == "2"):
        clean_folder = "/Users/William/Desktop"
        clean_files(clean_folder)
    elif(flag == "3"):
        clean_folder = "/Users/William/Documents"
        clean_files(clean_folder)
    elif(flag == "4"):
        clean_folder = raw_input("Enter [c] to cancel\nEnter the file path you want cleaned (e.g. /Users/USERNAME/Downloads):\n")
        clean_files(clean_folder)
    elif(flag == "q"):
        print "----end program-----\n"
        sys.exit()
    else:
        print "\nERROR: Invalid input\n"
        main()

if __name__ == '__main__':
    main()
