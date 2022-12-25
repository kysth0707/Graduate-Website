var ButtonPossible = true;

function OnLoginButtonClick()
{
	if(!ButtonPossible) {return;}
	ButtonPossible = false;

	if($('#pw-input').val() == ""){
		$('#pw-input').next('label').addClass('warning');
		setTimeout(function(){
			$('label').removeClass('warning')
		}, 1500);
		return;
	}
	pw = $('#pw-input').val();
	$('#btn').text('확인 중...');

	// var WaitingForResponse = true;

	var url = "http://"+BackendURL+"/gettoken/?pw="+pw;
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", url, true);

	xmlHttp.onreadystatechange = function(){
		if(this.status == 200 && this.readyState == this.DONE)
		{
			if(xmlHttp.responseText == 'false'){
				$('#top').text('비밀번호가 틀렸습니다');
				$('#btn').text('인증하기');
				setTimeout(function(){
					$('#top').text('인증 절차');
				}, 1500);
			}else{
				var Token = JSON.parse(xmlHttp.responseText).Token;
				console.log(Token);
				window.localStorage.setItem('Token', Token);
				window.location.href = 'http://'+FrontendURL+'/items.html';
			}
			ButtonPossible = true;
		}
	}

	xmlHttp.send( null );
	setTimeout(function(){
		if(!ButtonPossible)
		{
			$('#btn').text('나중에 다시 시도해주세요');
			$('#top').text('서버 상태가 나쁩니다');
			ButtonPossible = true;
		}
	}, 5000);
}