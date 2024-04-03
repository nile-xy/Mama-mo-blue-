function login() {
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    firebase.auth().signInWithEmailAndPassword(email, password)
    .then((userCredential) => {
        // Signed in
        const user = userCredential.user;
        document.getElementById('message').innerText = 'Logged in successfully!';
    })
    .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        document.getElementById('message').innerText = errorMessage;
    });
}

function signup() {
    const email = document.getElementById('signupEmail').value;
    const password = document.getElementById('signupPassword').value;

    firebase.auth().createUserWithEmailAndPassword(email, password)
    .then((userCredential) => {
        // Signed up
        const user = userCredential.user;
        document.getElementById('message').innerText = 'Signed up successfully!';
    })
    .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        document.getElementById('message').innerText = errorMessage;
    });
}
