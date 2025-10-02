document.addEventListener('DOMContentLoaded', function () {
    const btn = document.querySelector('.menutoggle');
    if (!btn) return;
    btn.addEventListener('click', function () {
        document.body.classList.toggle('open');
    });
});
