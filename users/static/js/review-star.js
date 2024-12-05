// Select all star elements and the hidden input field for the rating
const allStars = document.querySelectorAll('.rating .star');
const ratingInput = document.querySelector('.rating input[name="rating"]');

document.addEventListener("DOMContentLoaded", () => {
    const stars = document.querySelectorAll(".rating .star");
    const ratingInput = document.querySelector("input[name='rating']");

    stars.forEach((star, index) => {
        star.addEventListener("click", () => {
            ratingInput.value = index + 1;
            stars.forEach((s, i) => {
                s.classList.toggle("bxs-star", i <= index);
                s.classList.toggle("bx-star", i > index);
            });
        });
    });
});
