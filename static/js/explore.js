document.addEventListener('DOMContentLoaded', function() {
    const likeButtons = document.querySelectorAll('.like-btn');
    const retweetButtons = document.querySelectorAll('.retweet-btn');
    const commentButtons = document.querySelectorAll('.comment-btn');
    const followButtons = document.querySelectorAll('.follow-btn');

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

    followButtons.forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.getAttribute('data-user-id');
            toggleFollow(this, userId);
        });
    });

    function handleLike(postId, button) {
        fetch(`/social/like/${postId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `<i class="fa fa-heart"></i> ${data.likes} Likes`;
            }
        });
    }

    function handleRetweet(postId, button) {
        fetch(`/social/retweet/${postId}/`, { method: 'POST' })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                button.innerHTML = `<i class="fa fa-retweet"></i> ${data.retweets} Retweets`;
            }
        });
    }

    function handleComment(postId) {
        window.location.href = `/social/post/${postId}/#comments`;
    }

    function toggleFollow(button, userId) {
        const icon = button.querySelector('.follow-icon');
        const isFollowing = icon.textContent === '+';

        icon.textContent = isFollowing ? '-' : '+'; // Toggle icon
        button.innerHTML = isFollowing ? '<i class="fas fa-user-plus follow-icon">+</i> Follow' : '<i class="fas fa-user-minus follow-icon">-</i> Unfollow'; // Update button text

        fetch(`/social/explore/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            },
            body: JSON.stringify({ following: userId })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
});