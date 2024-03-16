from django.shortcuts import render,redirect



import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="fx818",
  password="fx818",
  database='teckathon'
)
db = 'hbtuerp'
mycursor = mydb.cursor()


def index(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        command = 'select * from user where username = %s'
        mycursor.execute(command,(username,))
        res = mycursor.fetchall()
        
        if len(res)!=0 and res[0][-1] == password:    
            return redirect('home')
        
        else:
            errormsg = {'error':'Sorry buddy Something is wrong'}
            return render(request,'index.html',errormsg)

    else:
        return render(request,'index.html')
    
    
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        dn = 'Now login !'

        
        command = "insert into user values(%s,%s,%s,%s)"
        mycursor.execute(command,(name,username,email,password1))
        mydb.commit()
        return redirect('/')
        # return redirect('index')
    
    else:
        return render(request,'register.html')
    
    
    
def home(request):
    return render(request,'home.html')
    
    
# command = 'select * from user where username = %s'
# mycursor.execute(command,('fx818',))
# res = mycursor.fetchall()
# print(res)

def application(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        role = request.POST['role']
        education = request.POST['education']
        experience = request.POST['experience']
        referral = request.POST['referral']
        # email = request.POST['email']
        # email = request.POST['email']
        
        value = (name,email,mobile,role,education,experience,referral)

        command = 'insert into application values(%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(command,value)
        mydb.commit()
        return render(request,'msg.html')


    else:
        return render(request,'application.html')
    


def opportunities(request):
    return render(request,'../')


def allrequests(requests):

    command = 'select * from application'
    mycursor.execute(command)
    res = mycursor.fetchall()
    data = {
        'values':res
    }
    return render(requests,'allrequests.html',data)



