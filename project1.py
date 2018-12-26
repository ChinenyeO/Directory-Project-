from pathlib import Path
from shutil import copyfile




def directory(p:Path)->'When user inputs D and a path print all the items in the dir of that path':
        list_of_file=[]
        for x in p.iterdir():
                if x.is_file():
                        list_of_file.append(x)
                        print(x)
        return list_of_file

def directoryR(p:Path)->'When user inputs R and a path print out all items in the dir and the dir dir':
        list_of_file=[]
        for element in p.iterdir():
                list_of_file.append(element)
                list_of_file.sort()
                if element.is_dir():
                        print(element)
                if element.is_dir(): 
                        a = element
                        directoryR((a))
        return list_of_file.sort()

def rec_search(p:Path):
        pathlist = []
        for item in p.iterdir():
                if item.is_file():
                        pathlist.append(item)
                else:
                        pathlist.extend(rec_search(item))
        return pathlist

def listsort(pathlist:list):
        pathlist.sort(key = lambda x:str(x).count('/'))
        for item in pathlist:
                print(item)
        return pathlist
        



def interestingfile(l : list)-> 'Takes all files in directories and consideries then interesting':
        directoryR()



def FirstInput()->'Call both functions D and R':
        commands=['D','R']
        while True:
                line = input().split()

                
                if len(line) == 1 :
                        print('ERROR')
                
                elif line[0] == 'D':
                        return directory(Path(line[1]))
                elif line[0] == 'R':
                        #return directoryR(Path(line[1]))
                        return listsort(rec_search(Path(line[1])))
                elif line[0] not in commands:
                        print('ERROR')
def SecondInput(list_of_file:list)->'Call all second input you want':
        interesting_files=[]
        commands = ['A' , 'N', 'E', 'T']
        while True:
                line = input().split()

##                if line[0] == 'A':
##                        ''' show all inreresting files '''
##                        for item in list_of_file:
##                                print(item)
##                                interesting_files.append(items)
##                        return interesting_files
                if line[0] == 'N' and len(line) == 2:
                        ''' search for files whose names match the name searched for'''
                        for item in list_of_file:
                                p = Path(item)
                                if line[1] == p.parts[-1]:
                                        print(p)
                                        interesting_files.append(p)
                        return interesting_files

        ##        elif line[0] == 'N' and len(line) == 1:
        ##                print('ERROR')
        ##                
                elif line[0] == 'E':
                        ''' search for files with a particular extention ''' 
                        for item in list_of_file:
                                p = Path(item)
                                if line[1][0] != '.':
                                        line[1] = '.' + line[1]
                                        
                                if line[1] == p.suffix:
                                         print(item)
                                         interesting_files.append(items)
                        return interesting_files

                elif line[0] == 'T':
                        ''' search for text files that have certain texts'''
                        for file in list_of_file:
                                if file.suffix == '.txt':
                                        interesting_files.append(str(file))
                        for file in interesting_files:
                                open_file = open(file, 'r')
                        for file_line in open_file:
                                if line[1] in file_line:
                                        print(open_file.name)
                        return interesting_files
                
                        open_file.close()
                else:
                        print('ERROR')

                if line[0] == 'T' and line[1] == '<':
                        '''Search for files that are less than a certain amoount of bytes'''
                        interesting_files=[]
                        for file in list_of_file:
                               f = Path(file)
                               if f.stat().st_size < int(line[2]):
                                        print(f.name)
                                        interesting_files.append(f)
                        return interesting_files

                                      
                if line[0] == 'T' and line[1] == '>':
                        for file in list_of_file:
                                f = Path(file)
                                if f.stat().st_size > int(line[2]):
                                        print(f.name)
                                        interesting_files.append(f)
                        return interesting_files
                
                elif line[0] not in commands:
                        print('ERROR')


        

def third_input(list_of_file:list):
        interesting_files=[]
        commands = ['T','F','D']

        while True:
                line = input().split()


        
                if line[0] == 'F':
                
                        
                        for file in list_of_file:
                                File=Path(file)
                                if File.suffix == '.txt':
                                        interesting_files.append(File)
                        for file in interesting_files:
                                with file.open() as f:
                                        print(f.readline().strip('\n'))
                        break
                
                elif line[0] == 'D' :
                        for file in list_of_file:
                                newpath = Path(str(file) + '.dup')
                                copyfile(file,newpath)
                        break
                                
                elif line[0] == 'T':
                        for file in list_of_file:
                                File = Path(str(file))
                                File.touch(exist_ok=True)
                        break
                elif line[0] not in commands:
                        print('ERROR')
                        
                        
                        

               

        
        

                                
                        
                        

def main()->'Calls the all inputs': 
        orig_list = FirstInput()
        interesting_files = SecondInput(orig_list) 
        third_input(interesting_files)

    
        
                
if __name__ == '__main__':

        main()
        

        


        
        
        
        
      

    
