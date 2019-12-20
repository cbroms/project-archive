// set the copyright notice with the current year
window.addEventListener("DOMContentLoaded", event => {
    console.log("hey");

    document.getElementById(
        "copy"
    ).innerHTML = `Copyright &copy; ${new Date().getFullYear()} Christian Broms`;
});

const showImg = (id, elt) => {
    document.getElementById(id).style.top = `${window.pageYOffset +
        elt.getBoundingClientRect().top}px`;
    document.getElementById(id).style.display = "block";
};

const hideImg = (id, elt) => {
    document.getElementById(id).style.display = "none";
};
