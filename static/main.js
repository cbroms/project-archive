// set the copyright notice with the current year
window.addEventListener("DOMContentLoaded", (event) => {
	console.log("hey");

	document.getElementById(
		"copy"
	).innerHTML = `Copyright &copy; ${new Date().getFullYear()} Christian Broms`;
});

// const showImg = (id, elt) => {
// 	document.getElementById(id).style.top = `${
// 		window.pageYOffset + elt.getBoundingClientRect().top
// 	}px`;
// 	document.getElementById(id).style.display = "block";
// };

// const hideImg = (id, elt) => {
// 	document.getElementById(id).style.display = "none";
// };

window.addEventListener("load", function () {
	lazyLoad();
});

function lazyLoad() {
	const images = document.querySelectorAll(".image");

	// loop over each card image
	images.forEach(function (image) {
		var image_url = image.getAttribute("data-image-full");
		var content = image.querySelector("img");

		// change the src of the content image to load the new high res photo
		content.src = image_url;

		// listen for load event when the new photo is finished loading
		content.addEventListener("load", function () {
			// swap out the visible background image with the new fully downloaded photo
			image.style.backgroundImage = "url(" + image_url + ")";
			// add a class to remove the blur filter to smoothly transition the image change
			image.className = image.className + " is-loaded";
		});
	});
}
