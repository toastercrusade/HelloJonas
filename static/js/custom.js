$('body').on('DOMSubtreeModified', '.highscore', function(event) {
    $.ajax({
        data : {
            score : $('.highscore').text()
        },
        type : 'POST',
        url : '/update/score'
    })
    .done(function(data) {
        if (data.error) {
            console.log("ERROR RETURNED");
            
        }else {
            // change border color of card
            console.log("SUCCESS");
        }
    });
});