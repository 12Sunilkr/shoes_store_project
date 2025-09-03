// Main JavaScript for StepStyle Shoes Store

document.addEventListener('DOMContentLoaded', function() {
    
    // Initialize all features
    initializeCartCounter();
    initializeProductCards();
    initializeSearch();
    initializeTooltips();
    initializeAnimations();
    
    // Cart Counter Update
    function initializeCartCounter() {
        updateCartCounter();
    }
    
    function updateCartCounter() {
        // This would typically be updated via AJAX after cart operations
        // For now, it's handled by Django template context
    }
    
    // Product Card Interactions
    function initializeProductCards() {
        const productCards = document.querySelectorAll('.product-card');
        
        productCards.forEach(card => {
            // Add hover effects
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-5px)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
            
            // Quick view functionality (placeholder)
            const quickViewBtn = card.querySelector('.quick-view-btn');
            if (quickViewBtn) {
                quickViewBtn.addEventListener('click', function(e) {
                    e.preventDefault();
                    // Quick view modal would be implemented here
                    console.log('Quick view clicked');
                });
            }
        });
    }
    
    // Search Enhancement
    function initializeSearch() {
        const searchInput = document.querySelector('input[name="q"]');
        
        if (searchInput) {
            // Add search suggestions (placeholder)
            searchInput.addEventListener('input', debounce(function() {
                const query = this.value;
                if (query.length > 2) {
                    // Implement search suggestions here
                    console.log('Search suggestions for:', query);
                }
            }, 300));
            
            // Enter key search
            searchInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    this.form.submit();
                }
            });
        }
    }
    
    // Tooltips
    function initializeTooltips() {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }
    
    // Animations
    function initializeAnimations() {
        // Fade in animations for elements
        const animatedElements = document.querySelectorAll('.fade-in-up');
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in-up');
                    observer.unobserve(entry.target);
                }
            });
        });
        
        animatedElements.forEach(el => observer.observe(el));
    }
    
    // Wishlist functionality (placeholder)
    window.toggleWishlist = function(productId) {
        console.log('Toggle wishlist for product:', productId);
        // Implement wishlist toggle here
        
        // Show feedback
        showToast('Added to wishlist!', 'success');
    };
    
    // Toast notifications
    window.showToast = function(message, type = 'info') {
        const toastContainer = getOrCreateToastContainer();
        
        const toastHtml = `
            <div class="toast align-items-center text-white bg-${type === 'error' ? 'danger' : type === 'success' ? 'success' : 'primary'} border-0" role="alert">
                <div class="d-flex">
                    <div class="toast-body">${message}</div>
                    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
                </div>
            </div>
        `;
        
        const toastElement = document.createElement('div');
        toastElement.innerHTML = toastHtml;
        const toast = toastElement.firstElementChild;
        
        toastContainer.appendChild(toast);
        
        const bsToast = new bootstrap.Toast(toast);
        bsToast.show();
        
        // Remove toast after it's hidden
        toast.addEventListener('hidden.bs.toast', function () {
            toast.remove();
        });
    };
    
    function getOrCreateToastContainer() {
        let container = document.getElementById('toast-container');
        if (!container) {
            container = document.createElement('div');
            container.id = 'toast-container';
            container.className = 'toast-container position-fixed top-0 end-0 p-3';
            container.style.zIndex = '9999';
            document.body.appendChild(container);
        }
        return container;
    }
    
    // Form enhancements
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                // Add loading state
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Processing...';
                submitBtn.disabled = true;
                
                // Re-enable after 3 seconds (fallback)
                setTimeout(() => {
                    submitBtn.innerHTML = originalText;
                    submitBtn.disabled = false;
                }, 3000);
            }
        });
    });
    
    // Quantity input validation
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            const min = parseInt(this.min) || 1;
            const max = parseInt(this.max) || 999;
            let value = parseInt(this.value) || min;
            
            if (value < min) value = min;
            if (value > max) value = max;
            
            this.value = value;
        });
    });
    
    // Price filters (placeholder implementation)
    const priceFilters = document.querySelectorAll('input[type="checkbox"][id^="price"]');
    priceFilters.forEach(filter => {
        filter.addEventListener('change', function() {
            console.log('Price filter changed:', this.id, this.checked);
            // Implement price filtering here
        });
    });
    
    // Image lazy loading
    if ('IntersectionObserver' in window) {
        const imageObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.classList.remove('lazy');
                    observer.unobserve(img);
                }
            });
        });
        
        const lazyImages = document.querySelectorAll('img[data-src]');
        lazyImages.forEach(img => imageObserver.observe(img));
    }
    
    // Back to top button
    const backToTop = document.createElement('button');
    backToTop.innerHTML = '<i class="fas fa-arrow-up"></i>';
    backToTop.className = 'btn btn-primary position-fixed';
    backToTop.style.cssText = 'bottom: 20px; right: 20px; z-index: 999; border-radius: 50%; width: 50px; height: 50px; display: none;';
    backToTop.setAttribute('aria-label', 'Back to top');
    document.body.appendChild(backToTop);
    
    window.addEventListener('scroll', () => {
        if (window.pageYOffset > 300) {
            backToTop.style.display = 'block';
        } else {
            backToTop.style.display = 'none';
        }
    });
    
    backToTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
    
});

// Utility Functions
function debounce(func, wait, immediate) {
    let timeout;
    return function executedFunction() {
        const context = this;
        const args = arguments;
        const later = function() {
            timeout = null;
            if (!immediate) func.apply(context, args);
        };
        const callNow = immediate && !timeout;
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
        if (callNow) func.apply(context, args);
    };
}

// Global cart functions
window.addToCart = function(productId, quantity = 1) {
    console.log('Adding to cart:', productId, quantity);
    // This would typically make an AJAX request
    showToast('Product added to cart!', 'success');
};

window.removeFromCart = function(productId) {
    if (confirm('Remove this item from cart?')) {
        console.log('Removing from cart:', productId);
        // This would typically make an AJAX request
        showToast('Product removed from cart!', 'info');
    }
};
