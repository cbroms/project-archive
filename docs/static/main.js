// set the copyright notice with the current year
window.addEventListener("DOMContentLoaded", (event) => {
	document.getElementById(
		"copy"
	).innerHTML = `Copyright &copy; ${new Date().getFullYear()} Christian Broms`;
});

// progressively load the images
//https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Loading
window.onload = function () {
	let imagesToLoad = document.querySelectorAll("img[data-src]");

	const loadImages = (image) => {
		image.setAttribute("src", image.getAttribute("data-src"));
		image.onload = () => {
			image.removeAttribute("data-src");
		};
	};

	imagesToLoad.forEach((img) => {
		loadImages(img);
	});
};

let imageElt;

function followCursor(event) {
	imageElt.style.display = "block";
	imageElt.style.left = `${event.clientX}px`;
	imageElt.style.top = `${event.clientY}px`;
}

function showImg(id, elt) {
	imageElt = document.getElementById(id);
	if (imageElt.src.includes("-gif")) {
		imageElt.src = imageElt.src
			.replace("-gif-mid", "")
			.replace(".jpg", ".gif");
	}
	document.body.addEventListener("mousemove", followCursor);
}

function hideImg(id, elt) {
	imageElt.style.display = "none";
	document.body.removeEventListener("mousemove", followCursor);
}
