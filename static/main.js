// set the copyright notice with the current year
window.addEventListener("DOMContentLoaded", (event) => {
	document.getElementById(
		"copy"
	).innerHTML = `Copyright &copy; ${new Date().getFullYear()} Christian Broms`;

	const header = document.getElementById("header-link");
	header.innerHTML = generateRandomEmote();
});

const generateRandomEmote = () => {
	// get a random member of the array
	const r = (arr) => {
		return arr[Math.floor(Math.random() * arr.length)];
	};

	const style1 = () => {
		const mouths = [")", "O", "D", "P", "/", "]", "|", "3"];
		const eyes = [":", ";"];
		const noses = ["-", "*", "~", "", "", ""];
		return r(eyes) + r(noses) + r(mouths);
	};

	const style2 = () => {
		const leftSides = ["(", "<(", "\\(", "—("];
		const eyes = ["o", "O", "-", "X", "T", "*", "@", "^", "~", "!"];
		const mouths = ["o", "_", ".", "x"];
		const rightSides = [")", ")>", ")/", ")—"];

		const ey = r(eyes);
		return r(leftSides) + ey + r(mouths) + ey + r(rightSides);
	};

	const styles = [style1, style2];

	return r(styles)();
};

// progressively load the images
//https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Loading
window.onload = function() {
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
	if (!("ontouchstart" in window)) {
		imageElt.style.display = "block";
		imageElt.style.left = `${event.clientX}px`;
		imageElt.style.top = `${event.clientY}px`;
	}
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
