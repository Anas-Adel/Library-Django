function signUp() {
    
    if (document.getElementById("Username").value.length == 0) {
        alert("Username is empty!");
        return true;
    }

    if (document.getElementById("password").value.length == 0) {
        alert("Password is empty!");
        return true;
    }

    if (document.getElementById("password").value.length < 6) {
        alert("Password must be at least 6 characters")
        return true;
    }

    if (document.getElementById("password").value != document.getElementById("confpass").value) {
        alert("passwords don't match");
        return true;
    }
    if (document.getElementById("check").checked) {
        window.location.replace("Admin main page.html");
    }
    else {
        window.location.replace("user main page.html");
    }
    return false;
}

function LogIn() {
    if (document.getElementById("Username").value.length == 0) {
        alert("Username is empty!");
        return true;
    }

    if (document.getElementById("password").value.length == 0) {
        alert("Password is empty!");
        return true;
    }

    if (document.getElementById("check").checked) {
        window.location.replace("Admin main page.html");
    }
    else {
        window.location.replace("user main page.html");
    }
    return false;
}