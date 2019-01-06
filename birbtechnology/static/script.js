var get_image = function (){
    $.getJSON("api/get", function(data){
        $("#bird_image").attr("src", data["url"]);
        $("#source").attr("href", data["source"]);
        $("#creator").attr("href", data["creator"]);
        $("#collection").html(data["collection"]);
    });
}

$(get_image);
$("#new_image").click(get_image)