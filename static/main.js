// set the copyright notice with the current year
window.addEventListener("DOMContentLoaded", event => {
    console.log("hey");

    document.getElementById(
        "copy"
    ).innerHTML = `Copyright &copy; ${new Date().getFullYear()} Christian Broms`;
});
