
        

      async function getDBInfo() {
           
              try {
               let resultsDiv = document.getElementById("table");
             
                 let searchProduct = document.getElementById('searchInput').value
                 let url ="http://localhost:8081/process_get/" + "?"  + new URLSearchParams({serachTerm:searchProduct})
                 
                 const response = await fetch(url);
                 const result  = await response.json();
                // createTableWitHResults(result)
                 console.log("Success:", result);
                 resultsDiv.innerText = "Product: "+result[0].ProductName + "Description: "+result[0].Description+" Price: $"+result[0].Price;
                 
              } catch (error) {
                 console.error("Error:", error);
              }
        }




        function addHeaders(table, keys) {
         let row = table.insertRow();
         for( let i = 0; i < keys.length; i++ ) {
           let cell = row.insertCell();
           cell.appendChild(document.createTextNode(keys[i]));
         }
       }
       
      
       
        createTableWitHResults =function  (stateArray) {
           let table = document.createElement('table');
           for( let i = 0; i < stateArray.length; i++ ) {
       
           let state = stateArray[i];
           if(i === 0 ) {
               addHeaders(table, Object.keys(child));
           }
           
           let row = table.insertRow();
           Object.keys(state).forEach(function(k) {
               console.log(k);
               let cell = row.insertCell();
               cell.appendChild(document.createTextNode(child[k]));
           })
           }
       
           document.getElementById('tables').appendChild(table)
       }
     
      

