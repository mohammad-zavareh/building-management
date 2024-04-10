$('#submit-comment').click(function (e) {
    e.preventDefault();
    var url = $('#comment-form').attr("action");
    var comment = $('#comment-text').val();
    var notifi_id = $('#notifi-id').val();
    var token = $("#comment-form").find('input[name=csrfmiddlewaretoken]').val();
    let unit_name = document.getElementById("unit-name").innerHTML;
    console.log(unit_name)

    $.ajax({
        method: "POST",
        url: url,
        data: {
            csrfmiddlewaretoken: token,
            'comment': comment,
            'notifi_id': notifi_id,
        },
        success: function () {
            $('#comment-text').val('');
            $('#comment-list').append(
                `                            <div class="card">
                                <div class="card-body">
                                    <h5>${unit_name}</h5>
                                    <p class="card-text">${comment}</p>
                                </div>
                            </div>`
            );
        }
    });
});