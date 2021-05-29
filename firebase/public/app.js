const auth = firebase.auth();
const db = firebase.firestore();

const content= document.querySelector("#content");

auth.onAuthStateChanged( user => {

  if(user){
    content.innerHTML=`
                
                  <a href='firebase-photos.html'>
                    <button >View Certificate</button>
              </a>

                

                <button id="logout">Logout</button>`;
      

   

  
    //logout
    const logout = document.querySelector("#logout");

    logout.addEventListener('click', event => {
      event.preventDefault();
      auth.signOut().then(cred=>{
        //console.log(cred);
      });
    });

  }else{

    content.innerHTML=`<form id="signup-form">
      <input type="email" id="signup-email" placeholder="Email" required/>
      <input type="password" id="signup-password" placeholder="Password" required/>
      <button> Signup </button>
    </form>

    <hr>

    <form id="login-form">
      <input type="email" id="login-email" placeholder="Email" required/>
      <input type="password" id="login-password" placeholder="Password" required/>
      <button> Login </button>
    </form>

    <hr>

    <button id="google">Sign in with google</button>
    

    `;

    //signup using email
    const signup = document.querySelector("#signup-form");

    signup.addEventListener('submit', (event) => {
      event.preventDefault();

      const email = signup['signup-email'].value;
      const password = signup['signup-password'].value;

      auth.createUserWithEmailAndPassword(email,password).then( cred => {
        //console.log(cred);
        signup.reset();
      }).catch( e => {
          alert(e.message);
      });
    });



    


    //sign in with Google
    const google = document.querySelector("#google");

    google.addEventListener('click', event => {
      event.preventDefault();

      let provider = new firebase.auth.GoogleAuthProvider();

      auth.signInWithPopup(provider).then( cred =>{
        alert('Logged in with google');
      }).catch(e=>{
        alert(e.message);
      });
    });

    //login
    const login = document.querySelector("#login-form");

    login.addEventListener('submit', event => {
      event.preventDefault();

      const email = login['login-email'].value;
      const password = login['login-password'].value;

      auth.signInWithEmailAndPassword(email,password).then( cred => {
        //console.log(cred);
        login.reset();
      }).catch(e =>{
        alert(e.message);
      });

    });

  }

});
