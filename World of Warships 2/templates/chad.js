//łączenie sie z serwerem
var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.addEventListener( 'connect', function() {
    socket.emit( 'my event', {
        data: 'User Connected'
    } )

    var form = document.getElementById('chadForm').addEventListener( 'submit', function( e ) {
        e.preventDefault()
        //↓pozostałości po oryginalnym kodzie który z jakiegoś nieracjonalnego powodu był zaśmiecony jquery, po przepisaniu tego wszystkiego zostawiłem tą linijke żebym o czymś nie zapomniał ale już nie pamiętam co to było
        //let user_name = $( 'input.username' ).value()
        let user_input = document.getElementById( 'chadMesContent' ).value
        socket.emit( 'my event', {
        //jak narazie nazwy nie da sie zmienić, zamierzam dodać cookie z jakimś losowo generowanym unikalnym identyfikatorem do którego będzie przypisana nazwa i wszystko powiązane z grą ale do tego jeszcze troche brakuje
        user_name : "Anon",
        message : user_input
        } )
    } )
} )


//bez tego chat zamienia sie w piaskownice skryptów
function sanitize(string) {
  const map = {
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#x27;',
      "/": '&#x2F;',
  };
  const reg = /[&<>"'/]/ig;
  return string.replace(reg, (match)=>(map[match]));
}

socket.addEventListener( 'my response', function( msg ) {
console.log( msg )
if( typeof msg.message !== 'undefined' ) {
    //jak narazie czyszcze tylko samą wiadomość bo zmiany nazwy jeszcze nie wprowadziłem
    massage = sanitize(msg.message);
    document.getElementById( 'chadMes' ).innerHTML += '<div class="message"><b>'+msg.user_name+' :</b> '+massage+'</div>'
}
})
