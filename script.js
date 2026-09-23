document.addEventListener('DOMContentLoaded', () => {
    // Elegant, non-disruptive fade-ins for that premium feel
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('appear');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    const animatedElements = document.querySelectorAll('.fade-on-scroll');
    animatedElements.forEach(el => observer.observe(el));

    // Force appearance on load for hero elements instantly
    setTimeout(() => {
        document.querySelectorAll('.hero-content, .stats-container').forEach(el => {
            el.classList.add('appear');
        });
    }, 100);
});
