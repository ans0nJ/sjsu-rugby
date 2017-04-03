$(document).ready(function(){
	$("tr:odd").css("background-color", "#cccccc");
	if($(window).width() < 768){
		$(".navbar .active a").css("border-bottom", "none");
	}
});