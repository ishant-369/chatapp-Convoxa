const usersContainer = document.getElementById('users-container');
function addUser(username){
    const userDiv = document.createElement("div");
    userDiv.classList.add("friend");
    userDiv.textContent = username;
    usersContainer.appendChild(userDiv);    
    
    window.alert("A girl from your area wants to sleep with you");
    
    

}
//for temporarily testing cause i dont have backend rn so i will just user add user type thing instead of the fetch function
    //addUser("joe goldberg");
    //addUser("tony stark");
    //addUser("thomas shelby");
    
