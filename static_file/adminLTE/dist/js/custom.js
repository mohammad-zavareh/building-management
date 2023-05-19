function addManager(pk){
    $.get('/manager-panel/add-manager', {
        pk: pk
    }).then(message => {

        const buttonElement = $("#add_manager_id_" + pk)
        const badgeElement = $("#is_manager_badge_" + pk)

        badgeElement.append('<span class="right badge badge-primary">مدیر</span>')

        buttonElement.empty();
        buttonElement.html('<button class="btn btn-success" disabled >ارتقا به مدیر</button>')
        console.log(message)
        $("#alert").html(message)
    });
}

function resignManager(token){
    $.post("/manager-panel/resign-manager",{
        'csrfmiddlewaretoken': token
    }).then(message =>{
        $(".modal").modal('toggle');
        $("#alert").html(message)
    });
}