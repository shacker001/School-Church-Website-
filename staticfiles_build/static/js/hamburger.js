// home.js

document.addEventListener("DOMContentLoaded", function () {
    const navToggle = document.getElementById("navToggle");
    const navLinks = document.getElementById("navLinks");

    // Log to check if elements are found
    console.log("navToggle:", navToggle);
    console.log("navLinks:", navLinks);

    // Check if navToggle and navLinks exist before adding event listener
    if (navToggle && navLinks) {
        navToggle.addEventListener("click", function () {
            navLinks.classList.toggle("show");
            console.log("Toggle clicked. 'show' class applied:", navLinks.classList.contains("show"));
        });
    } else {
        console.error("navToggle or navLinks element not found.");
    }
});
