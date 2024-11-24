document.addEventListener('DOMContentLoaded', function() {
    const titleInput = document.querySelector('.title-input');
    const slugInput = document.querySelector('input[name="slug"]');
    const slugDisplay = document.querySelector('#slug-display');

    function generateSlug(text) {
        return text.toString().toLowerCase()
            .replace(/\s+/g, '-')           // Replace spaces with -
            .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
            .replace(/\-\-+/g, '-')         // Replace multiple - with single -
            .replace(/^-+/, '')             // Trim - from start of text
            .replace(/-+$/, '');            // Trim - from end of text
    }

    titleInput.addEventListener('input', function(e) {
        const slug = generateSlug(e.target.value);
        slugInput.value = slug;
        slugDisplay.textContent = slug;
    });
});