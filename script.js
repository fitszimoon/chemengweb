// Sidebar toggle function
function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    var mainContent = document.getElementById('main-content');
    sidebar.classList.toggle('open');
    mainContent.classList.toggle('shifted');
    document.getElementById('header').classList.toggle('shifted');
}

function changeBackground(imageUrl) {
    const overlay = document.getElementById('background-overlay');
    overlay.style.backgroundImage = `url(${imageUrl})`;
    overlay.style.opacity = 1;
}

function resetBackground() {
    const overlay = document.getElementById('background-overlay');
    overlay.style.opacity = 0;
}
