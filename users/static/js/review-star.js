const allStar = document.querySelectorAll('.rating .star');
const ratingValue = document.querySelector('.rating input[name="rating"]'); // Ensuring the correct input is targeted

allStar.forEach((item, idx) => {
    item.addEventListener('click', function () {
        ratingValue.value = idx + 1; // Set rating value to the hidden input field

        allStar.forEach((star, starIdx) => {
            if (starIdx <= idx) {
                star.classList.replace('bx-star', 'bxs-star'); // Change to filled star
                star.classList.add('active');
            } else {
                star.classList.replace('bxs-star', 'bx-star'); // Change to empty star
                star.classList.remove('active');
            }
        });
    });
});
