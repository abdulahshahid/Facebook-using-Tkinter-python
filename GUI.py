import MyFacebook
import Database_Manage
from tkinter import *
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('My facebook.db')
c = conn.cursor()
class MainFrontend:
    def initial(self):
        root = Tk()
        root.geometry("1366x768")
        Label(root,text = "",font = ("Arial",40)).grid(row = 5,column = 0)
        Label(root,text = "Namal Book",font = ("Arial",50,"bold italic"),fg = "#4267B2").grid(row = 180,column = 0)
        Label(text = "Bringing Namalites Together!",font = ("Arial",24,"bold italic")).grid(row = 185,column = 0)
        Label(text = "username",padx = 50,font = ("Arial",20)).grid(row = 78,column = 75)
        self.username = Entry(root)
        self.username.grid(row = 78,column = 5000)
        Label(text = "password",padx = 50,font = ("Arial",20)).grid(row = 79,column = 75)
        self.password = Entry(root)
        self.password.grid(row = 79,column =  5000)
        Button(text = "Login",font = ("Arial",15),fg = "#4267B2",bg = "white",command = lambda:f.call_login(self.username.get(),self.password.get())).grid(row = 82,column = 5000)
        Button(root,text = "forget password?",font = ("Arial",20,"italic"),fg = "#4267B2",bg = "white",command = lambda:f.windyofchangepassword()).grid(row = 85,column = 5000)
        Label(root,text = "New Here?",font = ("Trade Gothic Next HvyCd",30),pady = 20).grid(row = 89,column = 5000)
        Button(text = "Signup",font = ("Arial",15),fg = "#4267B2",bg = "white",command = lambda:f.signup(root)).grid(row = 96,column = 5000)
        root.mainloop()
    def windyofchangepassword(self):
        # windy.destroy()
        root = Tk()
        root.geometry("1366x768")
        root.title("reset password")
        Label(root,text = "Forgot your password? Don't worry Namal Book is here to assist you.\nIts just single step verification process.You just have to verify your email id.",font = ("Arial",20,"italic"),fg = "#4267B2").grid(row = 0,column = 0)
        self.email = Entry(root)
        self.email.grid(row = 2,column = 0)
        Button(root,text = "Continue",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda:f.takenewpassword(self.email.get())).grid(row = 5,column = 0)
        root.mainloop()   
    def takenewpassword(self,email):
        check = False
        c.execute("SELECT Email FROM SIGNUP")
        data = c.fetchall()
        for i in data:
            if i[0] == email:
                check = True
        if check == True:
            f.newpasswordwindy(email)
        else:
            messagebox.showerror("error","email does not matched")
            f.windyofchangepassword()
    def newpasswordwindy(self,email):
        # if decide == 1:
        #     windy.destroy()
        root = Tk()
        root.geometry("1366x768")
        Label(root,text = "Just one step away! Choose your new password...",font = ("Arial",30,"italic"),fg = "#4267B2").grid(row = 0,column = 0)
        self.password = Entry(root)
        self.password.grid(row = 2,column = 0)
        Button(root,text = "Change password",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda:f.putpassword(self.password.get(),email)).grid(row = 7,column = 0)
        root.mainloop()
    def putpassword(self,password,email):
        y = Database_Manage.reset_password(password,email)
        if y == True:
            f.initial()
        if y == False:
            f.newpasswordwindy("root",0)
    def call_login(self,username,password):
        x = MyFacebook.u.login(username,password)
        if x == True:
            messagebox.showinfo("notification", "successfully logged in")
            h.Mainpage(username)
        if x == False:
            messagebox.showerror("login failed","Invalid username or password")
    def signup(self):
        # windy.destroy()
        root = Tk()
        root.geometry("1366x768")
        Label(root, text = "Signup",padx =80,pady = 70,font = ("Arial",60,"bold italic"),fg = "#4267B2").grid()
        Label(root,text = "Username",padx = 100,font = ("Arial",15)).grid(row = 78,column = 75)
        Label(root,text = "Password",padx = 100,font = ("Arial",15)).grid(row = 79,column = 75)
        Label(root,text = "Email",padx = 100,font = ("Arial",15)).grid(row = 80,column = 75)
        Label(root,text = "City",padx = 100,font = ("Arial",15)).grid(row = 81,column = 75)
        username = Entry(root)
        username.grid(row = 78,column = 76)
        password = Entry(root)
        password.grid(row = 79,column =76)
        email = Entry(root)
        email.grid(row = 80,column = 76)
        city = Entry(root)
        city.grid(row = 81,column = 76)
        # Label(root,text = "Gender",padx = 100,font = ("Arial",15)).grid(row = 82,column = 75)
        def call_signup():
            if len(username.get())<4:
                messagebox.showerror("error", "username should contain atleast 4 characters.")
            if len(password.get())<4:
                messagebox.showerror("error", "password should contain atleast 4 characters.")
            if len(username.get())>=4 and len(password.get())>=4:
                x = Database_Manage.checkuser(username.get())
                if x == True:
                    messagebox.showerror("error", "username name not available")
                else:
                    MyFacebook.u.signup(username.get(), password.get(),email.get(),city.get())
                    messagebox.showinfo("notification", "account created successfully")
                    h.Mainpage(root,username.get())
        Button(root,text = "Signup",font = ("Arial",15),fg = "#4267B2",command = call_signup).grid(row = 85,column = 76)
        root.mainloop()
