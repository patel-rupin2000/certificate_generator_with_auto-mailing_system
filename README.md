# certificate_generator_with_auto-mailing_system

   Project is created by the team The Six Clique VIT-Hack:
   
        https://github.com/Aaryan5121
        
        https://github.com/Dhruvam25
        
        https://github.com/patel-rupin2000
        
        
        
        
   

#alter the .csv file add data or you can create another .csv file and add data  
1.just install required library of python -> opencv-python, pillow, smtplib, pyrebase

     Commnad line:pip install "name-of-python-library"

2.change the configuration of firebase according to your own apiKeys

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


    
4.just run certi.py it will automatically detect all .csv file present in folder and send mail to participants with .jpg attached and uplaod certificates on google firebase

     you can just check teams folder certificates will generated according to following path teams->college's name->event->.jpg file

5.for firebase just alter the credentials and apiKey in config.js file same config which are given in certi.py with your own apiKey

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

7.Or if you want to try hosting URL which is generated by Me so just change Emai_id as in 3rd steps settings and keep the firebase config same in  all files which is of mine-> Hosting URL:  https://cert-43ffe.web.app

8.Just write participants name and press submit button -> it will show the particular participants certificate
