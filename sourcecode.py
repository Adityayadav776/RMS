from tkinter import*
import PIL
from PIL import Image,ImageTk
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import sqlite3
import os
class RMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="light blue")
        #==ICONS===============
        self.logo_dash = ImageTk.PhotoImage(file=r"d:/Python/RMS/images/Icon1.png")

        #==TITLE===============
        title=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="White").place(x=0,y=0,relwidth=1,height=50)
        #==Menu/Buttons================
        M_Frame=LabelFrame(self.root,text="Menus",font=("times new roman",15),bg="light cyan")
        M_Frame.place(x=10,y=70,width=1340,height=80)

        btn_course=Button(M_Frame,text="course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_course).place(x=20,y=5,width=200,height=40)
        btn_student=Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_student).place(x=240,y=5,width=200,height=40)
        btn_result=Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_result).place(x=460,y=5,width=200,height=40)
        btn_view=Button(M_Frame,text="View Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.add_report).place(x=680,y=5,width=200,height=40)
        btn_Logout=Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.logout).place(x=900,y=5,width=200,height=40)
        btn_exit=Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor="hand2",command=self.exit_).place(x=1120,y=5,width=200,height=40)

        #==CONTENT_WINDOW IMAGE=======
        self.bg_img=Image.open(r"d:/Python/RMS/images/bg04.jpg")
        self.bg_image=self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_photo=ImageTk.PhotoImage(self.bg_image)

        self.lbl_bg=Label(self.root,image=self.bg_photo).place(x=400,y=180,width=920,height=350)
        
        #==UPDATE_DETAILS====
        self.lbl_course=Label(self.root,text="Total Courses\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#029386",fg="white")
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_student=Label(self.root,text="Total Student\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#FF6347",fg="white")
        self.lbl_student.place(x=710,y=530,width=300,height=100)

        self.lbl_result=Label(self.root,text="Total Result\n[ 0 ]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#DC143C",fg="white")
        self.lbl_result.place(x=1020,y=530,width=300,height=100)

        #==FOOTER===============
        footer=Label(self.root,text="STUDENT RESULT MANAGEMENT SYSTEM\nContact us for any Technical Issue:7895071754",font=("goudy old style",15,),bg="#262626",fg="White").pack(side=BOTTOM,fill=X)
        self.update_details()

#===========Details on dashboad================
    def update_details(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total courses\n[{str(len(cr))}]")

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")

            cur.execute("select * from result")
            cr=cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")


            self.lbl_course.after(200,self.update_details)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to{str(ex)}")



    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

#====Logout Function====================================
    def logout(self):
        op=messagebox.askyesno("Confirm","Do you really want to logout?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")
    def exit_(self):
        op=messagebox.askyesno("Confirm","Do you really want to exit?",parent=self.root)
        if op==True:
            self.root.destroy()









if __name__=="__main__":
    root=Tk()
    obj=RMS(root)
    root.mainloop()