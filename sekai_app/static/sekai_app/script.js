document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const toggleButton = document.querySelector('.toggle-sidebar');
    toggleButton.addEventListener('click', function() {
        sidebar.classList.toggle('hidden');
    });
});