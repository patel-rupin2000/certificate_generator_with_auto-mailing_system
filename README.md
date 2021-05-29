# certificate_generator_with_auto-mailing_system
<h2>If you want try deployed tool run main.exe file and do watch video https://youtu.be/VY9aPLamaHg  for reference and the website for validation URL:  https://cert-43ffe.web.app </h2>
<h2>You can download main.exe file from repository as well as from https://drive.google.com/file/d/1KxNgo27yFAFzfIXKiSZQL9X4rQo-EV9V/view?usp=sharing </h2>


<h1>If you want to mainpulate code follow the steps to run source code</h1>
        
        
#alter the .csv file add data or you can create another .csv file and add data  
1.just install required library of python -> opencv-python, pillow, smtplib, pyrebase,

     Commnad line:pip install "name-of-python-library"

2.change the configuration of firebase according to your own apiKeys in main.py and dynamic.py file

config={

    "apiKey": "****",
    
    "authDomain": "****",
    
    "databaseURL": "***",
    
    "projectId": "**",
    
    "storageBucket": "***",
    
    "messagingSenderId": "***",
    
    "appId": "***",
    
    "measurementId": "****"
}

3. Email_id settings change variables-> 

       from_addr='to your email id',

       email='to your email id',

       recipients='to your email id'
       
       password="*****"
       
       Make sure that you ON the less secure app option ON of your Google Account : https://myaccount.google.com/lesssecureapps


    
4.just run main.py it will open GUI app and just follow the steps (Refrence:https://youtu.be/VY9aPLamaHg) do refer result.txt file for certificates hash code


5.for firebase just alter the credentials and apiKey in config.js file same config which are given in main.py with your own apiKey

config={

    "apiKey": "****",
    
    "authDomain": "****",
    
    "databaseURL": "***",
    
    "projectId": "**",
    
    "storageBucket": "***",
    
    "messagingSenderId": "***",
    
    "appId": "***",
    
    "measurementId": "****"
}

6.Just change directory to firebase folder in CMD and  type "firebase serve" (make sure that you have installed firebase tool in your system)

7.Just write hash code press submit button -> it will show the particular participants certificate
