// app/static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Add interactive hover effects for cards
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 10px 20px rgba(24, 119, 242, 0.1)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.05)';
        });
    });

    // Add search functionality enhancement
    const searchInput = document.querySelector('input[name="query"]');
    if (searchInput) {
        searchInput.addEventListener('focus', function() {
            this.style.boxShadow = '0 0 0 0.25rem rgba(24, 119, 242, 0.25)';
        });
        
        searchInput.addEventListener('blur', function() {
            this.style.boxShadow = 'none';
        });
    }
});
