from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('wow2.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    #tutaj zamierzam dodać IO do statków jednak jeszcze nie jestem pewien w jaki sposób chce to zaimplementować (funkcja?,jakoś osobny plik? game loop? itp?), ale najpierw na pewno będe musiał wyodrębnić wiadomość od reszty eventu, następnie jakaś 'interpretacja' i powinien być git, aktualnie myśle żeby komendy wyglądały mniej więcej tak:
    #
    #    b4                 - strzał
    #    b4-b8              - ułożenie statków, od pozycji   do pozycji
    #    b4-b8,a1-e1,f2-d4  - wielokrotne ułożenie statków
    #    
    #może być to niezbyt wygodne dla gracza, jednak bardziej martwie sie tu o pare problemów które musiałbym rozwiązać żeby było to wgl możliwe
    socketio.emit('my response', json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)
