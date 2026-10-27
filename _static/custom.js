function otevrit(co)
{
    seed=Math.round(Math.random()*1000);
    window.open("http://um.mendelu.cz/webwork2/render_rpc?&answersSubmitted=0&sourceFilePath="+co+"&problemSeed="+seed+"&displayMode=MathJax&courseID=daemon&user=demon&passwd=demonek&outputformat=simpleM&language=cs_CZ", "_blank");
};

/* document.onload = function(){
	document.querySelector(".bd-toc").classList.remove("show");
    }; */
