function otevrit(co)
{
    seed=Math.round(Math.random()*1000);
    window.open("http://um.mendelu.cz/webwork2/html2xml?&answersSubmitted=0&sourceFilePath="+co+"&problemSeed="+seed+"&displayMode=MathJax&courseID=daemon&userID=demon&course_password=demonek&outputformat=simpleM&language=cs_CZ", "_blank");
};

document.onload = function(){
	document.querySelector(".bd-toc").classList.remove("show");
    };
