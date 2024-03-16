document.addEventListener("DOMContentLoaded", function() {
    const searchButton = document.getElementById("search");
    const searchBox = document.getElementById("searchbox");
    const uploadButton = document.getElementById("upload");
    const uploadBox = document.getElementById("uploadbox");
    
    // Search functionality
    searchButton.addEventListener("click", function() {
        const searchTerm = searchBox.value.trim().toLowerCase();
        const articles = document.querySelectorAll(".article");

        articles.forEach(function(article) {
            const title = article.querySelector(".article-title").textContent.toLowerCase();
            const description = article.querySelector(".article-description").textContent.toLowerCase();

            if (title.includes(searchTerm) || description.includes(searchTerm)) {
                article.style.display = "block";
            } else {
                article.style.display = "none";
            }
        });

        searchBox.value = "";
    });

    // Upload functionality (dummy implementation)
    uploadButton.addEventListener("click", function() {
        const newArticleContent = uploadBox.value.trim();

        // Dummy implementation: Log the uploaded content to console
        console.log("Uploaded article content:");
        console.log(newArticleContent);

        // Dummy implementation: Clear the upload box after uploading
        uploadBox.value = "";
    });
});
