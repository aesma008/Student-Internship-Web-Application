// Select all star elements and the hidden input field for the rating
const allStars = document.querySelectorAll('.rating .star');
const ratingInput = document.querySelector('.rating input[name="rating"]');

document.addEventListener("DOMContentLoaded", () => {
    const stars = document.querySelectorAll(".rating .star");
    const ratingInput = document.querySelector("input[name='rating']");

    stars.forEach((star, idx) => {
        star.addEventListener("click", () => {
            ratingInput.value = idx + 1; // Set hidden input value
            stars.forEach((s, sIdx) => {
                if (sIdx <= idx) {
                    s.classList.replace("bx-star", "bxs-star");
                } else {
                    s.classList.replace("bxs-star", "bx-star");
                }
            });
        });
    });
});
