const rainbowText = document.getElementById('rainbow-text');

function changeColor() {
	const colors = ['#FF0000', 'FF70F700', '#FFFF00','#00FF00', '#0000FF', '#4B0082', '8B00FF'];
	let i = 0;
	
	setInterval(() => {
	rainbowText.style.color = colors[i];
	i = (i + 1) % colors.length;
         }, 300);
     } 
     
     changeColor();
