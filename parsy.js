// quick little DOM navigation to get my links

// need to pull down the HTML so I can traverse it with this
var websites = document.getElementsByClassName("row_name");
i=0;
function grabNames(){
	while (i < websites.length) {
		sitesArray = websites[i].innerText;
		i++;
	}
}
grabNames();
console.log(sitesArray); //need to test that this is working

//