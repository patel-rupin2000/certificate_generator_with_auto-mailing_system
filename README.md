# certificate_generator_with_auto-mailing_system
just install required libarary of python -opencv-python,pillow,smtplib,pyrebase
change the configuration of firebase according to your own apiKeys
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
change variables from_addr='to your email id',email='to your email id',recipients='to your email id'
Commnad line:pip install <name-of-python-library>
just run certi.py it will auto matically send mail to participants and uplaod certificates on google firebase
you can just check teams folder certificates will generated according to following path teams->college's name->event->.jpg file
for firebase just alter the credentials and apiKey in config.js file same config which are given in cert.py
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
Just change directory to firebase folder in CMD and  type "firebase serve" (make sure that you have installed firebase tool in your system)
Or if you want to try hosting URL ->Hosting URL:  https://cert-43ffe.web.app
Just write participants name and press submit button -> it will show the particular participants certificate
