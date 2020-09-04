# MySQLCSVReader

This program will watch a folder, or a series of folders and track for any new files being added to the folder.



When new files are added to the folder, this program will scan them and see if they are .csv files.

If the file is a csv file, it will add it to a specified MySQL database.



Before adding the file to the specified MySQL database, it will use Pandas in order to sort and organize the data into a way that works well with MySQL imports. 









