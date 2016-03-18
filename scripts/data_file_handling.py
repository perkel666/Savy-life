__author__ = 'Perkel'

import os


class FileList():
    def __init__(self):
        """ requires import os"""

        self.file_list = []

        self.file_list = self.update()

    def update(self):
        """ Function first makes a copy of current files list for safety
            and update it with files
        """

        file_list = self.create_list_of_all_game_files()

        return file_list

    def create_list_of_all_game_files(self):

        """ Function to scan all files in root folder and generate list of
            files and asocieted with them filepaths as tuple (filename, filepath).

            With this functions you will be able to have all files names and paths
            in one instance and when you will need to load file you will be able to
            quickly iterate over list without much cpu power unlike using something
            like os.walk(directory) for each individual file which is both slow and
            hard drive intensive.
        """

        list_of_all_files_in_root = []

        for root, directories, filenames in os.walk(os.curdir):
            #for directory in directories:
            #    pass
            for filename in filenames:
                path = os.path.join(root, filename)
                list_of_all_files_in_root.append((filename, path))

        return list_of_all_files_in_root

    def find_path(self, name):

        """ Takes name of the file (ex. file.txt) and iterates over
            list FileIO.file_list returning file-path. List consists of
            tuples (nameofthefile, filepath)
        """

        file_list = self.file_list
        file_path = None
        hits = 0
        multiple_occurrences_list = []

        for filename in file_list:
            if filename[0] == name:
                file_path = filename[1]
                hits += 1
                multiple_occurrences_list.append(filename[1])

        if hits == 1:
            return file_path
        elif hits == 0:
            print 'File : ', name, " doesn't exist in program folder"
        elif hits > 1:
            print 'File : ', name, ' exist in several places in program folders, please rename files'
            print 'List of files :'
            print '--------------'
            for occurence in multiple_occurrences_list:
                print occurence
            print '--------------'
