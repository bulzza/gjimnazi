document.querySelectorAll('.edit-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Show editSection and hide tableSection
        document.getElementById('editSection').style.display = 'block';
        document.getElementById('tableSection').style.display = 'none';
    });
});

document.querySelectorAll('.cancel-btn').forEach(button => {
    button.addEventListener('click', function() {
        // Hide editSection and show tableSection
        document.getElementById('editSection').style.display = 'none';
        document.getElementById('tableSection').style.display = 'block';
    });
});
