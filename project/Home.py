import tkinter as tk
from tkinter import * 
from PIL import ImageTk, Image #image processing library - Pillow
from tkinter import messagebox as mb
from csv import *
import os
import webbrowser #high-level interface to display web-based documents
import pickle
import dbm
import json 
import glob
import numpy as np
import matplotlib.pyplot as plt

def center_screen(): #function to center the root window in the center of the screen
	global screen_height, screen_width, x_cordinate, y_cordinate
	screen_width = s1.winfo_screenwidth()
	screen_height = s1.winfo_screenheight()
	x_cordinate = int((screen_width/2) - (window_width/2))
	y_cordinate = int((screen_height/2) - (window_height/2))
	s1.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

s1 = Tk() #creating the root window
s1.title(" PLUM")
#s1.iconbitmap("project/icon.ico")
s1.config(background='RosyBrown1')

s1.resizable(False, False)
window_height = 450
window_width = 800
center_screen() #placing the root window in the screen's center

frame1 = Frame(s1, width= 800, height=80, relief = 'flat', bg="MediumPurple4") #frame to split the root window into sections
frame1.pack(anchor=N)
frame1.pack_propagate(0)
mainl = Label(frame1, text = " PLUM | Please Learn and Understand Menstruation", font=("Times", 20, "bold"), bg="MediumPurple4", fg='white')
mainl.pack(pady = 10)
subti = Label(frame1, text = "A student-led NGO", font =("Times", 16, "bold italic"), bg="MediumPurple4", fg= "firebrick")
subti.pack()

img = ImageTk.PhotoImage(Image.open("project/logo.png")) #adding logo image to root window
label = Label(s1, image = img)
label.pack(pady = 15)

def callback(url): #function to link PLUM's webpage to this gui application using web browser controller
    webbrowser.open_new(url)
 
def closeAb():
    global Ab
    Ab.destroy()
    Ab = None   

def openAbout(): #function to open the about page that describes PLUM
    global Ab
    if Ab is None:
        Ab = Toplevel(s1) #creates a pop-up window and closing a top-level window does not shut down the program
        Ab.title("About PLUM")
        Ab.geometry("1440x900")
        Ab.config(bg="lavender blush")
        try:
            with open('project/about.pickle', 'rb') as pf:
                dict1 = pickle.load(pf) #loading the pickle file containing data about PLUM in dictionary format
                
                str1 = dict1['Mission'] #getting string data from each of the keys
                str2 = dict1['Story']
                str3 = dict1['PLUM?']
                str4 = dict1['partners']
                
                f1 = Frame(Ab, width=1440, height=200)
                f1.config(relief = 'flat', bg= "thistle2")
                f1.pack(anchor=N)
                f1.pack_propagate(0)
                l1 = Label(f1, text = "PLUM's Mission", font=("Times", 28, "bold"), bg="thistle2", fg='maroon').pack(pady=20) 
                l2 = Label(f1, text = str1, font=("Times", 20), bg = "thistle2", fg = 'black').pack(pady= 10)
                link1 = Label(f1, text= 'Link for PLUM Website', fg='blue', bg="thistle2", cursor='hand2')
                link1.pack(pady=10) 
                #using bind function to bind label to hyperlink
                link1.bind("<Button-1>", lambda e: callback("https://plumforall.wixsite.com/plum")) #using lambda function

                l3 = Label(Ab, text = "Our Story", font=("Times", 28, "bold"), bg="lavender blush", fg='maroon').pack(pady = 20)
                l4 = Label(Ab, text = str2, font=("Times", 20), bg = "lavender blush", fg = 'black').pack(pady= 10)
                
                l5 = Label(Ab, text = "Why PLUM?", font=("Times", 28, "bold"), bg="lavender blush", fg='maroon').pack(pady = 20)
                l6 = Label(Ab, text = str3, font=("Times", 20), bg = "lavender blush", fg = 'black').pack(pady= 20)
                
                f2 = Frame(Ab, width=1440, height=220)
                f2.config(relief = 'flat', bg="pale violet red")
                f2.pack(anchor=S)
                f2.pack_propagate(0)
                l7 = Label(f2, text = "Partners", font=("Times", 28, "bold"), bg="pale violet red", fg='maroon').pack(pady = 20)
                l8 = Label(f2, text = str4, font=("Times", 20), bg = "pale violet red", fg = 'black').pack(pady= 10)
                
                pf.close()
                
        except FileNotFoundError():
            print('Pickle file does not exist')
        Ab.protocol("WM_DELETE_WINDOW", closeAb)

