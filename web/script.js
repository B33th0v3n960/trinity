document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('changeTextButton');
    button.addEventListener('click', () => {
        document.getElementById('text').textContent = 'Texte a converti!';
    });
});
