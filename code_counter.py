#-*- coding:utf-8 -*-
'''
Created on 2013-9-2

@author: pkking
'''

import os

class the_code(object):
    '''
    the code class
    '''
        
    def __init__(self):
        '''
        Constructor
        '''
        self.c_file_counter =0
        self.py_file_counter =0
        self.c_file_list = []
        self.py_file_list = [] 
        self.c_line_counter = 0
        self.py_line_counter = 0
        for root_dir,dirs,files in os.walk('.'):
                if(self.is_git_dir(root_dir)):
                    continue
                for this_file in files:
                    tail = os.path.splitext(this_file)
                    if(tail[1] == '.py'):
                        self.py_file_list.append(os.path.join(root_dir, this_file))
                        self.py_file_counter +=1
                    elif(tail[1] == '.c' or tail[1] == '.h'):
                        self.c_file_list.append(os.path.join(root_dir, this_file))
                        self.c_file_counter +=1

    def source_files_count(self, file_type):
        '''
        count code lines for c files
        '''
        if file_type == 'c' or file_type == 'C':
            for c_file in self.c_file_list:
                fobj = open(c_file,'r+')
                lines = fobj.readlines()
                for line in lines:
                    if(';' in line):
                        self.c_line_counter +=1
                fobj.close()
        elif file_type == 'py' or file_type == 'PY' or file_type == 'pY' or file_type == 'Py':
            for py_file in self.py_file_list:
                fobj = open(py_file,'r+')
                lines = fobj.readlines()
                for line in lines:
                    if( '\r\n' in line or '\n' in line or '\r' in line):
                        self.py_line_counter +=1
                fobj.close()
        else:
            print('no this kind source file!')
            exit()
            
    def is_git_dir(self,source_dir):
        '''
        if the dir is a git repo
        '''
        if '.git' == source_dir:
            return True
        else:
            return False
    
    def print_line(self):
        '''
        print the line num
        '''
        if(self.c_file_counter):
            print'there are ' + str(self.c_file_counter) + ' c source files'
            print'the c and h source files lines are :' + str(self.c_line_counter)
        if(self.py_file_counter):
            print'there are ' + str(self.py_file_counter) + ' python source files'
            print'the py source files lines are:' + str(self.py_line_counter)

my_code = the_code()
my_code.source_files_count('c')
my_code.source_files_count('py')
my_code.print_line()
raw_input("Press Enter to continue...")