class HomePage:
    def checkcomment(self,post,comment,username):
        if len(comment) ==0 :
            messagebox.showerror("error","write something to add comment")
        else:
            Database_Manage.addcomments(post,comment,username)
    def Mainpage(self,username):
        self.username = username
        def checkpost(post,username):
            if len(post) == 0:
                messagebox.showerror("error","write something to post")
            else:
                MyFacebook.p.MakeNewPOST(post,username,value.get())
                
        y,t_comments,comments,commentsby,comments_by,fulldata = [],[],[],[],[],[]
        # windy.destroy()
        root = Tk()
        root.geometry("1366x768")
        root.title("Home")
        mymenu = Menu(root)
        mymenu.add_command(label = "friends",command = lambda:fr.friends(self.username))
        mymenu.add_command(label = "notifications",command =lambda:n.notifications(self.username))
        mymenu.add_command(label = "Pages",command = lambda:p.initializepagewindy(self.username))
        mymenu.add_command(label = "setting",command = lambda:s.setting(self.username))
        mymenu.add_command(label = "search user",command = lambda:se.searchuserinitialpage(self.username))
        mymenu.add_command(label = "messenger",command = lambda:m.messenger(self.username))
        mymenu.add_command(label = "Profile",command = lambda:pr.profile_page(self.username))
        mymenu.add_command(label = "Back",command = quit)
        root.config(menu =mymenu)
        Label(root,text = "Write Something to add new post",font = ("Arial",20,"bold")).grid(row = 0,column = 0)
        new_p = Entry(root)
        new_p.grid(row = 0,column = 1)
        value = IntVar()
        Button(root,text = "Post",font = ("Arial",10,"bold"),bg = "#4267B2",fg = "white",command = lambda : checkpost(new_p.get(),self.username)).grid(row = 1,column = 2)
        fri =  Database_Manage.give_friends(self.username)
        data = Database_Manage.give_posts(fri)
        if len(data)!= 0:
            for i in data:
                for j in i:
                    fulldata.append(j)
                    y.append(j[1])
        for k in y:
            c.execute("SELECT Comment,CommentBy FROM Comments WHERE Post = ?",(k,))
            da = c.fetchall()
            for l in da: 
                t_comments.append(l[0])
                commentsby.append(l[1])
            comments_by.append(commentsby)
            comments.append(t_comments)
            t_comments = []
            commentsby = []
        if len(y)!= 0:
            Label(root,text =fulldata[-1][0]+" added post "+y[-1]+" on "+fulldata[-1][3]+" at "+fulldata[-1][4],font = ("Arial",20,"italic")).grid()
            if len(comments)!= 0:
                comen = comments[-1]
                comenby = comments_by[-1]
                comen,comenby = comen[::-1],comenby[::-1]
                for i in range(len(comen)):
                    Label(root,text = comenby[i]+" added comment :"+comen[i]).grid()
            if len(comments) == 0:
                Label(root,text = "Be first to comment",font = ("Arial",20,"italic")).grid()
            comment = Entry(root)
            comment.grid()
            Button(root,text = "Comment",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda post = y[-1]:h.checkcomment(post,comment.get(),self.username)).grid()
            Button(root,text = "next",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda: h.showposts(-2,y,fulldata,comments,comments_by)).grid()
        if len(y) == 0:
            Label(root,text = "No activity to show here probably you have no friend, or no activity by your friend/s.",font = ("Arial",20),fg = "#4267B2").grid()
        root.mainloop()
    def showposts(self,postcounter,allposts,data,comments,commenter):
        root = Tk()
        root.geometry("1366x768")
        # windy.destroy()
        if postcounter == -1:
            h.Mainpage(self.username)
        if postcounter>=(0-len(allposts)):
            comen = comments[postcounter]
            comenby = commenter[postcounter]
            comen,comenby = comen[::-1],comenby[::-1]
            Label(root,text =data[postcounter][0]+" added post "+allposts[postcounter]+" on "+data[postcounter][3]+" at "+data[postcounter][4],font = ("Arial",20,"italic")).grid()
            if len(comen)!= 0:
                for i in range(len(comen)):
                    Label(root,text = comenby[i]+" added comment :"+comen[i]).grid()
            if len(comen) == 0:
                Label(root,text = "Be first to add comment",font = ("Arial",20,"italic")).grid()
            comment = Entry(root)
            comment.grid()
            Button(root,text = "Comment",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda post =allposts[postcounter] :Database_Manage.addcomments(post,comment.get(),f.username.get())).grid()
            Button(root,text = "Next Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda:h.showposts(postcounter-1,allposts,data,comments,commenter)).grid()
            Button(root,text = "Previous Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda:h.showposts(postcounter+1,allposts,data,comments,commenter)).grid()
        if postcounter <0-len(allposts):
            Button(root,text = "Back",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda:h.Mainpage(self.username)).grid()
            Label(root,text = "You are all caught up",font = ("Arial",50)).grid()
        root.mainloop()        
class Messages:
    def messenger(self,user):
        rercent_chat = []
        import sqlite3
        con = sqlite3.connect("My Facebook.db")
        c = con.cursor()
        def searchrespond(searcher):
            notshow = []
            notshow1 = []
            blockedbyyou = False
            blockedbyother = False
            c.execute("SELECT Blocked,Blocker FROM Black_list")
            dat = c.fetchall()
            for j in dat:
                notshow1.append(j[0])
                notshow.append(j[1])
            for i in range(len(notshow)):
                if notshow[i] == user and notshow1[i] == searcher:
                    blockedbyyou = True
                elif notshow[i] == searcher and notshow1[i] == user:
                    blockedbyother = True
            y = Database_Manage.check_existence(searcher)
            if y == True and searcher != user and (blockedbyother == False and blockedbyyou == False):
                windychat(searcher)
            if blockedbyyou == True:
                messagebox.showwarning("error","blocked by you")
            if blockedbyother == True:
                messagebox.showerror("error","no user found")
            if y  == user:
                messagebox.showwarning("error","cannot send message to yourself")
            if y == False:
                messagebox.showwarning("error","no such user")
        def sendmessage(sender,receiver,message):
            if len(message)!=0:
                Database_Manage.send_message(sender,receiver,message)
            if len(message)==0:
                messagebox.showwarning("Messenger","Nikal Bhosdi k")
        def windychat(name):
            counter2 = -1
            counter3 = 60
            allchat = []
            canvas3 = Canvas(root,width = 1108,height =800,bg = "#73F6F8")
            canvas3.place(x =400,y =100)
            c.execute("SELECT chat FROM CurrentChat WHERE Person1 = ? AND Person2 =?",(user,name))
            data = c.fetchall()
            if len(data)!=0:
                for i in data:
                    allchat.append(i[0])
            print(allchat)
            if len(allchat)==0:
                    canvas3.create_text(400,50,fill = "white",font = "Arial 20 italic",text = "No new message from "+name)
            while counter2 > -7 and counter2 >= (0-len(allchat)):
                    Label(canvas3,text =allchat[counter2],font = ("Eras Light",20)).place(x = 300,y = counter3)
                    counter2-=1
                    counter3+=40

                
            canvas3.create_text(400,20,fill = "white",font = "Arial 30 italic",text = "Messages From "+name)
            canvas3.create_text(100,610,fill = "#4267B2",font = "Arial 36",text = "Chat")
            message = Entry(canvas3,font = "Arial 15 bold",width = 40)
            message.place(x = 150,y =600)
            Button(canvas3,text = "send message",bg = "#4267B2",fg = "white",font = ("Arial",15,"italic"),command = lambda:sendmessage(name,user,message.get())).place(x = 600,y = 590)
        # windy.destroy()                
        root= Tk()
        root.geometry("1366x768")
        counter = 100
        counter1 = 0
        canvas = Canvas(root, width=1768, height=100, bg = "#4267B2")
        canvas.place(x = 0,y = 0)
        canvas.create_text(660,50,fill="white",font="Times 20 italic bold",
                                text=" Welcome to Messenger")
        E = Entry(canvas,font = ("Arial",15))
        E.place(x = 150,y = 20)
        canvas.create_text(70,30,fill="white",font="Times 20 italic bold",
                                text="Search User")
        Button(canvas,text = "search",bg = "#4267B2",fg = "white",font = ("Arial",15,"italic"),command = lambda:searchrespond(E.get())).place(x = 200,y = 50)
        Button(root,text = "Back to Home",bg = "#4267B2",fg = "white",font = ("Arial",15,"italic"),command = lambda:h.Mainpage(user)).place(x = 1000,y = 20)
        canvas2 = Canvas(root,width = 400,height= 800,bg = "#73DCF8")
        canvas2.place(x = 0,y=100)
        canvas2.create_text(180,40,fill = "white",font = ("Arial",30,"bold italic"),text = "Recent Chat")
        c.execute("SELECT Person1 FROM ChatPerson WHERE Person2 = ?",(user,))
        data = c.fetchall()
        if len(data)!=0:
            for i in data:
                rercent_chat.append(i[0])
        rercent_chat = list(set(rercent_chat))
        rercent_chat= rercent_chat[::-1]
        if len(rercent_chat)==0:
            canvas2.create_text(150,100,fill = "Black",font = ("Arial",20,"bold italic"),text = "No recent chat to show")
        else:    
            while counter1<7 and counter1 < len(rercent_chat):
                Button(canvas2,text = rercent_chat[counter1],bg ="white",font = ("Arial",20),command = lambda name = rercent_chat[counter1]:windychat(name)).place(x = 20,y =counter)
                counter+=60
                counter1+=1
        
        root.mainloop()
class Friends:
    def addfriend(self,username):
        def search():
            import sqlite3
            conn = sqlite3.connect('My facebook.db')
            c = conn.cursor()
            y = Database_Manage.check_existence(x.get())
            z = Database_Manage.give_friends(self.username)
            w = Database_Manage.check_duality(self.username,x.get())
            notshow = []
            notshow1 = []
            blockedbyyou = False
            blockedbyother = False
            c.execute("SELECT Blocked,Blocker FROM Black_list")
            dat = c.fetchall()
            for j in dat:
                notshow1.append(j[0])
                notshow.append(j[1])
            for i in range(len(notshow)):
                if notshow[i] == self.username and notshow1[i] == x.get():
                    blockedbyyou = True
                elif notshow[i] == x.get() and notshow1[i] == self.username:
                    blockedbyother = True
            if (y == True) and (x not in z) and (x != self.username) and (w == False) and (blockedbyother == False and blockedbyyou == False):
                c.execute("INSERT INTO Friends_Notifications VALUES(?,?,?)",(x.get(),'Friend',self.username))
                c.execute("INSERT INTO ALL_Notifications VALUES(?,?,?)",(x.get(),'Friend',self.username))
                messagebox.showinfo("sent","request to"+x.get()+'sent')
                conn.commit()
            if blockedbyyou == True:
                messagebox.showwarning("error","blocked by you")
            if blockedbyother == True:
                messagebox.showerror("error","no user found")
            else:
                messagebox.showerror("error","no such user found")
        # windy.destroy()
        self.username = username
        self.root = Tk()
        self.root.geometry("1366x768")
        self.root.title("Discover New Friend")
        Label(self.root,text = "Add friend to your friend lists",font = ('Comic Sans MS', 12, 'bold italic')).grid(row = 0,column = 1)
        Label(self.root,text = "enter username").grid(row = 1,column = 1)
        x = Entry(self.root)
        x.grid(row = 1,column = 2)
        Button(self.root,text = "search",command = search).grid(row = 4,column = 5)
        Button(self.root,text = "Back",command = lambda:fr.friends(self.username),font = ("Arial","20"),fg = "#4267B2",bg = "white").grid(row = 10,column = 8)
        self.root.mainloop()
    def friends(self,username):
        self.username = username
        self.root = Tk()
        m1 = Menu(self.root)
        self.root.geometry("1366x768")
        # windy.destroy()

        self.root.title("Friends")
        m1.add_command(label = "add friend",command = lambda:fr.addfriend(self.username))
        m1.add_command(label = "view friends requests",command = lambda:fr.seefriendsrequests(self.username)) 
        m1.add_command(label = "Back",command = lambda:h.Mainpage(self.username)) 
        self.root.config(menu =m1)
        friends = MyFacebook.fr.friends_list(self.username)
        if len(friends)!=0:
            Label(self.root,text = "Here is your friends list",font = ('Arial', 30,"italic"),fg = "#4267B2").grid(row = 0,column = 0)
            for i in range(len(friends)):
                Label(self.root,text = friends[i],font = ("Arial",20)).grid(row = i+1,column = 0)
                Button(self.root,text = "Unfriend",command= lambda k = friends[i]: Database_Manage.unfriend(k,self.username)).grid(row = i+1,column = 2)
        self.root.mainloop()
    def printnothing(self,sender,receiver):
        c.execute("DELETE FROM Friends_Notifications WHERE Receiver = ? AND Sender = ?",(receiver,sender,))
        conn.commit()
        messagebox.showinfo("removed","request removed")
    def seefriendsrequests(self,username):
        self.username = username
        counter = 0
        x = MyFacebook.fr.Notifications_friend(self.username)
        root = Tk()
        root.title("Friend Requests")
        root.geometry("1366x768")
        # windy.destroy()

        Button(root,text = "Back",command = lambda:fr.friends(self.username),font = ("Arial","20"),fg = "#4267B2",bg = "white").grid(row = 10,column = 8)

        if x == []:
            Label(root,text = "No new friend request").grid(row = 0,column = 0)
        if x!= []:
            for i in x:
                Label(root,text = i+" sent you a friend request ").grid(row = counter,column = 0)
                Button(root,text = "Accept",command = lambda k = i:Database_Manage.enrol_friend(k,self.username)).grid(row = counter+1,column = 0)
                Button(root,text = "Cancel",command = lambda k = i:fr.printnothing(k,self.username)).grid(row = counter+1,column = 1)
            counter+=1
        root.mainloop()
class Notifications:
    f_notify,comm_nitify,post_notify,comment_notify,counter = [],[],[],[],3
    def notifications(self,username):
        self.username = username
        self.root = Tk()
        m1 = Menu(self.root)
        self.root.geometry("1366x768")
        # windy.destroy()

        self.root.title("Notifications")
        Button(self.root,text = "Back",font = ("Arial",20,"bold"),fg= "#4267B2",bg = "white",command = lambda:h.Mainpage(self.username)).grid(row = 10,column = 9)
        m1.add_command(label = "Back",command = lambda:h.Mainpage(username))
        self.root.config(menu =m1)
        notif = c.execute("SELECT * FROM ALL_Notifications WHERE Receiver = ?",(self.username,))
        for i in notif:
            if i[1] == "Friend":
                n.f_notify.append(i[2])
            elif i[1] == "Comment":
                n.comm_nitify.append(i[2])
            elif i[1] == "Comment":
                n.comment_notify.append(i[2])
        c.execute("SELECT POST,POSTEDBY FROM Notifications_Posts WHERE Receiver = ?",(username,))
        noti_post = c.fetchall()
        for i in noti_post:
            n.post_notify.append(i[1]+" added a new post "+i[0])        
        if len(n.comm_nitify)+len(n.f_notify)+len(n.comm_nitify) != 0:
            Label(self.root,text = "You are seeing Notifications of POSTS, FRIENDS REQUESTS & COMMENTS",font = ("Arial",24,"bold"),fg = "#4267B2").grid(row= 0,column = 0)
            for i in n.f_notify:
                Label(self.root,text = i+" sent you friend request ",font = ("Arial",20)).grid(row= n.counter,column = 0)
                n.counter+=1
            for j in n.comm_nitify:
                Label(self.root,text = j+" Commented on post in Page",font = ("Arial",20)).grid(row= n.counter,column = 0)
                n.counter+=1
            for k in n.post_notify:
                Label(self.root,text = k,font = ("Arial",20)).grid(row= n.counter,column = 0)            
                n.counter+=1
            for l in n.comment_notify:
                Label(self.root,text = k+"Commented on your post",font = ("Arial",20)).grid(row= n.counter,column = 0)            
                n.counter+=1
            # Button(self.root,text = "  Mark All as Read     ",command =lambda: Database_Manage.deleteNotifications(self.username)).grid(row = 1,column =0)
        if len(n.comm_nitify)+len(n.f_notify)+len(n.comm_nitify) == 0:
            Label(self.root,text = "No new Notification").grid(row = 0,column = 0)
        
        self.root.mainloop()
class Search:
    def searchuserinitialpage(self,username):
        self.username = username
        root = Tk()
        root.geometry("1366x768")
        # windy.destroy() 
        root.title("Search User")
        Label(root,text = "Enter username",font = ("Arial",20,"italic")).grid(row = 0,column =0)
        name = Entry(root)
        name.grid(row = 0,column = 1)
        Button(root,text = "Search",command = lambda:search_user(name.get())).grid(row = 1,column = 1)
        Button(root,text = "Back",command = lambda:h.Mainpage(root,self.username)).grid(row = 50,column = 6)
        
        def search_user(search_u):
            counter = 2
            y = Database_Manage.search_user(search_u,self.username)
            if y == 0:
                Label(root,text="No user found with username: "+search_u,font = ("Arial",20,"italic")).grid(row = counter,column=1)
            if y !=0:
                Label(root,text = "username: "+y[0],font = ("Arial",20,"italic")).grid(row = counter,column=0)
                counter+=1
                Label(root,text = "Email Address: "+y[2],font = ("Arial",20,"italic")).grid(row = counter,column=0)
                counter+=1
                Label(root,text= "City: "+y[3],font = ("Arial",20,"italic")).grid(row = counter,column=0)
                counter+=1
                y = Database_Manage.give_friends(self.username)
                w = Database_Manage.check_duality(self.username,search_u)
                if w == True:
                    Label(root,text = "Requested").grid(row = counter+1,column = 3)
                if w ==False and search_u not in y:
                    Button(root,text = "Add Friend",command = lambda:se.sendrequest(username,search_u)).grid(row = counter,column = 4)
                if search_u in y:
                    Label(root,text = "Friend").grid(row = counter+2,column =3)
    def sendrequest(self,username,search_u):
        import sqlite3
        conn = sqlite3.connect('My facebook.db')
        c = conn.cursor()
        z = Database_Manage.give_friends(username)
        w = Database_Manage.check_duality(username,search_u)
        notshow = []
        notshow1 = []
        blockedbyyou = False
        blockedbyother = False
        c.execute("SELECT Blocked,Blocker FROM Black_list")
        dat = c.fetchall()
        for j in dat:
            notshow1.append(j[0])
            notshow.append(j[1])
        for i in range(len(notshow)):
            if notshow[i] == username and notshow1[i] == search_u:
                blockedbyyou = True
            elif notshow[i] == search_u and notshow1[i] ==username:
                blockedbyother = True
                
        # print(z,w,blockedbyyou,blockedbyother)
        if (search_u not in z) and (w == False) and (blockedbyother == False and blockedbyyou == False):
            c.execute("INSERT INTO Friends_Notifications VALUES(?,?,?)",(search_u,'Friend',self.username))
            c.execute("INSERT INTO ALL_Notifications VALUES(?,?,?)",(search_u,'Friend',self.username))
            messagebox.showinfo("sent","request to"+search_u+'sent')
            conn.commit()
        if blockedbyyou == True:
            messagebox.showwarning("error","blocked by you")
        if blockedbyother == True:
            messagebox.showerror("error","no user found")
        else:
            messagebox.showerror("error","no such user found")
        if w == True:
            messagebox.showerror("Friend","Request already sent")
class Setting:
    def setting(self,username):
        self.username = username
        self.root = Tk()
        self.root.geometry("1366x768")
        # windy.destroy()
        self.root.title("Setting")
        settingbar = Menu(self.root)
        settingbar.add_command(label = "View blocke users",command = lambda:s.viewblockusers(self.username))
        settingbar.add_command(label = "Block any user",command = lambda:s.blockanyuser(self.username))
        self.root.config(menu = settingbar)
        Button(self.root,text = "Back",font = ("Arial",20,"bold"),fg= "#4267B2",command = h.Mainpage(self.username)).grid(row = 10,column = 9)
        self.root.mainloop()
    def viewblockusers(self,username):
        self.username = username
        root = Tk()
        root.title("Black List")
        root.geometry("1366x768")
        # windy.destroy()
        blckusers = MyFacebook.u.view_black_list(self.username)
        Button(self.root,text = "Back",font = ("Arial",20,"bold"),fg= "#4267B2",command = lambda:s.setting(self.username)).grid(row = 10,column = 9)
        if len(blckusers) != 0:
            Label(root,text = "Users blocked by you are shown below",font = ('Arial',30, 'bold')).grid(row = 0,column = 0)
            for i in range(len(blckusers)):
                Label(root,text = blckusers[i]).grid(row  = i+1,column = 0)
                Button(root,text = "Unblock",command =lambda p = blckusers[i] : Database_Manage.unblock_user(p)).grid(row = i+1,column =2 )
        else:
            Label(root,text = "No user blocked by you.",font = ('Arial',30, 'bold')).grid(row = 0,column = 0)
        root.mainloop()
    def blockanyuser(self,username):
        self.username = username
        root = Tk()
        root.title("Block User")
        root.geometry("1366x768")
        # windy.destroy()
        Button(self.root,text = "Back",font = ("Arial",20,"bold"),fg= "#4267B2",command = lambda:s.setting(self.username)).grid(row = 10,column = 9)
        Label(root,text = "username").grid(row = 0,column =0)
        b = Entry(root)
        b.grid(row = 0,column =1)
        Button(root,text = "Block",command =lambda:MyFacebook.u.block_any_user(self.username,b.get())).grid(row = 1,column = 0)
        root.mainloop()
class Page:
    def checkpost(self,post,pagename,username):
            if len(post) == 0:
                messagebox.showerror("error","write something to post")
            else:
                MyFacebook.pa.MakeNewPOST(post,pagename,username)
    def checkcomment(self,post,comment,username,pagename):
        if len(comment) ==0 :
            messagebox.showerror("error","write something to add comment")
        else:
            Database_Manage.addcommentinPage(post,comment,username,pagename)
    def GUIofjoinedPage(self,pagename):
        # windy.destroy()
        counter= 2
        root = Tk()
        root.geometry("1366x768")
        Label(root,text = "Write Something").grid(row = 1,column = 0)
        new_p = Entry(root)
        new_p.grid(row = 1,column = 1)
        Button(root,text = "Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda : p.checkpost(new_p.get(),pagename,self.username)).grid(row = 1,column = 2)
        Label(root,font = ('Arial', 16, 'bold'), text = "This Page was created by "+Database_Manage.givepagesadmin(pagename)).grid(row = 0,column = 0)
        Button(root,text = "Back to home page",font=('Arial', 16, 'bold'),bg = "#4267B2",fg = "white",command = lambda:p.initializepagewindy(self.username)).grid(row = 1366,column = 0)
        x,y,comments,t_comments,b_comments,commentsby= [],[],[],[],[],[]
        c.execute("SELECT * FROM Page_Posts WHERE Pagename = ?",(pagename,))
        data = c.fetchall()        
        for i in data:
            x.append(i[2])
            y.append(i[0])
        for i in y:
            c.execute("SELECT * FROM Page_Comments WHERE Post = ?",(i,))
            da = c.fetchall()
            for k in da: 
                t_comments.append(k[2])
                b_comments.append(k[3])
            comments.append(t_comments)
            commentsby.append(b_comments)
            t_comments = []
            b_comments = []
        if len(y)!= 0:
            Label(root,font = ('Arial', 12, 'bold'),text = x[-1]+" posted "+y[-1]+" on "+data[-1][3]+" at "+data[-1][4]).grid(row = counter,column = 0)
            comen = comments[-1]
            comenby = commentsby[-1]
            counter += 1
            if len(comen)!= 0:
                for j in range(len(comen)):
                    Label(root,text = comenby[j]+" commented "+comen[j],font =("Arial",20) ,padx = -26).grid(row =counter,column = 2) 
                    counter+= 1
                
            comment = Entry(root)
            comment.grid(row = counter,column = 0)
            Button(root,text = "Comment",command = lambda post = y[-1]:p.checkcomment(post,comment.get(),self.username,pagename)).grid(row =  counter,column =1)
            Button(root,text = "Next Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda: p.showposts(-2,y,x,comments,commentsby,data,pagename)).grid(row = 1700,column = 0)
            counter+= 1
        if len(y) == 0:
            Label(root,text = "No activity to show here.").grid(row = counter,column =0)
        root.mainloop()
    def showposts(self,postcounter,allposts,postby,comments,commenter,data,pagename):
        root = Tk()
        root.geometry("1366x768")
        # windy.destroy()
        Button(root,text = "Back to home page",font=('Arial', 16, 'bold'),bg = "#4267B2",fg = "white",command = lambda:p.initializepagewindy(self.username)).grid(row = 1366,column = 0)
        if postcounter == -1:
            p.GUIofjoinedPage(root,pagename)
        if postcounter>=0-len(allposts):
            comen = comments[postcounter]
            comenby = commenter[postcounter]
            comen,comenby = comen[::-1],comenby[::-1]
            Label(root,text =postby[postcounter]+" added post "+allposts[postcounter]+" on "+data[postcounter][3]+" at "+data[postcounter][4],font = ("Arial",20,"italic")).grid()
            if len(comen)!= 0:
                for i in range(len(comen)):
                    Label(root,text = comenby[i]+" added comment :"+comen[i],font =("Arial",20) ).grid()
            if len(comen) == 0:
                Label(root,text = "Be first to add comment",font = ("Arial",20,"italic")).grid()
            comment = Entry(root)
            comment.grid()
            Button(root,text = "Comment",command = lambda post = allposts[0]:p.checkcomment(post,comment.get(),self.username,pagename)).grid()
            Button(root,text = "Next Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda:p.showposts(postcounter-1,allposts,postby,comments,commenter,data,pagename)).grid()
            # Button(root,text = "Next Post",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command =lambda:p.showposts(postcounter+1,root,allposts,postby,comments,commenter,data,pagename)).grid()

        if postcounter<0-len(allposts):
            Button(root,text = "Back",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda:p.GUIofjoinedPage(pagename)).grid()
            Label(root,text = "You are all caught up",font = ("Arial",50)).grid()
        root.mainloop()        
    def GUIofnotjoinedpages(self,pagename):
        root = Tk()
        root.geometry("1366x768")
        Label(root,font = ('Arial', 12, 'bold'), text = "This Page was created by "+Database_Manage.givepagesadmin(pagename)).grid(row = 0,column = 0)
        Label(root,font = ('Arial', 12, 'bold'), text= "To see page activities like page.").grid(row = 1,column =0)
        Button(root,text = "Like Page",command =lambda:MyFacebook.pa.Joinpage(self.username,pagename)).grid(row = 2,column = 0)
        root.mainloop()
    def initializepagewindy(self,username):
        self.username = username
        # windy.destroy()
        root = Tk()
        root.geometry("1366x768")
        m1 = Menu(root)
        m1.add_command(label = "create new page",command = p.createnewpage)
        # m1.add_command(label = "Page Setting")
        root.config(menu = m1)
        x = Database_Manage.givejoinedgroups(self.username)
        y = Database_Manage.notjoinedpages(self.username)
        if len(x)!= 0:
            Label(root,text = "Pages you have joined",font = ('Comic Sans MS', 12, 'bold')).grid(row = 0,column = 0)
        else:
            Label(root,text = "No page has been joined by you",font = ('Comic Sans MS', 12, 'bold')).grid()
        for i in range(len(x)):
            Button(root,text=x[i] ,font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda k = x[i]:p.GUIofjoinedPage(k)).grid(row = i+2,column = 1)
        if len(y)!=0:
            Label(root,text = "Pages you may like",font = ('Comic Sans MS', 12, 'bold')).grid(row = len(x)+2,column = 0)
        if len(y) == 0:
            Label(root,text = "No new page to show share",font = ("Comic Sans MS", 12, 'bold')).grid(row = len(x)+2,column = 0)
        for k in range(len(y)):
            Button(root,text = y[k],font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda j = y[k]:p.GUIofnotjoinedpages(j)).grid(row = len(x)+k+3,column = 1)
        Button(root,text ="Back to Home ",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda:h.Mainpage(self.username)).grid(row = 1700,column = 0)
        root.mainloop()
            
    def createnewpage(self):
        root = Tk()
        root.geometry("1366x768")
        Label(root,text = "Page Name").grid(row = 0,column = 0)
        namep = Entry(root)
        namep.grid(row = 0,column = 1)
        Button(root,text="Create",font = ("Arial",20,"bold"),bg = "#4267B2",fg = "white",command = lambda: MyFacebook.pa.createnewpage(namep.get(),self.username)).grid(row = 1,column = 2)
        root.mainloop()
class Profile:
    def profile_page(self,username):
        self.username = username
        root = Tk()
        root.geometry("1366x768")
        # windy.destroy()
        counter = 7
        Button(root,text = "Back to HomePage",font = ("Arial",20,"bold"),fg= "#4267B2",command = lambda:h.Mainpage(self.username)).grid(row = 50,column = 0)

        c.execute("SELECT * FROM SIGNUP WHERE Username = ?",(self.username,))
        y = c.fetchall()
        fr = MyFacebook.fr.friends_list(self.username)
        if fr!=[]:
            Label(root,text = "Friends:",font = ("Arial",20,"italic")).grid(row = 6,column = 0)
            for i in fr:
                Label(root,text = i,font = ("Arial",10)).grid(row= counter,column = 1)
                counter+=1
        if fr == []:
            Label(root,text = self.username+" has no friend ",font = ("Arial",20)).grid(row = counter,column = 0)
        root.mainloop()        
f = MainFrontend()
s  = Setting()  
p = Page()
pr = Profile()
fr = Friends()
se = Search()
m = Messages()
n = Notifications()
h = HomePage()
f.initial()