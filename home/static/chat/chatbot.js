//hàm xử lí chat

var date, time;
let divBot, divUser;
var divLocation;
//hàm khởi tạo

function Construct(){
    checkTime();
    divLocation = document.getElementsByClassName("detail_location")[0];

    var divCopy = document.getElementsByClassName("row-bot-chat");
    divBot = divCopy[0].cloneNode(true);

    divCopy = document.getElementsByClassName("row-user-chat");
    divUser = divCopy[0].cloneNode(true);
    
    $(".row-user-chat:last").remove();
   // $(".mapouter").last().hide();
    $("#bot-load").hide()
    $("#add_show").hide();
    //tạo thời gia bot chat hiển thị đầu tiên html
    document.getElementsByClassName("msg_time")[0].innerHTML = time;
    //lấy div Bot và User
}

Construct();

function checkTime(){
    today = new Date();
    date = today.getDate()+'-'+(today.getMonth()+1)+'-'+today.getFullYear();
    time = today.getHours() + ":" + today.getMinutes();
}

function showMap(data){
    place = 'https://maps.google.com/maps?q='+ data + '&t=&z=13&ie=UTF8&iwloc=&output=embed';
    $("#gmap_canvas").attr('src', place);
    $(".mapouter").last().show();
}


function addTextBot(data){
    checkTime();
    let temp = divBot.cloneNode(true);
    $("#bot-load").before(temp);
    $(".text_bot:last").text(data);
    $(".msg_time:last").text(time);
    $("#bot-load").hide();
}

function addTextUser(data){
    checkTime();

    $("#bot-load").show();
    let temp = divUser.cloneNode(true);

    $("#bot-load").before(temp);
    $(".text_user:last").text(data);
    $(".msg_time_send:last").text(time);
}

function setUI() {
    setTimeout( function(){
    var dialogDom = document.getElementById("chatbox");
    dialogDom.scrollTop = dialogDom.scrollHeight;
    })
};

function listLocations(data){
    $("#add_show").show();
    //tách chuỗi thành mảng

    for(var i = 0; i < data.length; i++) {
        let temp = divLocation.cloneNode(true);
        $("#detail_locations").append(temp);
        
        var tr =  $(".detail_location").last();
        tr.find("td:eq(0)").text(i+1);
        tr.find("td:eq(1)").text(data[i].name);
        tr.find("td:eq(2)").attr('href', data[i].link).text("Ảnh");
        tr.find("a:first").attr('href', '#gsc.tab=0&gsc.q='+  data[i].name +'&gsc.sort=').text("Tìm Kiếm");
    }


    // $("#map").append(viewHtml);
    // $("#chatbox").append(botHtml);
}

function show(data, user){
    var div2 = document.getElementsByClassName("link-preview");
    var div = document.getElementsByClassName("img-fluid");
    $('#gmap_canvas').attr('src', 'https://maps.google.com/maps?q=' + user +'&t=&z=13&ie=UTF8&iwloc=&output=embed');
    
    for(var i = 0; i < div.length; i++){
       
        div[i].setAttribute('src', data.data[0].img[i]);
        div2[i].setAttribute('href', data.data[0].img[i]);
    }

    //thông tin
    var div = document.getElementsByClassName("review-text-p");
    var div2 = document.getElementsByClassName("review-img-src");

    for(var i = 0; i < div.length; i++){
        div[i].innerHTML = data.data[0].wiki[i];
        div2[i].setAttribute('src', data.data[0].img[i]);
    }
    
}


function test(){
    a = '{"in" : "text", "data" : ["ad","sp"]}';
    a = JSON.parse(JSON.stringify(eval('('+a+')')));
    alert(a.data[1]);
}


function getBotResponse() {
    setUI();


    var rawText = $("#textInput").val();
    rawText = rawText.toLowerCase();
    $("#textInput").val("");

    addTextUser(rawText);
       
    $.get("/get", { msg: rawText }).done(function(data) {
        //nếu người dùng hỏi đường
       
        try {
            data = JSON.parse(JSON.stringify(eval('('+data+')')));
            
            if(data.type == "text"){
                addTextBot(data.data);      
            }
            else if(data.type == "tt"){
                show(data, rawText);
                addTextBot("BOT đã tìm xong ạ!");
            }
            else if(data.type == "table"){
                addTextBot(data.data);
                addTextBot("cú pháp: tìm + {tên}");
                addTextBot("ví dụ: tìm đại nội Huế");
            }

        } catch (error) {
            addTextBot('BOT không hiểu ạ !');
        }
    });

}

$("#textInput").keypress(function(e) {
    if ((e.which == 13) && document.getElementById("textInput").value != "" ){
        getBotResponse();
    }
});
$("#buttonInput").click(function() {
    if (document.getElementById("textInput").value != "") {
        getBotResponse();
    }
})