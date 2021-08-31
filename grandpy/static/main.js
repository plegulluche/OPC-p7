(function () {
    let Message;
    Message = function (arg) {
        this.text = arg.text, this.message_side = arg.message_side;
        this.draw = function (_this) {
            return function () {
                let $message;
                $message = $($('.message_template').clone().html());
                $message.addClass(_this.message_side).find('.text').html(_this.text);
                $('.messages').append($message);
                return setTimeout(function () {
                    return $message.addClass('appeared');
                }, 0);
            };
        }(this);
        return this;
    };
    $(function () {
        let getMessageText, message_side, sendMessage;
        message_side = 'right';
        getMessageText = function () {
            let $message_input;
            $message_input = $('.message_input');
            return $message_input.val();
        };
        sendMessage = function (text) {
            let $messages, message;
            if (text.trim() === '') {
                return;
            }
            $('.message_input').val('');
            $messages = $('.messages');
            message_side = message_side === 'left' ? 'right' : 'left';
            message = new Message({
                text: text,
                message_side: message_side
            });
            message.draw();
            return $messages.animate({ scrollTop: $messages.prop('scrollHeight') }, 300);
        };
        $('.send_message').click(function (e) {
            return sendMessage(getMessageText());
        });
        $('.message_input').keyup(function (e) {
            if (e.which === 13) {
                return sendMessage(getMessageText());
            }
        });
        
    });
}.call(this)); 

let message;

$('.send_message').click(function (event) {
    return message = $('.message_input').val();
    
})

$(document).keydown(function (event) {
    if (event.which === 13) {
        return message = $('.message_input').val();
        
    }
})

console.log(message)
if (message !== '' && message !== undefined) {

fetch(`${window.origin}/process`, {
    method: 'POST',
    credentials: 'include',
    body: JSON.stringify(message),
    cache: 'no-cache',
    headers: new Headers({ 'Content-Type': 'application/json'})
})
.then(function (response) {
    if (response.status !== 200) {
        console.log(`response status Not 200: ${response.status}`);
        return ;
    }

    response.json().then( function (data) {
        
        const test = JSON.stringify(data)
        console.log(test);

        
        const cursor = document.getElementById('response');
        const createP = document.createElement('p');
        createP.innerText = test
        cursor.append(createP)
     
    })    
})

}