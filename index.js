var canvas = document.querySelector("canvas");
    var context = canvas.getContext("2d");
    const video = document.querySelector('#myVidPlayer');
	
	//w-width,h-height
    var w, h;
    canvas.style.display = "none";
	
	//new
    function snapshot(){
        context.fillRect(0, 0, w, h);
        context.drawImage(video, 0, 0, w, h);
        canvas.style.display = "block";
    }

    window.navigator.mediaDevices.getUserMedia({ video: true, audio: true })
        .then(stream => {
            video.srcObject = stream;
            video.onloadedmetadata = (e) => {
                video.play();
                
                //new
                w = video.videoWidth;
                h = video.videoHeight
                
                canvas.width = w;
                canvas.height = h;
            };
    	})
        .catch(error => {
        	alert('You have to enable the mike and the camera');
    	});