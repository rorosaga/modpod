'use strict';
const project = JSON.parse(document.getElementById('project-data').textContent);
const sources = Object.fromEntries(project.sources.map(source => [source.id, source]));
const workspace = document.getElementById('workspace');
const storageKey = 'modpod-checklist-v1';
let storageAvailable = true;
let progress = {};
let selectedTheme = (project.themes.find(theme => theme.slug === 'piplupos') || project.themes[0]).slug;
let draftTheme = structuredClone(project.themes.find(theme => theme.slug === selectedTheme));
let referenceFilter = 'all';
let noticeTimer;

const escape = value => String(value).replace(/[&<>"']/g, character => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[character]));
const link = source => `<a href="${escape(source.url)}" target="_blank" rel="noopener noreferrer">${escape(source.title)}</a>`;
const taskKey = (stage, task) => `${stage.id}:${task.id}`;
try {
  const stored = JSON.parse(localStorage.getItem(storageKey) || '{}');
  for (const stage of project.content.stages) {
    for (const task of stage.checklist) {
      const key = taskKey(stage, task);
      progress[key] = typeof stored?.[key] === 'boolean' ? stored[key] : Boolean(task.complete);
    }
  }
  localStorage.setItem(storageKey, JSON.stringify(progress));
} catch {
  storageAvailable = false;
  for (const stage of project.content.stages) for (const task of stage.checklist) progress[taskKey(stage, task)] = Boolean(task.complete);
}

function notify(message) {
  const notice = document.getElementById('notice');
  notice.textContent = message;
  notice.classList.add('visible');
  clearTimeout(noticeTimer);
  noticeTimer = setTimeout(() => notice.classList.remove('visible'), 4000);
}

function download(name, value) {
  const url = URL.createObjectURL(new Blob([JSON.stringify(value, null, 2) + '\n'], {type:'application/json'}));
  const anchor = document.createElement('a');
  anchor.href = url; anchor.download = name;
  document.body.append(anchor); anchor.click(); anchor.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

function header(eyebrow, title, intro) {
  return `<div class="page-head"><div><p class="eyebrow">${escape(eyebrow)}</p><h1>${escape(title)}</h1></div><p class="intro">${escape(intro)}</p></div>`;
}

function renderBuild(id) {
  const stages = project.content.stages;
  const stage = stages.find(item => item.id === id) || stages[0];
  const tasks = stages.flatMap(item => item.checklist.map(task => taskKey(item, task)));
  const complete = tasks.filter(key => progress[key]).length;
  return header('01 / THE BUILD', 'From parts to PiplupOS.', 'The Quad and battery are installed. Native Mac theme tests work; FAT32 conversion and physical Rockbox installation come next. Keep your Mac song originals for the restore and resync.') + `
    <div class="build-layout">
      <aside class="build-aside" aria-label="Build stages">
        <p class="aside-heading">FOLLOW THE BUILD</p>
        <div class="step-list">${stages.map(item => {
          const done = item.checklist.filter(task => progress[taskKey(item, task)]).length;
          return `<button class="step-button" data-stage="${item.id}" ${item.id === stage.id ? 'aria-current="step"' : ''}><span class="step-number">${item.number}</span><span class="step-copy"><strong>${escape(item.title)}</strong><small>${done} of ${item.checklist.length} checkpoints</small></span></button>`;
        }).join('')}</div>
        <div class="build-progress"><div class="progress-line"><span>YOUR CHECKLIST</span><span>${complete} / ${tasks.length}</span></div><progress max="${tasks.length}" value="${complete}" aria-label="Completed build checkpoints"></progress><button class="text-button" data-action="export-progress">Export progress</button><p class="small-note">${storageAvailable ? 'Saved in this browser. Export a backup; record real test results in the build log.' : 'Browser storage is unavailable. Export progress before closing this page.'}</p></div>
      </aside>
      <article class="guide" aria-labelledby="guide-title">
        <p class="eyebrow">STAGE ${stage.number} / GUIDE</p>
        <h2 id="guide-title">${escape(stage.title)}</h2>
        <p class="guide-before">${escape(stage.before)}</p>
        ${stage.steps.map((step, index) => `<section class="guide-step"><span class="number">${String(index + 1).padStart(2,'0')}</span><div><h3>${escape(step.title)}</h3><p>${escape(step.body)}</p></div></section>`).join('')}
        <p class="callout">${escape(stage.note)}</p>
        <section class="checklist"><h3>Checkpoints</h3>${stage.checklist.map(task => `<label class="task"><input type="checkbox" data-task="${taskKey(stage, task)}" ${progress[taskKey(stage, task)] ? 'checked' : ''}><span>${escape(task.text)}</span></label>`).join('')}</section>
        <section class="source-links"><h3>Keep these guides open</h3>${stage.sources.map(id => link(sources[id])).join('')}</section>
      </article>
    </div>`;
}

function renderParts() {
  return header('02 / THE PARTS', 'On the workbench.', 'Your purchased parts, with the exact links you supplied. Product specifications are advertised; clearance and card compatibility still need a real build test.') + `<section class="parts-list" aria-label="Purchased parts">${project.parts.map(part => `
    <article class="part-row"><figure class="part-photo"><img src="${escape(part.image)}" alt="${escape(part.name)} product photo" loading="lazy" referrerpolicy="no-referrer"><p class="photo-unavailable" hidden>Product photo unavailable offline. Open the seller link to view it.</p><figcaption>${escape(part.image_credit)}</figcaption></figure><div class="part-info"><div class="part-meta"><span>${escape(part.category.toUpperCase())}</span><span>${escape(part.seller)}</span></div><h2>${escape(part.name)}</h2><p>${escape(part.details)}</p><p class="part-pending"><strong>Before the build:</strong> ${escape(part.pending)}</p><a class="part-link" href="${escape(part.url)}" target="_blank" rel="noopener noreferrer">Open product listing ↗</a><p class="small-note">${escape(part.purchase_status)}</p></div></article>`).join('')}</section>`;
}

function previewSVG(theme) {
  const c = theme.colors;
  return `<svg viewBox="0 0 320 240" role="img" aria-label="${escape(theme.name)} playback layout illustration" xmlns="http://www.w3.org/2000/svg"><rect width="320" height="240" fill="#${c.background}"/><g font-family="monospace" fill="#${c.foreground}"><text x="12" y="23" font-size="10" fill="#${c.muted}">MODPOD</text><text x="308" y="23" text-anchor="end" font-size="10" fill="#${c.muted}">87%</text><text x="12" y="69" font-size="17" fill="#${c.accent}">Weird Fishes / Arpeggi</text><text x="12" y="99" font-size="13">Radiohead</text><text x="12" y="125" font-size="11" fill="#${c.muted}">In Rainbows</text><rect x="12" y="170" width="296" height="6" fill="#${c.muted}" opacity=".2"/><rect x="12" y="170" width="122" height="6" fill="#${c.accent}"/><text x="12" y="200" font-size="11">2:11</text><text x="308" y="200" text-anchor="end" font-size="11">5:18</text><text x="12" y="229" font-size="10" fill="#${c.muted}">Playing</text><text x="308" y="229" text-anchor="end" font-size="10" fill="#${c.muted}">-18 dB</text></g></svg>`;
}

function renderThemes() {
  return header('03 / THE THEME WORKSHOP', 'A small screen. Yours.', 'PiplupOS has native Mac checks. Use the palette illustration to explore text colors; real simulator captures are below. Delayed headphones need custom firmware; the standard skin changes immediately on pause.') + `
    <section class="theme-layout" aria-label="Theme workshop">
      <div class="theme-choices"><div>${project.themes.map(theme => `<button class="theme-option" data-theme="${theme.slug}" aria-pressed="${theme.slug === selectedTheme}"><strong>${escape(theme.name)}</strong><small>${escape(theme.description)}</small><span class="swatches" aria-hidden="true">${Object.values(theme.colors).map(color => `<span class="swatch" style="background:#${color}"></span>`).join('')}</span></button>`).join('')}</div></div>
      <div class="theme-preview"><div class="ipod"><div class="ipod-screen" id="screen-preview">${previewSVG(draftTheme)}</div><div class="click-wheel" aria-hidden="true">MENU<span class="wheel-center"></span><span class="wheel-left">◀◀</span><span class="wheel-right">▶▶</span><span class="wheel-bottom">▶Ⅱ</span></div></div><p class="preview-note">GENERIC PALETTE ILLUSTRATION<br>NATIVE PIPLUPOS CAPTURES BELOW · DEVICE TEST PENDING</p></div>
      <div class="palette-editor"><fieldset class="palette"><legend>EDIT THE PALETTE</legend>${Object.entries(draftTheme.colors).map(([key, color]) => `<label class="color-field"><span>${escape(key[0].toUpperCase() + key.slice(1))}</span><span class="color-inputs"><code id="hex-${key}">#${color}</code><input type="color" value="#${color}" data-color="${key}" aria-label="${escape(key)} color"></span></label>`).join('')}</fieldset><div class="palette-actions"><button class="button" data-action="download-theme">Download theme.json</button><button class="button secondary" data-action="reset-theme">Reset palette</button></div><p class="small-note">Replace <strong>themes/${escape(selectedTheme)}/theme.json</strong> with the downloaded file, then rebuild. Downloading does not change your repository.</p><p class="small-note">${escape(draftTheme.status)}</p></div>
    </section>
    <section class="native-captures" aria-label="Native PiplupOS simulator captures">${(project.native_renders || []).map(render => `<figure><img src="${escape(render.image)}" width="320" height="240" alt="${escape(render.label)}"><figcaption>${escape(render.label)} · native 320 × 240 render, 1 October 2026</figcaption></figure>`).join('')}</section>
    <section class="theme-howto"><div><h3>Make another theme</h3><p>Create a separate folder to keep your originals. The CLI copies native templates and assets. Edit bitmap colors in Aseprite; manifest colors alone do not recolor PiplupOS artwork.</p><pre>python3 tools/modpod.py new my-theme --from ${escape(selectedTheme)}\npython3 tools/modpod.py build my-theme</pre></div><div><h3>Build this palette</h3><p>After saving the manifest, this refreshes the handbook and creates a package in dist/themes/.</p><pre>python3 tools/modpod.py build ${escape(selectedTheme)}</pre><p>Stage and recheck modified themes in the Mac simulator. Native PiplupOS results are in docs/BUILD_LOG.md; device tests remain pending. Merge a standard-compatible package only after Rockbox works. The experimental timers skin requires custom firmware.</p></div></section>`;
}

function renderReferences() {
  const matches = source => referenceFilter === 'all' || (referenceFilter === 'rockbox' && source.kind === 'Official manual') || (referenceFilter === 'repair' && /guide/i.test(source.kind)) || (referenceFilter === 'videos' && source.kind.startsWith('Video'));
  const filters = {all:'All references',repair:'Repair guides',rockbox:'Rockbox',videos:'Videos'};
  return header('04 / THE REFERENCES', 'Keep the good guides.', 'Primary repair and Rockbox references first. Video titles and descriptions were checked; viewing notes and timestamps are still to be added.') + `
    <div class="reference-filters" aria-label="Filter references">${Object.entries(filters).map(([key, label]) => `<button class="filter" data-filter="${key}" aria-pressed="${key === referenceFilter}">${label}</button>`).join('')}</div>
    <section class="reference-list" aria-label="Reference links">${project.sources.filter(matches).map(source => `<article class="reference-row"><div class="reference-type">${escape(source.kind)}<br>CHECKED ${escape(source.checked)}${source.author ? '<br>' + escape(source.author) : ''}</div><div><h2>${link(source)} ↗</h2><p>${escape(source.note)}</p></div></article>`).join('')}</section>`;
}

function render() {
  const [requested, id] = location.hash.slice(1).split('/');
  const page = ['build','parts','themes','references'].includes(requested) ? requested : 'build';
  for (const anchor of document.querySelectorAll('[data-page]')) {
    if (anchor.dataset.page === page) anchor.setAttribute('aria-current','page');
    else anchor.removeAttribute('aria-current');
  }
  workspace.innerHTML = page === 'build' ? renderBuild(id) : page === 'parts' ? renderParts() : page === 'themes' ? renderThemes() : renderReferences();
  document.title = `Modpod — ${page === 'build' ? 'build notebook' : page}`;
}

document.addEventListener('click', event => {
  const button = event.target.closest('button');
  if (!button) return;
  if (button.dataset.stage) location.hash = `build/${button.dataset.stage}`;
  if (button.dataset.theme) {
    selectedTheme = button.dataset.theme;
    draftTheme = structuredClone(project.themes.find(theme => theme.slug === selectedTheme));
    render();
    document.querySelector(`[data-theme="${selectedTheme}"]`).focus({preventScroll:true});
  }
  if (button.dataset.filter) {
    referenceFilter = button.dataset.filter; render();
    document.querySelector(`[data-filter="${referenceFilter}"]`).focus({preventScroll:true});
  }
  if (button.dataset.action === 'export-progress') {
    download('modpod-progress.json', {version:1, exported:new Date().toISOString(), checkpoints:progress});
    notify('Progress exported. Keep the file with your build notes.');
  }
  if (button.dataset.action === 'download-theme') {
    const value = structuredClone(draftTheme);
    value.status = 'Draft · not tested in Rockbox';
    download('theme.json', value);
    notify(`Downloaded ${value.name} manifest. Save it in themes/${value.slug}/.`);
  }
  if (button.dataset.action === 'reset-theme') {
    draftTheme = structuredClone(project.themes.find(theme => theme.slug === selectedTheme));
    render(); document.querySelector('[data-action="reset-theme"]').focus({preventScroll:true});
  }
});

document.addEventListener('change', event => {
  const key = event.target.dataset.task;
  if (!key) return;
  progress[key] = event.target.checked;
  try { localStorage.setItem(storageKey, JSON.stringify(progress)); }
  catch { storageAvailable = false; notify('Could not save in this browser. Export your progress.'); }
  render();
  document.querySelector(`[data-task="${key}"]`).focus({preventScroll:true});
});

document.addEventListener('input', event => {
  const color = event.target.dataset.color;
  if (!color) return;
  draftTheme.colors[color] = event.target.value.slice(1).toUpperCase();
  document.getElementById(`hex-${color}`).textContent = event.target.value.toUpperCase();
  document.getElementById('screen-preview').innerHTML = previewSVG(draftTheme);
});

document.addEventListener('error', event => {
  if (event.target.tagName === 'IMG') {
    event.target.hidden = true;
    const fallback = event.target.parentElement.querySelector('.photo-unavailable');
    if (fallback) fallback.hidden = false;
  }
}, true);
window.addEventListener('hashchange', () => {
  if (location.hash === '#workspace') {
    workspace.focus();
    return;
  }
  render();
  window.scrollTo(0, 0);
});
render();
