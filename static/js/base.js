// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    const tabLinks = document.querySelectorAll(".tab-link");
    const tabPanes = document.querySelectorAll(".tab-pane");

    tabLinks.forEach(function(link) {
        link.addEventListener("click", function(event) {
            event.preventDefault();

            // Remove active class from all links
            tabLinks.forEach(function(item) {
                item.classList.remove("active");
            });

            // Remove active class from all panes
            tabPanes.forEach(function(pane) {
                pane.classList.remove("active");
            });

            // Add active class to clicked link
            this.classList.add("active");

            // Show the corresponding tab pane
            const tabId = this.getAttribute("data-tab");
            document.getElementById(tabId).classList.add("active");
        });
    });
});
