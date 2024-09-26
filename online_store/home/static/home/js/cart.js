function checkLogin() {
    const isAuthenticated = "{{ user.is_authenticated|yesno:'true,false' }}"; // Use Django's template tag

    if (isAuthenticated === 'true') {
        // Code to add product to cart
        alert('Product added to cart!');
    } else {
        alert('Please log in or sign up to add items to your cart.');
        // Redirect to login/signup page
        window.location.href = "{{ url 'login' }}";  // Change to your login URL
    }
}