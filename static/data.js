 document.getElementById("saveButton").addEventListener("click", saveData1, false);


function saveData1(){
       let matches_data = document.getElementById("matches").value;
        let category_data = document.getElementById("category").value;
        let difficulty_data = document.getElementById("difficulty").value;
        let data = { matches : matches_data, category : category_data, difficulty : difficulty_data };
        let request = new XMLHttpRequest();
        request.open("POST", "/save",true);
        request.setRequestHeader('Content-Type', 'application/json');
        request.send(JSON.stringify(data));

}

