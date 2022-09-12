from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%d/%m/%Y")
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect('My facebook.db')
c = conn.cursor()
def checkuser(Name):
    print(Name)
    c.execute("SELECT username FROM SIGNUP")
    data = c.fetchall()
    state = False
    for i in data:
        if i[0] == Name:
            state = True
    return state
def create_account(Name,Password,Gmail_address,city):
    c.execute("SELECT * FROM SIGNUP")
    c.execute("INSERT INTO SIGNUP VALUES(?,?,?,?)",(Name,Password,Gmail_address,city,))
    conn.commit()
    conn.close()
def login(Name,Password):
    state = False
    c.execute("SELECT * FROM SIGNUP")
    data = c.fetchall()
    for i in data:
        if i[0] == Name and str(i[1]) == Password:
            state = True
    return state
def search_user(name,username):
    c.execute("SELECT * FROM SIGNUP")
    data = c.fetchall()
    check = 0
    for i in data:
        if i[0] == name and i[0]!= username:
            check= i
    return check
def check_existence(Name):
    c.execute("SELECT * FROM SIGNUP")
    data = c.fetchall()
    state = False
    for i in data:
        if i[0] == Name:
            state = True
    return state
def check_duality(username,x):
    c.execute("SELECT * FROM Friends_Notifications")
    data = c.fetchall()
    duality = False
    for i in data:
        if (i[0]== x and i[2] == username) or (i[0] == username and i[2] == x):
            duality = True
    return duality
def notifications_friends(username):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    notif = []
    print(username)
    c.execute("SELECT Sender FROM Friends_Notifications WHERE Receiver = ?",(username,))
    data = c.fetchall()
    for i in data:
        notif.append(i[0])
    print(notif)
    return notif
def enrol_friend(lst,username):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO Friends VALUES(?,?)",(lst,username,))
    c.execute("INSERT INTO Friends VALUES(?,?)",(username,lst,))
    messagebox.showinfo("Added","Friend Added")
    conn.commit()
    conn.close()
def give_friends(username):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    f_list = []
    c.execute("SELECT * FROM Friends WHERE User = ?",(username,))
    data = c.fetchall()
    for i in data:
        f_list.append(i[1])
    return f_list
def unfriend(username,friend):
    print(username,friend)
    c.execute("DELETE FROM Friends WHERE User = ? AND Friend = ?",(username,friend,))
    c.execute("DELETE FROM Friends WHERE User = ? AND Friend = ?",(friend,username,))
    conn.commit()
    messagebox.showinfo("Removed","User has been removed from your friends list")
def Block_user(username,blocked):
    c.execute("INSERT INTO Black_list VALUES(?,?)",(username,blocked,))
    conn.commit()
    conn.close()
def give_block_list(username):
    lst = []
    c.execute("SELECT * FROM Black_list WHERE Blocker = ?",(username,))
    y = c.fetchall()
    for i in y:
        lst.append(i[1])
    return lst
def unblock_user(y):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("DELETE FROM Black_list WHERE Blocked = ?",(y,))
    messagebox.showinfo("unblocked","successfuly unblocked "+y)
    conn.commit()
    conn.close()
def addNewPost(username,post,posttype):
    c.execute("INSERT INTO Posts VALUES(?,?,?,?,?)",(username,post,posttype,current_date,current_time,))
    conn.commit()
    conn.close()
def Notify_Friends_Of_new_post(username,post):
    fr = give_friends(username)
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    for i in fr:
        c.execute("INSERT INTO Notifications_Posts VALUES(?,?,?)",(i,post,username,))
    conn.commit()
    conn.close()
def give_posts(friends):
    posts = []
    if len(friends) == 0:
        return []
    else:
        for i in friends:
            c.execute("SELECT * FROM POSTS WHERE username = ? AND Posttype = ?",(i,"Public",))
            p = c.fetchall()
            posts.append(p)
        return posts
