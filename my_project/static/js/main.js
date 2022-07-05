$(document).ready(function() {
    $(".address").suggestions({
        token: "5972803ddb5251f578cd38d1848d415ba68a3cfd",
        type: "ADDRESS",
        /* Вызывается, когда пользователь выбирает одну из подсказок */
        onSelect: function(suggestion) {
            console.log(suggestion);
        }
    });
});