def closePj():
    global Pj
    Pj.destroy()
    Pj = None 
           
def openProjects():
    global Pj
    if Pj is None: 
        Pj = Toplevel(s1) #creates pop-up window for projects page
        Pj.title("PLUM's Projects")
        Pj.geometry("1440x900")
        Pj.config(bg='peach puff')
        
        db = dbm.open("project/pdb", 'c') #opens dbm file with projects data in dictionary format
        str1=db['KOICA']
        str2= db['Nuwakot']
        str3= db['Service Nepal']

        l1 = Label(Pj, text = "KOICA: ", font=("Times", 28, "bold"), bg="peach puff", fg='maroon').pack(pady = 20) 
        l2 = Label(Pj, text = str1, font=("Times", 20), bg = 'peach puff', fg = 'black').pack(pady= 10)
        
        f1 = Frame(Pj) #creating a frame to organize the pictures in
        f1.config(bg='peach puff')
        f1.pack()
        i1 = ImageTk.PhotoImage(Image.open("project/plumpics/koica.png"))
        label = Label(f1, image = i1) #placing the first image in the frame
        label.image = i1
        label.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20)
        i2 = ImageTk.PhotoImage(Image.open("project/plumpics/nuwakot.png"))
        lab2= Label(f1, image = i2)#placing the seconf image in the frame
        lab2.image = i2
        lab2.pack(side=LEFT, expand=TRUE, fill=BOTH, pady=20)
        
        l3 = Label(Pj, text = "Nuwakot Project: ", font=("Times", 28, "bold"), bg="peach puff", fg='maroon').pack(pady=10)
        l4 = Label(Pj, text = str2, font=("Times", 20), bg = 'peach puff', fg = 'black').pack(pady= 10)
        
        l5 = Label(Pj, text = "Service Nepal: ", font=("Times", 28, "bold"), bg="peach puff", fg='maroon').pack(pady = 10)
        l6 = Label(Pj, text = str3, font=("Times", 20), bg = 'peach puff', fg = 'black').pack(pady= 10)
        
        btn = Button(Pj, text = "Schooling & Period Statistics", command = openStats, relief=RAISED, highlightbackground= "peach puff")
        btn.pack(pady = 5)
        db.close()
        Pj.protocol("WM_DELETE_WINDOW", closePj)

def openStats(): #function to open bar plot with some statistics that inspired PLUM's work
    barWidth = 0.25
    fig,ax = plt.subplots(figsize =(14, 8)) # returns a figure object and a tuple with axes objects 
    #setting bar heights for each label
    Missing_school = [20, 10, 6, 23, 17]
    Conc_problem = [55, 44, 39, 66, 45]
    Other_issue = [70, 60, 45, 85, 58]
 
    # Setting position of bar on X axis
    br1 = np.arange(len(Missing_school)) #Returns evenly spaced values in given interval.
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
 
    # Make the plot
    plt.bar(br1, Missing_school, color ='r', width = barWidth, edgecolor ='grey', label ='Missing School')
    plt.bar(br2, Conc_problem, color ='g', width = barWidth, edgecolor ='grey', label ='Concentration Problem')
    plt.bar(br3, Other_issue, color ='b', width = barWidth, edgecolor ='grey', label ='Other Issue')
 
    plt.xlabel('Type of Menstrual Item Used', fontweight ='bold', fontsize = 15)
    plt.ylabel('Percentage', fontweight ='bold', fontsize = 15)
    #xticks is to set the current tick (markers denoting data points) locations and labels of the x-axis
    plt.xticks([r + barWidth for r in range(len(Missing_school))],['Cloth', 'Reusable Pads', 'Disposable Pads', 'Tampons', 'No Item'])
    plt.legend()
    ax.set_title('Reported School Problems Related to Menstruation, Three States in India, 2015| From: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6286883/',loc ='left',)
    plt.show()

