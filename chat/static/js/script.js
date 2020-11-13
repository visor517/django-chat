var chats = document.querySelectorAll(".messenger_layout");

chats.forEach(function(elem) { 
    elem.scrollTop = elem.scrollHeight;
});
