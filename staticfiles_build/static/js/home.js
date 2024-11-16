// home.js

document.addEventListener("DOMContentLoaded", function () {
    console.log("JavaScript is working"); // This should appear in the console if JavaScript is loaded
    const navToggle = document.getElementById("navToggle");
    const navLinks = document.getElementById("navLinks");

    // Toggle navigation visibility on click
    navToggle.addEventListener("click", function () {
        navLinks.classList.toggle("show");
        console.log("Hamburger icon clicked"); // This should appear in the console on click
    });
});
