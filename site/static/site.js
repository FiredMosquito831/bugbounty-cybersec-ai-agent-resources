// Shared behaviour: mobile nav + copy buttons.
(() => {
  const toggle = document.getElementById('navToggle');
  const nav = document.getElementById('siteNav');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
    });
  }

  document.querySelectorAll('[data-copy-text]').forEach((button) => {
    button.addEventListener('click', async () => {
      const text = button.dataset.copyText;
      try {
        await navigator.clipboard.writeText(text);
        const original = button.textContent;
        button.textContent = 'copied';
        setTimeout(() => (button.textContent = original), 1400);
      } catch {
        window.prompt('Copy this command', text);
      }
    });
  });
})();
