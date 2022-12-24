window.onload = function()
{
	setInterval(function(){
		if($(".video").prop("ended")){
			window.location.href = 'http://'+FrontendURL+'/main-index.html';
			return;
		}
	},200);
}