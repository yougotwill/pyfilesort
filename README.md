# pyfilesort

*Get your files sorted*

## Description

***Depreciated*** - please note that I am no longer working on this project.

Check out my new project [filesort](https://github.com/yougotwill/filesort) where a lot of further work has been done.

Just a basic program to sort items in a directory.
Please use with caution. I have only tested this on macOS.

Sorts files and folders and puts them into *\_Type* folders for easy access at the top of your directory.

## Prerequisites
Python 2

## Building
Initial setup for pyfilesort
```
make
```

## Running
To run pyfilesort
```
make run
```

## Uninstalling
To cleanup the code directory and remove dependencies
```
make clean
```

## File Classification
Files are classified as follows:

| *_Type* Folder | File Extension                           |
| :------------- | :--------------------------------------- |
| _Books         | ".epub", ".mobi"                         |
| _Documents     | ".pdf", ".txt", ".doc", ".docx", ".ppt", ".pptx", ".md", ".json", ".ods", ".log", ".xls" |
| _Images        | ".png", ".jpg", ".jpeg", ".gif", ".xcf", ".stl", ".blend" |
| _Music         | ".mp3", ".wav", ".flac", ".m4a", ".ogg", ".mid", ".asd", ".m3u", ".pls", ".alp", ".asx", ".bfxrsound" |
| _Programs      | ".dmg", ".exe", ".sh", ".app", ".pkg", ".apk", ".ipa"    |
| _Scripts       | ".py", ".java", ".class", ".sh"          |
| _Torrents      | ".torrent"                               |
| _Videos        | ".mkv", ".mp4", ".mov", ".mpeg"          |
| _Web           | ".html", ".css", ".js"                   |
| _Zipped        | ".zip", ".rar", ".7z", ".tar.gz", ".tar", ".gz" |

## Authors
* **William Grant** - *Current Work* - [yougotwill](https://github.com/yougotwill)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
