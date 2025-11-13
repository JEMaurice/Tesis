$(function(){
    var url = 'ws://' + window.location.host + '/ws/room/' + room_id + '/';
    var chatSocket = new WebSocket(url);
    var historyUrl = '/api/get-messages/' + room_id + '/';

    // Función para cargar y mostrar los mensajes
    function loadMessages(showAll) {
        $.ajax({
            url: historyUrl,
            type: 'GET',
            success: function(response) {
                var messages = response.messages;

                // Mostrar todos los mensajes si showAll es verdadero, de lo contrario, mostrar solo los últimos 4
                if (showAll) {
                    messages.forEach(function(message) {
                        renderMessage(message);
                    });
                } else {
                    var lastFourMessages = messages.slice(Math.max(messages.length - 4, 0));
                    lastFourMessages.forEach(function(message) {
                        renderMessage(message);
                    });
                }
                // Desplazar el contenedor hacia abajo después de cargar los mensajes
                scrollToBottom();
            },
            error: function(xhr, status, error) {
                console.error('Error al obtener los mensajes:', error);
            }
        });
    }

    // Función para renderizar un mensaje en la interfaz de usuario
    function renderMessage(message) {
        var username = message.user;
        var text = message.message;
        var datetime = message.timestamp;

        // Formatear la fecha y hora del mensaje
        var formattedDate = new Date(datetime).toLocaleString();

        // Crear el HTML del mensaje
        var messageHTML = `
            <div class="callout secondary">
                ${text}
                <div class="clearfix">
                    <small class="float-left fst-italic fw-bold">${username}</small>
                    <small class="float-right">${formattedDate}</small>
                </div>
            </div>
        `;

        // Agregar el mensaje al contenedor en la interfaz de usuario
        $('#boxMessagess').append(messageHTML);
    }

    // Función para desplazar el contenedor del chat hacia abajo
    function scrollToBottom() {
        var chatContainer = $('#chatContainer');
        chatContainer.scrollTop(chatContainer[0].scrollHeight);
    }

    // Cargar los últimos 4 mensajes al cargar la página
    loadMessages(false);

    // Manejar clic en el botón "Mostrar Todos"
    $('#showAllBtn').click(function() {
        $('#boxMessagess').empty(); // Limpiar el contenedor
        loadMessages(true); // Cargar y mostrar todos los mensajes    
    })

    // Manejar clic en el botón "Mostrar Menos"
    $('#showLessBtn').click(function() {
        $('#boxMessagess').empty(); // Limpiar el contenedor
        loadMessages(false); // Cargar y mostrar todos los mensajes    
    })

    chatSocket.onopen = function(e){
        console.log('WEBSOCKET ABIERTO')
    }

    chatSocket.onclose = function(e){
        console.log('WEBSOCKET CERRADO')
    }

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);

        console.log(data.type)

        if (data.type === 'chat_message') {

            var msj = data.message
            var username = data.username
            var datetime = data.datetime

            document.querySelector('#boxMessages').innerHTML +=
            `
            <div class="callout secondary" style="background-color: lightgreen;">
            ${msj}
                <div class="clearfix">
                    <small class="float-left fst-italic fw-bold">${username}</small>
                    <small class="float-right">${datetime}</small>
                </div>
            </div>
            `
            // Desplazar el contenedor hacia abajo después de agregar un nuevo mensaje
            scrollToBottom();

        } else if (data.type === 'user_list') {
            let userListHTML = '';

            for (const username of data.users){
                const userClass = (username === user) ? 'list-group-item-success' : ''
                userListHTML += `<li class="list-group-item ${userClass}">${username}</li>`
            }
            document.querySelector('#userList').innerHTML = userListHTML
        }
    }

    // tocar el boton con click para que mande el mensaje
    document.querySelector('#btnMessage').addEventListener('click', sendMessage)

    // tocar el boton enter para que mande el mensaje (e.keyCode == 13 en el teclado es el ENTER)
    document.querySelector('#inputMessage').addEventListener('keypress', function(e){
        if(e.keyCode == 13){
            sendMessage()
        }
    })

    function sendMessage(){
        // mensaje enviado por el usuario
        var message = document.querySelector('#inputMessage')

        // limpiamos el input y sacamos los espacios adelante y detras del mensaje y enviamos el mensaje
        if(message.value.trim() !== ''){
            loadMessageHTML(message.value.trim())
            chatSocket.send(JSON.stringify({
                type : 'chat_message',
                message: message.value.trim(),
            }))

            console.log(message.value.trim())

            message.value = ''
        } else {
            console.log('Envió un mensaje vacío')
        }
    }

    function loadMessageHTML(m){
        // armamos el formato que se mostrara la fecha y hora que se manda el mensaje
        var currentDatetime = new Date();
        var dateObject = new Date(currentDatetime)

        var year = dateObject.getFullYear();
        var month = ('0' + (dateObject.getMonth() + 1)).slice(-2);
        var day = ('0' + dateObject.getDate()).slice(-2);
        var hours = ('0' + dateObject.getHours()).slice(-2);
        var minutes = ('0' + dateObject.getMinutes()).slice(-2);
        var seconds = ('0' + dateObject.getSeconds()).slice(-2);

        const formattedDate = `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`

        document.querySelector('#boxMessages').innerHTML +=
        // inscrustamos el usuario qie escribio, el mensaje del usuario y fecha y hora que manda el mensaje
        `
        <div class="callout primary">
        ${m}
        <div class="clearfix">
            <small class="float-left fst-italic fw-bold">${user}</small>
            <small class="float-right">${formattedDate}</small>
        </div>
    </div>
        `
        // Desplazar el contenedor hacia abajo después de agregar un nuevo mensaje
        scrollToBottom();
    }

})