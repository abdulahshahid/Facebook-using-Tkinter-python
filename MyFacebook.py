import Database_Manage
from tkinter import messagebox
class Facebook:
    def signup(self,username,password,email,city):
        Database_Manage.create_account(username,password,email,city)
    def login(self,username,password):
        y = Database_Manage.login(username,password) 
        return y
class User(Facebook):
    def search_user(self):
        x = input('Enter username to search: ')
        Database_Manage.search_user(x)
    def block_any_user(self,username,y):
        z = Database_Manage.check_existence(y)
        blocklist = Database_Manage.give_block_list(username)
        if y not in blocklist and z == True and y != username:
            Database_Manage.Block_user(username,y)
            messagebox.showinfo("blocked","successfully blocked user")
        if y in blocklist:
            messagebox.showerror("error","user is already blocked")
        if y == username or z == False:
            messagebox.showerror("error","no user found to block")
    def view_black_list(self,username):
        blocklist = Database_Manage.give_block_list(username)
        return blocklist
    def unblock_blocked_user(self,username,x):
        blocklist = Database_Manage.give_block_list(username)
        if x in blocklist:
            Database_Manage.unblock_user(x)
            messagebox.showinfo("unblocked","successfully unblocked")
        else:
            messagebox.showerror("error","no such user in blocked list")       
class Friends(User):
    def Notifications_friend(self,username):
        x = Database_Manage.notifications_friends(username)
        print(x)
        return x
    def friends_list(self,username):
        x = Database_Manage.give_friends(username)
        return x
class Messenger(User):
    def send_messages(self,username,receiver,mess):
        Database_Manage.send_message(username,receiver,mess)
class Post:
    def MakeNewPOST(self,post,username,posttype):
        print(posttype)
        if posttype == 1:
            Database_Manage.addNewPost(username,post,'Private')
        else:
            Database_Manage.addNewPost(username,post,'Public')
            Database_Manage.Notify_Friends_Of_new_post(username,post)
        messagebox.showinfo("Posted"," You just added a new post ")
    def show_all_posts(self,username):
        allfriends = fr.friends_list(username)
        posts = Database_Manage.give_posts(allfriends)
        return posts
class Pages:
    def createnewpage(self,pagename,admin):
        y = Database_Manage.giveallpagesnames()
        if pagename in y:
            messagebox.showerror("error","page with name already exist")
        else:
            z = Database_Manage.insertinPage1(pagename,admin)
            if z == True:
                messagebox.showinfo("created","new page has been created")
    def Joinpage(self,username,pagename):
        x = Database_Manage.Joinpage(username,pagename)
        if x == True:
            messagebox.showinfo("Joined","successfully joined "+pagename) 
    def MakeNewPOST(self,post,page,postedby):
        Database_Manage.addnewposttopage(post,page,postedby)
        messagebox.showinfo("Added","successfully added your post to page")



f = Facebook()
u = User()
fr = Friends()
me = Messenger()
p = Post()
pa = Pages() 