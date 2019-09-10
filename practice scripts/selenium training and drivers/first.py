import tkinter as tk
import tkinter.filedialog
import subprocess
from selenium import webdriver

class Create_workspace:
    def __init__(self,root):
        root.title("Workspace creator") # this will assign the title for the top level widget
        root.config(bg='black') # NOT WORKING this will modify the length and width of the top level widget which is root in this case http://effbot.org/tkinterbook/toplevel.htm#Tkinter.Toplevel.config-method
        root.geometry("%dx%d%+d%+d" % (700, 700, 250, 125)) # this will set the boundry of the top level widget
       
        grid_config =0
        while grid_config < 700:
            root.rowconfigure(grid_config, weight=1)
            root.columnconfigure(grid_config,weight=1)
            grid_config+= 1
           
    
       
        """
        ----------LABELS----------
                                    """
        tk.Label(root,text='::This project is still in Development phase::',bg='red').grid(row=0,column=1,columnspan=3,rowspan=10)
        tk.Label(root,text=':: Boring Stuff ::',bg='green').grid(row=11,column=0,columnspan=4,sticky='E,W')
        tk.Label(root,text=':: Developing Tools ::',bg='green').grid(row=11,column=5,columnspan=5,sticky='E,W')
        tk.Label(root,text=':: Important Links::',bg='green').grid(row=50,column=0,columnspan=5,sticky='E,W')
        tk.Label(root,text='Story Number',fg = 'white',bg='black').grid(row=12,column=0,rowspan=2) # Story number label
        tk.Label(root,text='App name', fg = 'white',bg='black').grid(row=14,column=0,rowspan=2)    # App name label
        tk.Label(root,text='story Name',fg = 'white',bg='black').grid(row=16,column=0,rowspan=2)   # story name label
        tk.Label(root,text='Destination Folder',fg = 'white',bg='black').grid(row=18,column=0,rowspan=2) # Destination folder label
        tk.Label(root,text='View Location',fg='white',bg='black').grid(row=0,column=8)
       
        """
        ----------BUTTONS----------
                                    """
        tk.Button( root, text='GET STORY',command = lambda f = 'get_story':self.Url_generator(flag2=f)).grid(row=12,column=3,columnspan=2,rowspan=2,sticky='W') # this button is assigned for the story number label
        tk.Button( root, text='GET APP PAGE',command = lambda f = 'get_app_page':self.Url_generator(flag2=f)).grid(row=14,column=3,columnspan=2,rowspan=2,sticky='W') # this button is assigned for the application name
        tk.Button( root, text='OPEN',command= lambda f = 'destination_folder':self.Open_dialog(flag =f)).grid(row=18,column=3,rowspan=2,sticky='W') # this button is assigned for the destination folder
        tk.Button( root,text='Cal_update',command=self.cal_update).grid(row=40 , column=0 )
        tk.Button( root,text='New Role',command = self.New_role).grid(row=40 , column=1 )
        tk.Button( root, text='OPEN',command= lambda f = 'view_location':self.Open_dialog(flag = f)).grid(row=0,column=10,sticky='W')
        tk.Button( root, text='Calibrations Validator',command=lambda f1='calibrations_validator':self.dev_tools_process(flag1=f1)).grid(row=13,column=9,columnspan=1,sticky='S,W')
        tk.Button( root, text='Diff Tool',command=lambda f1='diff_tool':self.dev_tools_process(flag1=f1)).grid(row=14,column=9,columnspan=1,sticky='S,W')
        tk.Button( root, text='AB Interface Database', command=lambda f1='AB_interface_database':self.dev_tools_process(flag1=f1)).grid(row=15,column=9,columnspan=1,sticky='S,W')
       
       
        """
        ----------ENTRIES----------
                                    """
                                   
        self.story_num = tk.Entry( root, relief='ridge')
        self.app_name = tk.Entry( root, relief='ridge')
        self.story_name = tk.Entry( root, relief='ridge')
        self.destination_folder = tk.Entry(root, relief='ridge')
        self.view_location = tk.Entry(root,relief='ridge')
        self.story_num.grid(row=12,column=1,rowspan=2)
        self.app_name.grid(row=14,column=1,rowspan=2)
        self.story_name.grid(row=16,column=1,rowspan=2,sticky= 'N')
        self.destination_folder.grid(row=18,column=1,rowspan=2,sticky = 'S')
        self.view_location.grid(row=0,column=9)
       
       
       
       
       
       
       
    def Open_dialog(self,flag):
        req_dest = tk.filedialog.askdirectory()
        if flag=='destination_folder':
            self.destination_folder.insert(0,str(req_dest))
        elif flag == 'view_location':
             self.view_location.insert(0,str(req_dest))
             
             
       
    def Populate_list(self):
        self.entry_list = [self.destination_folder.get(),self.app_name.get(),self.story_num.get(),self.story_name.get()]
        return self.entry_list
       
    def cal_update(self):
        tmp_entry_list = self.Populate_list()
        sub_files_list = ['previous csv files','import these files','before importing',
                          'after importing','notes.txt']
        self.Dir_creator(tmp_entry_list,sub_files_list)
    def New_role(self):
        tmp_entry_list = self.Populate_list()
        print(tmp_entry_list[0]=='')
        sub_files_list = ['csv files','upload these first iteration','comments.txt','notes.txt']
        self.Dir_creator(tmp_entry_list,sub_files_list)
       
    def Dir_creator(self,list,sub_files):
        if(list[0]==''or list[2]==''or list[3] == ''):
            print('One or more of the required fields is or are missing please correct it and try again!!!!')
        else:
            raw_Dir= list[0]
            base_folder = "Story"+' '+list[2]+' '+list[3]
       
            """
            This below code creates the base working directory inside the root directory
            """
            cmd = 'cd '+ raw_Dir+'/'+ " && md "+ '"'+base_folder+'"'
            process = subprocess.Popen(cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            stdout, stderr = process.communicate()
            if stderr == stdout:
                print("Base working Directory has been created in the destination folder.Creating the subfiles and folders in the existing base working Directory")
            else:
                print(stderr)
           
            """
            this below code creates the files and folders inside the base working directory
            """
            for x in sub_files:
                test_str = '.txt' in x
                if (test_str == False):
                    cmd = 'cd '+ raw_Dir+'/'+base_folder+ " && md " + '"'+x+'"'
                    process = subprocess.Popen(cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                elif(test_str == True):
                    cmd = 'cd '+ raw_Dir+'/'+base_folder+ " && echo.>"+x
                    process = subprocess.Popen(cmd , stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    
    def dev_tools_process(self,flag1):        
        root_path = self.view_location.get()
        derived_path = "/lib/sdsa_utils/Java/CalibrationTools//"
        final_path = root_path+derived_path
        tools = ['runCalTool.bat','runDifTool.bat']
        if root_path!='':
            if flag1 == 'calibrations_validator':
                cmd = 'new.bat'
                #cmd = 'start cmd.exe /W '+'cd '+ root_path+derived_path+' && '+tools[0]
                print(cmd)
                self.dev_tools_open(cmd)
                #root.destroy()
                
            elif flag1 == 'diff_tool':
                cmd = 'cd '+final_path +' && '+tools[1]
                print(cmd)
            elif flag1 == 'AB_interface_database':
                cmd = 'cd C:/sdviews/sddocs/lib/sd_doc_utils/Java/AbTools// ' + ' && run_query.bat'
                print(cmd)
        else:
            print("you need to provide the view location before accessing the developing tools")
            
    def dev_tools_open(self,cmd):
        #bat_file_info = 'start cmd.exe /k '+'"'+cmd+'"'
        bat_file_info = cmd
        cmd1 = 'echo '+ bat_file_info+' >Temp.bat && Temp.bat && del Temp.bat' 
        p = subprocess.Popen(cmd1,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
        stdout,stderr  = p.communicate()
    def Open_browser(self,url):
            web_instance = webdriver.Chrome()
            web_instance.get(url)
            
    def Url_generator(self,flag2):
        
        if flag2 == 'get_story':
            url = ("https://cateapps.ecorp.cat.com/shell/issues/issues.pl?/issues/list/00006005,detailcard,0000%d" % (int(self.story_num.get())))
        elif flag2== 'get_app_page':
            url = ("https://catedocs.ecorp.cat.com/12/%s_doc/" %(self.app_name.get()))  
        self.Open_browser(url)
      
            
        

       
       
       
       
   
       
       
       
       
       
root = tk.Tk()    
e = Create_workspace(root)


root.mainloop()











"""
gird geometry: http://www.effbot.org/tkinterbook/grid.htm
label documentation: http://effbot.org/tkinterbook/label.htm
entry widget: http://effbot.org/tkinterbook/entry.htm  , https://www.tutorialspoint.com/python/tk_entry.htm
top level geometry:https://www.geeksforgeeks.org/python-geometry-method-in-tkinter/
scrollbar: http://effbot.org/tkinterbook/scrollbar.htm
https://smallguysit.com/index.php/2017/03/11/tkinter-grid-set-default-grid-size/



"""