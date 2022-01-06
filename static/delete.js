document.getElementById("deleteButton").addEventListener("click", deleteUser(), false);
function deleteUser(){
        data = {test: "test"}
        let request = new XMLHttpRequest();
        request.open("POST", "/deleteUser",true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.send(JSON.stringify(data));

}