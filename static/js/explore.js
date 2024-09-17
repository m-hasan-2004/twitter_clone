document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-btn');
    const retweetButtons = document.querySelectorAll('.retweet-btn');
    const commentButtons = document.querySelectorAll('.comment-btn');

    likeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            handleLike(postId, this);
        });
    });

    retweetButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            handleRetweet(postId, this);
        });
    });

    commentButtons.forEach(button => {
        button.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            handleComment(postId);
        });
    });

    function handleLike(postId, button) {
        // Perform AJAX request to like the post
        fetch(`/social/like/${postId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `<i class="fa fa-heart"></i> ${data.likes} Likes`;
            }
        });
    }

    function handleRetweet(postId, button) {
        // Perform AJAX request to retweet the post
        fetch(`/social/retweet/${postId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `<i class="fa fa-retweet"></i> ${data.retweets} Retweets`;
            }
        });
    }

    function handleComment(postId) {
        // Redirect to post comment section
        window.location.href = `/social/post/${postId}/#comments`;