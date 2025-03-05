document.addEventListener('DOMContentLoaded', () => {
    // Parallax Hover Effect
    document.querySelectorAll('.parallax-layer').forEach(layer => {
        layer.addEventListener('mousemove', (e) => {
            const { left, top, width, height } = e.target.getBoundingClientRect()
            const x = (e.clientX - left) / width - 0.5
            const y = (e.clientY - top) / height - 0.5
            
            e.target.style.transform = `
                translate3d(${x * 15}px, ${y * 15}px, 0)
                rotateX(${y * -8}deg)
                rotateY(${x * 8}deg)
            `
        })
        
        layer.addEventListener('mouseleave', () => {
            layer.style.transform = 'translate3d(0, 0, 0)'
        })
    })

    // Dynamic Border Follow
    const container = document.querySelector('.container')
    const dynamicBorder = document.querySelector('.dynamic-border')
    
    container.addEventListener('mousemove', (e) => {
        const rect = container.getBoundingClientRect()
        const x = e.clientX - rect.left
        const y = e.clientY - rect.top
        
        dynamicBorder.style.background = `
            conic-gradient(
                from ${Math.atan2(y - rect.height/2, x - rect.width/2)}rad,
                var(--stellar-blue),
                var(--quantum-purple),
                var(--hologram-teal),
                var(--stellar-blue)
            )
        `
    })

    // Particle Field Interaction
    document.querySelector('.holographic-card').addEventListener('mousemove', (e) => {
        const particles = document.createElement('div')
        particles.className = 'particle-trail'
        particles.style.left = `${e.clientX}px`
        particles.style.top = `${e.clientY}px`
        document.body.appendChild(particles)
        
        setTimeout(() => particles.remove(), 1000)
    })
})

document.addEventListener('DOMContentLoaded', () => {
    const holographicCard = document.querySelector('.holographic-card');
    const fileInput = document.querySelector('input[type="file"]');

    holographicCard.addEventListener('click', () => {
        fileInput.click();
    });

    holographicCard.addEventListener('dragover', (e) => {
        e.preventDefault();
        holographicCard.classList.add('drag-over');
    });

    holographicCard.addEventListener('dragleave', () => {
        holographicCard.classList.remove('drag-over');
    });

    holographicCard.addEventListener('drop', (e) => {
        e.preventDefault();
        holographicCard.classList.remove('drag-over');
        const files = e.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
        }
    });
});

// Add to animations.js
document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const submitButton = form.querySelector('button[type="submit"]');
    const fileInput = form.querySelector('input[type="file"]');
    const fileNameDisplay = form.querySelector('.file-name');
    const hologramCard = form.querySelector('.holographic-card');

    // File input handling
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            hologramCard.classList.add('file-uploaded');
            fileNameDisplay.textContent = fileInput.files[0].name;
        }
    });

    // Form submission handling
    form.addEventListener('submit', (e) => {
        if (fileInput.files.length > 0) {
            submitButton.classList.add('loading');
            submitButton.disabled = true;
            submitButton.querySelector('.button-text').textContent = 'Analyzing...';
        } else {
            e.preventDefault();
        }
    });

    // Drag and drop feedback
    hologramCard.addEventListener('dragover', () => {
        hologramCard.classList.add('dragover');
    });

    hologramCard.addEventListener('dragleave', () => {
        hologramCard.classList.remove('dragover');
    });

    hologramCard.addEventListener('drop', () => {
        hologramCard.classList.remove('dragover');
    });
});