def closeCt():
    global Ct
    Ct.destroy()
    Ct = None

main_lst=[] #list to save the contact details entered by user
def openContact(): #function to receiver responses from user and for user to get in touch
    global Ct
    if Ct is None:
        Ct = Toplevel(s1)
        Ct.title("Get in Touch!")
        Ct.geometry("480x380")
        Ct.config(bg='light cyan')
        
        def Add():
            lst=[name.get(),contact.get(),comment.get()] #appending the list with the data entered by user
            main_lst.append(lst)
            mb.showinfo("Information","The data has been added successfully - please save it")
            
        def Save():
            with open("data_entry.csv","a+") as file: #writing the contact details into csv file after opening it in append+ mode
                Writer=writer(file)
                Writer.writerow(["Name","Contact","Comment/Query"])
                Writer.writerows(main_lst)
                mb.showinfo("Information","Saved succesfully")
                
        def Clear(): #function to clear the entries
            name.delete(0,END) 
            comment.delete(0,END)
            contact.delete(0,END)
        
        label1=Label(Ct,text="Name: ",padx=20,pady=10, bg='light cyan')
        label2=Label(Ct,text="Contact: ",padx=20,pady=10, bg='light cyan')
        label3=Label(Ct,text="Comment/Query: ",padx=20,pady=10, bg='light cyan')
        label1.grid(row=0,column=0)
        label2.grid(row=1,column=0)
        label3.grid(row=2,column=0)
        #create and add the different entry fields while calling respective functions to add, save, etc
        name=Entry(Ct,width=30,borderwidth=1)
        contact=Entry(Ct,width=30,borderwidth=1)
        comment=Entry(Ct,width=30,borderwidth=1)
        save=Button(Ct,text="Save", bg='light cyan', highlightbackground= 'light cyan', padx=20,pady=10,command=Save)
        add=Button(Ct,text="Add",bg='light cyan', highlightbackground= 'light cyan',padx=20,pady=10,command=Add)
        clear=Button(Ct,text="Clear",bg='light cyan',highlightbackground= 'light cyan', padx=20,pady=10,command=Clear)
        Exit=Button(Ct,text="Exit",bg='light cyan', highlightbackground= 'light cyan',padx=20,pady=10,command=Ct.quit)
        #organize and display everything in the window using grid()
        name.grid(row=0,column=1)
        contact.grid(row=1,column=1)
        comment.grid(row=2,column=1)
        save.grid(row=4,column=1,columnspan=2)
        add.grid(row=3,column=1,columnspan=2)
        clear.grid(row=5,column=1,columnspan=2)
        Exit.grid(row=6,column=1,columnspan=2)
        Ct.protocol("WM_DELETE_WINDOW", closeCt)

def closeGa():
    global Ga
    Ga.destroy()
    Ga = None
    
def openGallery():
    global Ga
    if Ga is None:
        Ga = Toplevel(s1) #creating a pop-up window for the image gallery
        Ga.title("Events & Images")
        Ga.geometry("1440x900")
        Ga.config(bg='cornsilk')
        
        COLUMNS = 4
        image_count = 0
        path = '/Users/sreshtacheekatla/Desktop/Python/project/plumpics'
        
        #repeatedly opening every file in the given path | adding image to the window using grid
        try:
            if os.path.exists(path):
                for infile in glob.glob(os.path.join(path,'*.png')): #using global module to search for all .png files
                    image_count += 1
                    r, c = divmod(image_count-1, COLUMNS)
                    
                    im = Image.open(infile)
                    resized = im.resize((360, 280),Image.LANCZOS)
                    tkimage = ImageTk.PhotoImage(resized)
                    
                    myvar=Label(Ga,image = tkimage)
                    myvar.image = tkimage
                    myvar.grid(row=r,column=c)            
        except:
            print('Path for folder with images not found!')
        Ga.protocol("WM_DELETE_WINDOW", closeGa)
       
    
