document.addEventListener("DOMContentLoaded", function () {
    const sliderContainer = document.querySelector(".slider-container");
    const images = document.querySelectorAll(".slider-container img");
    const prevBtn = document.getElementById("prev-btn");
    const nextBtn = document.getElementById("next-btn");

    let currentIndex = 0;

    function updateSlider() {
        const width = images[0].clientWidth;
        sliderContainer.style.transform = `translateX(-${currentIndex * width}px)`;
    }

    nextBtn.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        updateSlider();
    });

    prevBtn.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        updateSlider();
    });

    window.addEventListener("resize", updateSlider);
});
