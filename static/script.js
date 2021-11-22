
function init() {
    function upload() {
        function draw(data) {
            console.log(data);
            predictions = data.predictions;
            if (predictions.length > 0) {
                predictions.forEach(prediction => {
                    console.log(prediction)
                    box = prediction.boundingBox;
                    ocontext.strokeRect(
                        box.left*640, 
                        box.top*480, 
                        box.width*640, 
                        box.height*480
                        );
                    ocontext.fillText(
                        prediction.tagName + " " + prediction.probability, 
                        (box.left)*640+5,
                        (box.top+box.height)*480-5
                        );
                    document.getElementById(prediction.tagName).play();
                });
            } else {
                ocontext.strokeRect(
                        0,
                        0,
                        640,
                        480
                        );
            }
        }
        context.drawImage(video, 0, 0, 320, 240);
        var data = canvas.toDataURL('image/jpeg').replace("data:image/jpeg;base64,", "");
        var xhr = new XMLHttpRequest();
        xhr.responseType = 'json';
        xhr.open("POST", uploadLink, true);
        xhr.timeout = 2000;
        xhr.onload = function() {
            if(this.status = 200) {
                console.log("response");
            } else {
                console.error(xhr);
            }
            ocontext.clearRect(0, 0, 640, 480);
            draw(this.response);
        };
        xhr.ontimeout = function (e) {
            ocontext.clearRect(0, 0, 640, 480);
            console.log("timeout");
        };
        xhr.send(data);
    }
    var video = document.getElementById('video');
    var canvas = document.getElementById('canvas');
    var context = canvas.getContext('2d');
    var ocanvas = document.getElementById('overlay');
    var ocontext = ocanvas.getContext('2d');
    ocontext.fillStyle = "#FF0000";
    ocontext.strokeStyle = "#FF0000";
    ocontext.lineWidth = "4";
    ocontext.font = "20px sans-serif";
    var uploadLink = document.getElementById("link").getElementsByTagName("a")[0].href
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
            video.srcObject = stream;
            video.play();
            window.setInterval(function() {
                upload();
            }, 2000);    
        });
    }
}

window.addEventListener('load', function(){
    init();
})