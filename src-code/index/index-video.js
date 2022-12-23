window.onload = function()
{
	setInterval(function(){
		if($(".video").prop("ended")){
			window.location.href = 'http://localhost:5500/main-index.html';
		}
	},200);
}