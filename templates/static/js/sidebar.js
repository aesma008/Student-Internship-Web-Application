const body = document.querySelector("body"),
    sidebar = body.querySelector(".sidebar"),
    toggle = body.querySelector(".toggle"),
    modeSwitch = body.querySelector(".mode"),
    modeText = body.querySelector(".mode-text");

// Function to apply the theme
function applyTheme(theme) {
    if (theme === "dark") {
        body.classList.add("dark");
        modeText.innerText = "Light Mode";
    } else {
        body.classList.remove("dark");
        modeText.innerText = "Dark Mode";
    }
}

// Load theme preference from local storage and apply it
const currentTheme = localStorage.getItem("theme") || "light";
applyTheme(currentTheme);

modeSwitch.addEventListener("click", () => {
    const newTheme = body.classList.contains("dark") ? "light" : "dark";
    applyTheme(newTheme);
    localStorage.setItem("theme", newTheme);
});

toggle.addEventListener("click", () => {
    sidebar.classList.toggle("close");
});