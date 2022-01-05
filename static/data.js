 function saveData(){
        let matches_data = document.getElementById("matches").value;
        let category_data = document.getElementById("category").value;
        let difficulty_data = document.getElementById("difficulty").value;
        let data = { matches : matches_data, category : category_data, difficulty : difficulty_data };
        fetch("/save", {
            method: "POST",
            headers: {'Content-Type': 'application/json'}
            body: JSON.stringify(data);} )
 document.getElementById("saveButton").addEventListener("click", saveData, false);
