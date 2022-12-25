var PossibleToLoad = false;

window.onload = function()
{
	PossibleToLoad = true;
}

function InsertTr(urls, IsImg)
{
	var insertTr = "";
	
	Tag = 'img';
	if(!IsImg){
		Tag = 'video'
	}

	insertTr += '<tr align="center">';
	for(var i = 0; i < 5; i++)
	{
		insertTr += '<td><a href="'+urls[i]+'&isoriginal=true'+'" target="_blank"><'+Tag+' src="'+urls[i]+'" width="100%" onerror=' + 'this.style.display="none";' + '></a></td>';
	}
	insertTr += "</tr>";

	$("#table").append(insertTr);
}


function ClickItem(Name)
{
	if(!PossibleToLoad)
	{
		alert('10초 후에 클릭해주세요\n과부화 방지를 위해 딜레이를 걸어두었습니다\n보다 많은 인원을 수용하기 위함이니 양해 부탁드립니다');
		return;
	}

	$('.select-1').css('color','white');
	$('.select-2').css('color','white');

	PossibleToLoad = false;

	Token = window.localStorage.getItem('Token');

	var Waiting = true;
	var url = "http://"+BackendURL+"/getcount/?token="+Token+"&imgdir="+Name;
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", url, true);

	xmlHttp.onreadystatechange = function(){
		if(this.status == 200 && this.readyState == this.DONE)
		{
			if(xmlHttp.responseText == 'false'){
				alert('올바르지 않은 경로입니다.');	
			}else{
				var ImageLength = parseInt(xmlHttp.responseText);
				SetImages(Name, ImageLength, Token, Name);
			}
			Waiting = false;
		}
	}

	xmlHttp.send( null );
	setTimeout(function(){
		if(Waiting)
		{
			alert('서버의 상태가 나쁩니다.\n나중에 다시 시도해주세요');
			Waiting = false;
		}
	}, 5000);

	setTimeout(function(){
		PossibleToLoad = true;
		$('.select-1').css('color','black');
		$('.select-2').css('color','black');
	}, 10000)
}

function SetImages(ImageDir, ImageLength, Token, Name)
{
	IsImg = true;
	if(Name == "체육대회-영상")
	{
		IsImg = false;
		alert('영상은 우클릭 -> 다운 후 시청이 가능합니다.\n클릭이 안되어도 당황하지 말아주세요!')
	}
	$("#table tr").remove();

	for(var i = 0; i < ImageLength/5; i++)
	{
		var url = "http://"+BackendURL+"/get/?token="+Token+"&imgdir="+ImageDir+"&imgnum=";
		InsertTr([
			url+((i*5)+0),
			url+((i*5)+1),
			url+((i*5)+2),
			url+((i*5)+3),
			url+((i*5)+4),
		],
		IsImg);
	}
}