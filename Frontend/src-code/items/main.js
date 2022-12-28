var PossibleToLoad = false;

window.onload = function()
{
	PossibleToLoad = true;
	GetAndSetSelectors();
}

function GetAndSetSelectors()
{
	var url = "http://"+BackendURL+"/getstruct/";
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", url, true);

	xmlHttp.onreadystatechange = function(){
		if(this.status == 200 && this.readyState == this.DONE)
		{
			var Datas = JSON.parse(xmlHttp.responseText);
			insertDiv = "";
			for(var key in Datas) {
				var ClassValue = 'picture-selector';
				if(key[0] == "V")
				{
					ClassValue = 'video-selector';
				}
				insertDiv+='<div onclick="ClickItem(' +"'"+ key +"'"+ ');" class="'+ClassValue+'">▷ '+key+'</div>';
				// console.log(insertDiv);
			}
			$("#selectors").append(insertDiv);

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
}

async function GetImageName(url)
{
	var xmlHttp = new XMLHttpRequest();
	xmlHttp.open( "GET", url, true);

	xmlHttp.onreadystatechange = function(){
		if(this.status == 200 && this.readyState == this.DONE)
		{
			// console.log(xmlHttp.responseText);
			if(xmlHttp.responseText == '"존재하지 않는 데이터입니다."')
			{
				document.getElementById(url).innerHTML = "";
			}
			else
			{
				document.getElementById(url).innerHTML = xmlHttp.responseText;
			}
			// return xmlHttp.responseText;
			Waiting = false;
			return;
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
}

async function InsertTr(urls, IsImg)
{
	var insertTr = "";
	
	Tag = 'img';
	// if(!IsImg){
	// 	Tag = 'video'
	// }

	insertTr += '<tr align="center">';
	for(var i = 0; i < 5; i++)
	{
		if(IsImg)
		{
			insertTr += '<td><a href="'+urls[i]+'&isoriginal=true'+'" target="_blank"><'+Tag+' src="'+urls[i]+'" width="100%" onerror=' + 'this.style.display="none";' + '></a></td>';
		}
		else
		{
			await GetImageName(urls[i]);
			IDValue = urls[i];
			// insertTr += '<td><a href="'+urls[i]+'&isoriginal=true'+'" target="_blank"><'+Tag+' src="./src-content/Video-SmallFile.png" width="100%" onerror=' + 'this.style.display="none";' + '></a></td>';
			insertTr += '<td><a id='+IDValue+' href="'+urls[i]+'&isoriginal=true'+'" target="_blank">이름 로드 중...</a></td>';
		}
	}
	insertTr += "</tr>";

	$("#table").append(insertTr);
}


async function ClickItem(Name)
{
	if(!PossibleToLoad)
	{
		alert('3초 후에 클릭해주세요\n과부화 방지를 위해 딜레이를 걸어두었습니다\n보다 많은 인원을 수용하기 위함이니 양해 부탁드립니다');
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

	xmlHttp.onreadystatechange = async function(){
		if(this.status == 200 && this.readyState == this.DONE)
		{
			if(xmlHttp.responseText == 'false'){
				alert('다시 인증해주세요');	
			}else{
				var ImageLength = parseInt(xmlHttp.responseText);
				await SetImages(Name, ImageLength, Token, Name);
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
	}, 3000)
}

async function SetImages(ImageDir, ImageLength, Token, Name)
{
	IsImg = true;
	if(Name[0] == "V")
	{
		IsImg = false;
		alert('영상은 클릭 -> 다운 후 시청이 가능합니다.\n클릭을 해야 영상으로 이동됩니다!')
	}
	$("#table tr").remove();

	for(var i = 0; i < ImageLength/5; i++)
	{
		var url = "http://"+BackendURL+"/get/?token="+Token+"&imgdir="+ImageDir+"&imgnum=";
		await InsertTr([
			url+((i*5)+0),
			url+((i*5)+1),
			url+((i*5)+2),
			url+((i*5)+3),
			url+((i*5)+4),
		],
		IsImg);
	}
}