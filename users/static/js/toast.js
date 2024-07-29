document.addEventListener("DOMContentLoaded", function () {
    const toast = document.querySelector(".toast"),
        closeIcon = document.querySelector(".close"),
        progress = document.querySelector(".progress");

    if (toast) {
        toast.classList.add("active");
        progress.classList.add("active");

        setTimeout(() => {
            toast.classList.remove("active");
        }, 5000);
        setTimeout(() => {
            progress.classList.remove("active");
        }, 5300);
    }

    closeIcon.addEventListener("click", () => {
        toast.classList.remove("active");
        setTimeout(() => {
            progress.classList.remove("active");
        }, 300);
    });
});
