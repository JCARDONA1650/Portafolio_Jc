/*
 * JavaScript for dynamic effects on the portfolio site.
 *
 * This script populates the floating background with multiple letters that
 * drift slowly upward while rotating. It runs after the DOM has loaded.
 */

document.addEventListener('DOMContentLoaded', () => {
  const container = document.getElementById('floating-container');
  if (!container) return;

  const quantity = Math.floor(window.innerWidth / 30); // scale number with screen width
  for (let i = 0; i < quantity; i++) {
    const span = document.createElement('span');
    span.classList.add('floating-letter');
    span.textContent = 'J';

    // Randomize properties
    const size = Math.random() * 20 + 10; // font size between 10–30px
    span.style.fontSize = `${size}px`;
    span.style.left = `${Math.random() * 100}%`;
    span.style.animationDuration = `${Math.random() * 20 + 15}s`; // 15–35s
    span.style.animationDelay = `${Math.random() * 10}s`;
    span.style.opacity = (Math.random() * 0.1 + 0.05).toString(); // very subtle

    container.appendChild(span);
  }
});