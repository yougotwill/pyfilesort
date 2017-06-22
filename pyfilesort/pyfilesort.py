# Python Downloads Cleaner
# William Grant
# 26 May 2017

# TODO
# Make sure everything runs smoothly on Linux and Windows
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
"_Books": [".epub", ".mobi"],
"_Documents": [".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json", ".ods", ".log", ".xls"],
"_Videos": [".mkv", ".mp4", ".mov", ".mpeg"],
"_Programs": [".dmg", ".exe", ".sh", ".app", ".pkg"],
"_Zipped": [".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz"],
"_Web": [".html", ".css", ".js"],
"_Scripts": [".py", ".java", ".class", ".sh"]
}

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
                        global folder_count
                        folder_count += 1
                        # print filename + " is a folder"
                        # would try and run process_files(current_folder) and then based on the file contents classify the directory
                        # when classifying the directory if there is another directory inside then ask the user to classify it for you
                        # there should be a flag to allow the user to specify smart directory sorting or manual directory sorting
                        # print "Folder found. Would you like to move " + filename + "? [Y/N]"
                        # flag = raw_input()
                        # if(flag!="N"):
                        #     print "Where would you like to move " + filename + "?"
                        #     flag = raw_input(str(folder_dic.keys()) + "\n")
                        #     for k in folder_dic.keys():
                        #         if(flag==k):
                        #             shutil.move(base_folder + "/"+ filename, base_folder + "/" + k)
                        #             global move_count
                        #             move_count +=1
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