def addcomments(post,comment,username):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    print(comment)
    c.execute("INSERT INTO Comments VALUES(?,?,?)",(post,comment,username,))
    c.execute("SELECT Username FROM Posts WHERE Post = ?",(post,))
    name = c.fetchall()
    c.execute("INSERT INTO ALL_Notifications VALUES(?,?,?)",(name[0][0],"Comment1",username))
    messagebox.showinfo("added","comment added successfully")
    conn.commit()
    conn.close()
def send_message(user,receiver,mess):
    print(user,receiver)
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO CurrentChat Values(?,?,?)",(user,receiver,mess))
    c.execute("INSERT INTO ChatPerson VALUES(?,?)",(user,receiver))
    c.execute("INSERT INTO ChatPerson VALUES(?,?)",(receiver,user))

    conn.commit()
    messagebox.showinfo("Messenger","Message sent")
def giveallpagesnames():
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    p_names = []
    c.execute("SELECT Pagename FROM Page1")
    names = c.fetchall()
    for i in names:
        p_names.append(i[0])
    return p_names
def insertinPage1(pagename,admin):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO Page1 VALUES(?,?)",(pagename,admin,))
    c.execute("INSERT INTO Page1 VALUES(?,?)",(pagename,admin))
    conn.commit()
    conn.close()
def givejoinedgroups(username):
    j_pages = []
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("SELECT Pagename FROM Page2 WHERE Members = ?",(username,))
    dat = c.fetchall()
    for i in dat:
        j_pages.append(i[0])
    return j_pages
def notjoinedpages(username):
    not_j_pages = []
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    y = givejoinedgroups(username)
    c.execute("SELECT Pagename FROM Page1")
    dat = c.fetchall()
    for i in dat:
        if i[0] not in y:
            not_j_pages.append(i[0])
    return not_j_pages
def givepagesadmin(pagename):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("SELECT Admins FROM Page1 WHERE Pagename = ?",(pagename,))
    dat = c.fetchall()
    return dat[0][0]
def Joinpage(username,pagename):
    c.execute("INSERT INTO Page2 VALUES(?,?)",(pagename,username,))
    c.execute("INSERT INTO PageActivity VALUES(?,?,?)",(pagename,"new added",username))
    conn.commit()
    conn.close()
    return True
def addcommentinPage(post,comment,username,pagename):
    import sqlite3
    conn = sqlite3.connect('My facebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO Page_Comments VALUES(?,?,?,?)",(post,"",comment,username,))
    c.execute("SELECT PostedBy FROM Page_Posts WHERE Post = ?",(post,))
    name = c.fetchall()
    c.execute("INSERT INTO ALL_Notifications VALUES(?,?,?)",(name[0][0],"Comment",username))
    c.execute("INSERT INTO PageActivity VALUES(?,?,?)",(pagename,"new comment",username))

    conn.commit()
    conn.close()
    messagebox.showinfo("Comment","Your comment has been added")
def addnewposttopage(post,page,postby):
    receiver = []
    c.execute("INSERT INTO Page_Posts VALUES(?,?,?,?,?)",(post,page,postby,current_date,current_time,))
    c.execute("INSERT INTO PageActivity VALUES(?,?,?)",(page,"new post",postby))
    members = c.execute("SELECT Members FROM Page2 WHERE Pagename = ?",(page,))
    for i in members:
        if i[0]!=postby:
            receiver.append(i[0])
    for j in receiver:
        c.execute("INSERT INTO ALL_Notifications VALUES(?,?,?)",(j,"Page",postby))
        
    conn.commit()
    conn.close()
def reset_password(password,email):
    change = False
    if len(password)>= 4:
        c.execute("""UPDATE SIGNUP SET pasword = ? WHERE Email = ?""",(password,email))
        conn.commit()
        change = True
        messagebox.showinfo("reset","successfuly reset your password")
    if len(password)< 4:
        messagebox.showwarning("password","password should contain atleast 4 characters")
    return change
        

    