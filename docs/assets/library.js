// Client-side search for the source library.
(() => {
  const PAGE_SIZE = 50;
  let DATA = [];
  let filtered = [];
  const state = { q: "", c: "", sort: "relevance", described: "any", page: 1 };

  const $ = (id) => document.getElementById(id);
  const esc = (value) =>
    String(value ?? "").replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[ch]));

  function readUrl() {
    const params = new URLSearchParams(location.search);
    state.q = params.get("q") || "";
    state.c = params.get("c") || "";
    state.sort = params.get("sort") || "relevance";
    state.described = params.get("d") || "any";
    state.page = Math.max(1, parseInt(params.get("page") || "1", 10) || 1);
    $("q").value = state.q;
    $("collection").value = state.c;
    $("sort").value = state.sort;
    $("described").value = state.described;
  }

  function writeUrl() {
    const params = new URLSearchParams();
    if (state.q) params.set("q", state.q);
    if (state.c) params.set("c", state.c);
    if (state.sort !== "relevance") params.set("sort", state.sort);
    if (state.described !== "any") params.set("d", state.described);
    if (state.page > 1) params.set("page", String(state.page));
    const query = params.toString();
    history.replaceState(null, "", `${location.pathname}${query ? `?${query}` : ""}`);
  }

  function score(source, terms) {
    const title = source.t.toLowerCase();
    const host = source.h.toLowerCase();
    const desc = source.d.toLowerCase();
    let total = 0;
    for (const term of terms) {
      if (title.includes(term)) total += 6;
      if (title.startsWith(term)) total += 4;
      if (host.includes(term)) total += 3;
      if (desc.includes(term)) total += 1;
    }
    return total;
  }

  function apply() {
    const terms = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    filtered = DATA.filter((source) => {
      if (state.c && source.c !== state.c) return false;
      if (state.described === "yes" && !source.d) return false;
      if (state.described === "no" && source.d) return false;
      if (!terms.length) return true;
      const haystack = `${source.t} ${source.d} ${source.u} ${source.h}`.toLowerCase();
      return terms.every((term) => haystack.includes(term));
    });

    if (state.sort === "title") {
      filtered.sort((a, b) => a.t.localeCompare(b.t));
    } else if (state.sort === "collection") {
      filtered.sort((a, b) => a.cn.localeCompare(b.cn) || a.t.localeCompare(b.t));
    } else if (state.sort === "host") {
      filtered.sort((a, b) => a.h.localeCompare(b.h) || a.t.localeCompare(b.t));
    } else if (terms.length) {
      const scored = new Map(filtered.map((source) => [source.id, score(source, terms)]));
      filtered.sort((a, b) => scored.get(b.id) - scored.get(a.id) || a.t.localeCompare(b.t));
    } else {
      filtered.sort((a, b) => a.t.localeCompare(b.t));
    }

    const pages = Math.max(1, Math.ceil(filtered.length / PAGE_SIZE));
    if (state.page > pages) state.page = pages;
    render();
  }

  function resultMarkup(source) {
    const desc = source.d
      ? `<div class="result-desc">${esc(source.d)}</div>`
      : `<div class="result-desc empty">No description in the source report.</div>`;
    return `<div class="result">
      <div class="result-main">
        <a class="result-title" href="${esc(source.u)}" target="_blank" rel="noopener noreferrer">${esc(source.t)}<span class="host">${esc(source.h)}</span></a>
        ${desc}
      </div>
      <div class="result-side">
        <span class="collection">${esc(source.cn)}</span>
        <button class="copy-btn" type="button" data-url="${esc(source.u)}">copy link</button>
      </div>
    </div>`;
  }

  function render() {
    const start = (state.page - 1) * PAGE_SIZE;
    const pageRows = filtered.slice(start, start + PAGE_SIZE);
    $("results").innerHTML = pageRows.length
      ? pageRows.map(resultMarkup).join("")
      : `<div class="empty-state"><h3>No sources match</h3><p>Try fewer words, a different collection, or reset the filters.</p></div>`;

    const total = filtered.length;
    $("resultCount").textContent = total
      ? `Showing ${start + 1}–${Math.min(start + PAGE_SIZE, total)} of ${total.toLocaleString()} source${total === 1 ? "" : "s"}`
      : "No results";

    const active = [];
    if (state.q) active.push(`query “${esc(state.q)}”`);
    if (state.c) {
      const option = $("collection").selectedOptions[0];
      active.push(`collection “${esc(option ? option.textContent.replace(/ \(\d+\)$/, "") : state.c)}”`);
    }
    if (state.described !== "any") active.push(state.described === "yes" ? "annotated only" : "unannotated only");
    $("activeFilters").innerHTML = active.length
      ? `<span class="filters-on">${active.join(" · ")}</span> <button class="copy-btn" id="resetFilters" type="button">reset</button>`
      : "";

    renderPager(Math.max(1, Math.ceil(total / PAGE_SIZE)));
    const reset = $("resetFilters");
    if (reset) {
      reset.addEventListener("click", () => {
        Object.assign(state, { q: "", c: "", sort: "relevance", described: "any", page: 1 });
        $("q").value = "";
        $("collection").value = "";
        $("sort").value = "relevance";
        $("described").value = "any";
        writeUrl();
        apply();
      });
    }
  }

  function renderPager(pages) {
    const pager = $("pager");
    if (pages <= 1) {
      pager.innerHTML = "";
      return;
    }
    const buttons = [];
    const push = (label, page, options = {}) => {
      buttons.push(
        `<button type="button" data-page="${page}" ${options.disabled ? "disabled" : ""} class="${options.active ? "active" : ""}">${label}</button>`
      );
    };
    push("← prev", state.page - 1, { disabled: state.page === 1 });
    const windowStart = Math.max(1, Math.min(state.page - 2, pages - 4));
    const windowEnd = Math.min(pages, windowStart + 4);
    if (windowStart > 1) {
      push("1", 1);
      if (windowStart > 2) buttons.push(`<span class="muted">…</span>`);
    }
    for (let page = windowStart; page <= windowEnd; page += 1) {
      push(String(page), page, { active: page === state.page });
    }
    if (windowEnd < pages) {
      if (windowEnd < pages - 1) buttons.push(`<span class="muted">…</span>`);
      push(String(pages), pages);
    }
    push("next →", state.page + 1, { disabled: state.page === pages });
    pager.innerHTML = buttons.join("");
  }

  function bind() {
    let timer = null;
    $("q").addEventListener("input", (event) => {
      state.q = event.target.value.trim();
      state.page = 1;
      clearTimeout(timer);
      timer = setTimeout(() => {
        writeUrl();
        apply();
      }, 180);
    });
    for (const [id, key] of [["collection", "c"], ["sort", "sort"], ["described", "described"]]) {
      $(id).addEventListener("change", (event) => {
        state[key] = event.target.value;
        state.page = 1;
        writeUrl();
        apply();
      });
    }
    $("results").addEventListener("click", async (event) => {
      const button = event.target.closest(".copy-btn[data-url]");
      if (!button) return;
      try {
        await navigator.clipboard.writeText(button.dataset.url);
        const original = button.textContent;
        button.textContent = "copied";
        setTimeout(() => (button.textContent = original), 1400);
      } catch {
        window.prompt("Copy this link", button.dataset.url);
      }
    });
    $("pager").addEventListener("click", (event) => {
      const button = event.target.closest("button[data-page]");
      if (!button || button.disabled) return;
      state.page = Math.max(1, parseInt(button.dataset.page, 10));
      writeUrl();
      apply();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "/" && document.activeElement.tagName !== "INPUT" && document.activeElement.tagName !== "SELECT") {
        event.preventDefault();
        $("q").focus();
      }
      if (event.key === "Escape" && document.activeElement === $("q")) $("q").blur();
    });
  }

  fetch("data/library.json")
    .then((response) => {
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      return response.json();
    })
    .then((rows) => {
      DATA = rows;
      readUrl();
      bind();
      apply();
    })
    .catch((error) => {
      $("resultCount").textContent = "Could not load the library";
      $("results").innerHTML = `<div class="empty-state"><h3>Dataset unavailable</h3><p>Serve this page over HTTP (for example <code>python -m http.server</code>) — browsers block local file fetches. ${esc(error.message)}</p></div>`;
    });
})();
