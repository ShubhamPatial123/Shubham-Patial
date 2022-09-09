import pyrebase
firebaseConfig= {
  'apiKey': "AIzaSyB9IAFOI6NUwcx9HALoEmBrLPehuD4INhA",
  'authDomain': "hello-fe480.firebaseapp.com",
  'databaseURL': "https://hello-fe480-default-rtdb.firebaseio.com",
  'projectId': "hello-fe480",
  'storageBucket': "hello-fe480.appspot.com",
  'messagingSenderId': "868252179136",
  'appId': "1:868252179136:web:77e1243c4bb5307e21ab25",
  'measurementId': "G-47FMCJ5LRV"}

firebase=pyrebase.initialize_app(firebaseConfig)
auth=firebase.auth()  

def signup():
    email=input("enter email:")
    password=input("enter password:")
    try:
        user=auth.create_user_with_email_and_password(email,password)
        print("successfully built account")
        ask= input("do you want to login now?[y/n]")
        if ask=='y':
             login()

    except:
        print("Email already exists!")
signup()

def login():
    print("Login....")
    email=input("Enter email:")
    password=input("Enter password:")
    try:
        login=auth.sign_in_with_email_and_password(email,password)
        print("Sucessfully logged in.....!")
        print(auth.get_account_info(login['idToken']))
    except:
        print('Invalid email or password!')


ans=input("are you anew user?[y/n]")
if ans=='y':
    signup()
elif ans=='n':
    login()    

login()    


