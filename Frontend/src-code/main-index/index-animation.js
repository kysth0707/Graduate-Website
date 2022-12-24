window.onload = function()
{
	let Observer = new IntersectionObserver((e)=>{
		e.forEach((박스)=>{
			if(박스.isIntersecting)
			{
				박스.target.style.opacity = 1;
			}
			else
			{
				박스.target.style.opacity = 0;
			}
		});
	});
	
	let Contents = document.getElementsByClassName('animation-content-smooth');
	for(let i = 0; i < Contents.length; i++)
	{
		Observer.observe(Contents[i]);
	}





	let Observer2 = new IntersectionObserver((e)=>{
		e.forEach((박스)=>{
			if(박스.isIntersecting)
			{
				박스.target.style.left = "-20%";
			}
			else
			{
				박스.target.style.left = "0%";
			}
		});
	});
	
	let Contents2 = document.getElementsByClassName('animation-left');
	for(let i = 0; i < Contents2.length; i++)
	{
		Observer2.observe(Contents2[i]);
	}
}