def openQuiz(): #function to create a quiz window and run a quiz
    Qz = Toplevel(s1)
    Qz.title("Quiz yourself!")
    Qz.config(background="lavender")
    Qz.geometry("1440x900")
    
    class Quiz:
        
        def __init__(self): #call all the functions when initializing object
            self.q_no=0
            self.title()
            self.display_ques()
            self.opt_selected=IntVar() #selection starts with default integer value 0
            self.opts=self.radio_buttons()
            self.display_opt()
            self.buttons()
            self.data_size=len(question) # no of questions
            self.correct=0
            
        def display_result(self):
            wrong_count = self.data_size - self.correct
            correct = f"Correct: {self.correct}"
            wrong = f"Wrong: {wrong_count}"
            score = int(self.correct / self.data_size * 100)
            result = f"Score: {score}%"
            mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")
            
        def check_ans(self, q_no):
            if self.opt_selected.get() == answer[q_no]:
                return True
            
        def next_btn(self):
            if self.check_ans(self.q_no):
                self.correct += 1
            self.q_no += 1
            if self.q_no==self.data_size:
                self.display_result()
                Qz.destroy()
            else:
                self.display_ques()
                self.display_opt()
                
        def buttons(self):
            next_button = Button(Qz, text="Next",command=self.next_btn, width=10,bg="blue",fg="black",font=("ariel",16,"bold"))
            next_button.place(x=650,y=400)
            
            quit_button = Button(Qz, text="Quit", command=Qz.destroy,width=5,bg="black", fg="black",font=("ariel",16," bold"))
            quit_button.place(x= (screen_width-100) ,y=50)
            
        def display_opt(self):
            val=0
            self.opt_selected.set(0)# deselecting the options
            for option in options[self.q_no]: # looping over the options to be displayed for the text of the radio buttons.
                self.opts[val]['text']=option
                val+=1
                
        def display_ques(self):
            q_no = Label(Qz, text=question[self.q_no], width=160, background="lavender",
		    font=( 'ariel' ,16), anchor= 'w' )
            q_no.place(x=70, y=100)
            
        def title(self):
            title = Label(Qz, text="How much do you know about Period Statistics and Stigma?",
		    width=100, bg="light pink",fg="sienna", font=("Comic Sans MS", 24, "bold"))
            title.place(x=2, y=2)
            
        def radio_buttons(self): #function to show radio buttons that has only one selection
            q_list = [] 
            y_pos = 150
            while len(q_list) < 4: #until four radio buttons are places
                radio_btn = Radiobutton(Qz,text=" ",variable=self.opt_selected, value = len(q_list)+1,font = ("ariel",14), background="lavender")
                q_list.append(radio_btn)
                radio_btn.place(x = 100, y = y_pos)
                y_pos += 40
            return q_list
    
    #load quiz data from json file that already has all the questions, options, and answers 
    try:       
        with open('/Users/sreshtacheekatla/Desktop/project/plum_quiz.json') as f:
            data = json.load(f) 
        question = (data['question'])
        options = (data['options'])
        answer = (data[ 'answer'])
        quiz = Quiz() #create an object of Quiz class which initializes the various functions of quiz class 
        f.close()
        
    except FileNotFoundError():
        print('Json file with quiz data does not exist!')

Ab = None  
#About button
btn = Button(s1, text = "About PLUM", command = openAbout, relief=RAISED, highlightbackground= "RosyBrown1")
btn.pack(pady = 5)

Pj = None
#project Button
btn1 = Button(s1, text='Our Projects', command= openProjects, highlightbackground= "RosyBrown1")
btn1.pack(pady = 5)

#Contact Button
Ct = None
btn2 = Button(s1, text = "Contact/Contribute", command = openContact, highlightbackground= "RosyBrown1")
btn2.pack(pady = 5)

Ga = None
#Gallery Button
btn3 = Button(s1, text = "Image Gallery", command = openGallery, highlightbackground= "RosyBrown1")
btn3.pack(pady = 5)

#Quiz Button
btn4 = Button(s1, text = "Quick Quiz", command = openQuiz, highlightbackground= "RosyBrown1")
btn4.pack(pady = 5)

s1.mainloop()