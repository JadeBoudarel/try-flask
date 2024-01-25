$( document ).ready(function() {
 
    $( "#btn1" ).click(function( event ) {
   
        alert( "im win" );
   
        event.preventDefault();
    });
   });



   fetch('../static/data.json')
  .then(response => response.json())
  .then(data => {
    const formattedData = JSON.stringify(data, null, 2);


        document.getElementById('content').innerHTML = `<pre>${formattedData}</pre>`;
      })


