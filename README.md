[index.html](https://github.com/user-attachments/files/23654032/index.html)
<!DOCTYPE html>
<html lang="en">
<head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>HandMaster — Hand tracking mouse control</title>
        <link rel="stylesheet" href="style.css">
        <link rel="icon" href="icon.svg" type="image/svg+xml">
        <link rel="apple-touch-icon" href="icon.svg">
        <meta name="theme-color" content="#0a9d58">
</head>
        <style>
                :root{
	--bg: #ffffff;
	--green: #0a9d58;
	--green-dark: #067a41;
	--muted: #6b7280;
	--card: #f7fff9;
	--max-width: 1100px;
    /* default header offset for anchor scrolling (adjust if header size changes) */
    --header-offset: 88px;
}

*{box-sizing:border-box}
html,body{height:100%}
body{
	margin:0;
	font-family: Inter, ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
	background:var(--bg);
	color:#0f172a;
	-webkit-font-smoothing:antialiased;
	-moz-osx-font-smoothing:grayscale;
}

.container{max-width:var(--max-width);margin:0 auto;padding:1rem}

.site-header{border-bottom:1px solid #eef2f1;background:#fff}
.site-header .container{display:flex;align-items:center;justify-content:space-between;padding:1rem 1rem}
.logo{display:inline-flex;align-items:center;gap:.5rem;text-decoration:none}
.logo-text{font-weight:700;color:var(--green);font-size:1.2rem}
.logo-img{width:36px;height:36px;display:inline-block;flex:0 0 36px;border-radius:6px}

/* Dependencies table styles */
.table-wrap{overflow:auto;margin-top:.5rem}
.deps-table{width:100%;border-collapse:collapse;font-size:.95rem}
.deps-table thead th{background:#f7fff9;padding:.6rem;border:1px solid #e6f3ea;text-align:left;color:var(--green)}
.deps-table td{padding:.6rem;border:1px solid #eef3f0;background:#fff}
.deps-table code{background:#f1fff6;padding:.12rem .35rem;border-radius:4px;font-family:SFMono-Regular,Consolas,monospace;color:#064c2c}
.deps-table strong{color:var(--green)}
.table-wrap::-webkit-scrollbar{height:8px}
.table-wrap::-webkit-scrollbar-thumb{background:#d1f0db;border-radius:4px}

/* Local file tree */
.file-tree{font-family:inherit;background:transparent;padding:.5rem 0}
.file-tree .dir-item{margin:6px 0}
.file-tree .dir-title{font-weight:700;color:var(--green);padding:.2rem 0}
.file-tree .dir-children{padding-left:1rem;border-left:2px solid #f1f7f3}
.file-tree .file-item{padding:.15rem 0}
.file-tree a{color:var(--green);text-decoration:none}
.file-tree a:hover{text-decoration:underline}
.nav a{margin-left:1rem;color:var(--muted);text-decoration:none}
.nav a:hover{color:var(--green-dark)}

.hero{padding:3rem 0}
.hero-inner{display:flex;gap:2rem;align-items:stretch}
.hero-text{flex:1}
.hero h1{font-size:2rem;margin:0 0 .5rem;color:#0b5619}
.lead{color:var(--muted);margin:0 0 1rem}
.cta-row .btn{margin-right:.5rem}

.hero-card{width:280px;background:linear-gradient(180deg,var(--card),#fff);padding:1rem;border-radius:10px;border:1px solid #009135}
.hero-card h3{margin-top:0}

.btn{display:inline-block;padding:.6rem 1rem;border-radius:8px;border:1px solid transparent;background:#fff;color:var(--green);text-decoration:none;font-weight:600;box-shadow:0 1px 0 rgba(2,6,23,0.03)}
.btn:hover{transform:translateY(-1px)}
.btn-primary{background:var(--green);color:#fff}

/* active state (applies to selected platform button) */
.btn.active, .btn.active:hover{background:var(--green);color:#fff}


.sections{padding:2rem 0;border-top:1px solid #f1f5f4}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1rem}
.card{background:#fff;border-radius:8px;padding:1rem;border:1px solid #eef3f0}

.download-row{display:flex;gap:1rem;flex-wrap:wrap}
.download-card{flex:1;min-width:200px;border:1px dashed #378e57;padding:1rem;border-radius:8px;background:#fff}

.usage-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.code{background:#0f172a;color:#3c7f54;padding:1rem;border-radius:6px;overflow:auto}

.releases{list-style:none;padding-left:0;margin:0}
.releases li{margin:0.6rem 0}
.release-note{color:var(--muted);font-size:.95rem;margin-top:.25rem}

/* Download panel overlay */
.panel-overlay{display:none;position:fixed;inset:0;background:rgba(2,6,23,0.5);align-items:center;justify-content:center;padding:2rem;z-index:60}
.panel{background:var(--bg);max-width:680px;width:100%;border-radius:10px;padding:1.2rem 1.4rem;box-shadow:0 10px 30px rgba(2,6,23,0.12);border:1px solid #479764}
.panel h2{margin-top:0}
.panel .releases{margin-top:0.6rem}
.panel .releases a{color:var(--green);font-weight:600;text-decoration:none}
.panel .releases a:hover{color:var(--green-dark)}
.close-btn{position:absolute;right:1.2rem;top:1rem;border:0;background:var(--card);font-size:1.4rem;cursor:pointer;color:var(--green-dark);padding:.15rem .5rem;border-radius:6px;box-shadow:0 2px 6px rgba(2,6,23,0.06)}

@media (max-width:520px){
	.panel{padding:1rem;margin:1rem;border-radius:8px}
	.close-btn{right:.8rem;top:.6rem}
}

.site-footer{border-top:1px solid #abf2d2;background:#abf2d2;padding:1rem 0;margin-top:2rem}
.site-footer p{margin:0;color:var(--muted)}

@media (max-width:800px){
	.hero-inner{flex-direction:column}
	.usage-grid{grid-template-columns:1fr}
	.nav{display:none}
}

/* Make the header stick to the top while scrolling */
.site-header{
	position:sticky;
	top:0;
	z-index:30;
}

/* Ensure in-page anchor jumps account for the sticky header */
html{scroll-padding-top:var(--header-offset)}
/* apply margin so native anchor jumps land below the sticky header */
section[id], .sections{scroll-margin-top:calc(var(--header-offset) - 8px)}

/* When a fragment target is activated, insert an offset so the element is visible */
:target::before{
	content: "";
	display:block;
	height:var(--header-offset);
	margin-top:calc(-1 * var(--header-offset));
}

@media (max-width:800px){
	:root{--header-offset:64px}
}[style.css](https://github.com/user-attachments/files/23654043/style.css)

        </style>
<body>
    <header class="site-header">
        <div class="container">
            <a class="logo" href="#">
                <img src="icon.svg" alt="HandMaster logo" class="logo-img" width="36" height="36">
                <span class="logo-text">HandMaster</span>
            </a>
            <nav class="nav">
                <a href="#features">Features</a>
                <a href="#download">Download</a>
                <a href="#usage">Usage</a>
                <a href="#about">About</a>
            </nav>
        </div>
    </header>

    <main>
        <section class="hero">
            <div class="container hero-inner">
                <div class="hero-text">
                    <h1>Control your mouse with your hands — simply and precisely</h1>
                    <p class="lead">HandMaster is a lightweight hand-tracking tool to steer your mouse using a webcam. Easy to , privacy-friendly, and designed for productivity.</p>
                    <p class="cta-row">
                        <button id="btn-windows" data-platform="windows" class="btn btn-primary" type="button" onclick="openDownloads('windows')" aria-label="Download for Windows">Download for Windows</button>
                        <button id="btn-linux" data-platform="linux" class="btn" type="button" onclick="openDownloads('linux')" aria-label="Download for Linux">Download for Linux</button>
                    </p>
                </div>
                <div class="hero-card">
                    <h3>Why HandMaster?</h3>
                    <ul>
                        <li>Low-latency local tracking</li>
                        <li>Simple calibration — get started in minutes</li>
                        <li>Works with most webcams</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="features" class="container sections">
            <h2>Features</h2>
            <div class="grid">
                <article class="card">
                    <h3>Accurate Tracking</h3>
                    <p>Robust hand landmark detection translates gestures into precise cursor movement.</p>
                </article>
                <article class="card">
                    <h3>Customizable Gestures</h3>
                    <p>Map gestures to clicks, drag, scroll, and shortcuts.</p>
                </article>
                <article class="card">
                    <h3>Privacy First</h3>
                    <p>All processing happens locally — no cloud uploads.</p>
                </article>
            </div>
        </section>

        <section id="download" class="container sections">
            <h2>Download</h2>
            <p>Click the <strong>Download for Windows</strong> or <strong>Download for Linux</strong> buttons above to view releases and download links.</p>
        </section>

        <!-- Hidden download panel that appears when a platform button is clicked -->
        <div id="download-panel" class="panel-overlay" aria-hidden="true">
                <div class="panel" role="dialog" aria-modal="true" aria-labelledby="panel-title">
                <button class="close-btn" type="button" aria-label="Close" title="Close (Esc)" onclick="closeDownloads()">✕</button>
                <h2 id="panel-title">Downloads</h2>
                <div id="panel-content">
                    <!-- Populated by JS -->
                </div>
            </div>
        </div>

        <section id="usage" class="container sections">
            <h2>Install & Use</h2>
            <div class="usage-grid">
                <div>
                    <h3>Quick start</h3>
                    <ol>
                        <li>Download the appropriate package.</li>
                        <li>unzip the package.</li>
                        <li>Launch the ".run" file.</li>
                    </ol>
                </div>
                <div>
                    <h3>Developer / CLI</h3>
                    <p>If you ship a CLI or Python package, example commands go here:</p>
                    <pre class="code"># Start local UI
handmaster --gui

# Or run a headless service
handmaster --service</pre>
                </div>
            </div>
        </section>

        <section id="dependencies" class="container sections">
            <h2>Dependencies</h2>
            <p>Required Python libraries if something went wrong</p>
            <div class="table-wrap">
                <table class="deps-table" aria-label="Required Python libraries and install commands">
                    <thead>
                        <tr>
                            <th>Library</th>
                            <th>Verified import</th>
                            <th>Install command</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td><strong>OpenCV</strong></td>
                            <td><code>import cv2</code></td>
                            <td><code>pip install opencv-python</code></td>
                        </tr>
                        <tr>
                            <td><strong>MediaPipe</strong></td>
                            <td><code>import mediapipe as mp</code></td>
                            <td><code>pip install mediapipe</code></td>
                        </tr>
                        <tr>
                            <td><strong>NumPy</strong></td>
                            <td><code>import numpy as np</code></td>
                            <td><code>pip install numpy</code></td>
                        </tr>
                        <tr>
                            <td><strong>PyAutoGUI</strong></td>
                            <td><code>import pyautogui</code></td>
                            <td><code>pip install pyautogui</code></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <section id="local-files" class="container sections">
            <h2>Local release files</h2>
            <p>Browse the sample release tree created in the repository. Click files to open them.</p>
            <div id="local-tree" class="file-tree" aria-live="polite">
                <!-- Rendered by JS -->
            </div>
        </section>

        <section id="about" class="container sections">
            <h2>About HandMaster</h2>
            <p>HandMaster is a small utility that turns hand gestures into mouse movement. It is ideal for hands-free control, accessibility workflows, and creative interactions.</p>
            <p>If you'd like, I can add a changelog, license, or real download links for your releases.</p>
        </section>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>&copy; 2025 HandMaster — Built with care. <a href="#">Contact</a></p>
        </div>
    </footer>
    <script>
        // URLs and release metadata
        // You may optionally include `size` (bytes) and `date` (RFC 2822 / ISO) here
        // If not provided the page will attempt a HEAD request to read headers.
        // Releases per platform — each platform can have multiple releases (newest first)
        const RELEASES = {
            windows: {
                releases: [
                    {
                            version: '1.0.2',
                        note: 'Works with Python 3.10.x — 3.12.x',
                        files: [
                                {name: 'handmaster-1.0.2-win.zip', url: 'https://files.catbox.moe/mvizp5.zip', size: 74547, date: '2025-11-21T00:00:00Z'}
                        ]
                    },
                            {
                            version: '1.0.1',
                            note: 'Works with Python 3.10.x — 3.12.x',
                            files: [
                                {name: 'handmaster-1.0.1-win.zip', url: 'https://files.catbox.moe/6ifz8n.zip', size: 81101, date: '2025-11-20T00:00:00Z'}
                            ]
                            },
                    {
                        version: '1.0.0',
                        note: 'Works with Python 3.10.x — 3.12.x',
                        files: [
                            {name: 'handmaster-1.0.0-win.zip', url: 'https://files.catbox.moe/6w7xxl.zip', size: 74445, date: '2025-11-18T00:00:00Z'}
                        ]
                    }
                ]
            },
            linux: {
                releases: [
                    {
                        version: '1.0.2',
                        note: '',
                        files: [
                            {name: 'handmaster-1.0.2-linux.zip', url: 'https://files.catbox.moe/yqn3ln.zip', size: 74342, date: '2025-11-21T00:00:00Z'}
                        ]
                    },
                    {
                        version: '1.0.1',
                        note: '',
                        files: [
                            {name: 'handmaster-1.0.1-linux.zip', url: 'https://files.catbox.moe/er1wvb.zip', size: 75059, date: '2025-11-20T00:00:00Z'}
                        ]
                    },
                    {
                        version: '1.0.0',
                        note: '',
                        files: [
                            {name: 'handmaster-1.0.0-linux.zip', url: 'https://files.catbox.moe/utoxvi.zip', size: 86630, date: '2025-11-18T00:00:00Z'}
                        ]
                    }
                ]
            }
        };

        const panel = document.getElementById('download-panel');
        const panelContent = document.getElementById('panel-content');
        const btnWindows = document.getElementById('btn-windows');
        const btnLinux = document.getElementById('btn-linux');

        function setActiveButton(platform){
            // remove active from both
            btnWindows.classList.remove('btn-primary','active');
            btnLinux.classList.remove('btn-primary','active');
            // add to selected
            if(platform === 'windows') btnWindows.classList.add('btn-primary','active');
            if(platform === 'linux') btnLinux.classList.add('btn-primary','active');
        }

        function openDownloads(platform){
            const info = RELEASES[platform];
            if(!info) return;
            panelContent.innerHTML = '';

            // Render each release for the platform (newest first)
            info.releases.forEach(rel => {
                const hdr = document.createElement('p');
                hdr.innerHTML = `<strong>${platform.toUpperCase()} — ${rel.version}</strong>`;
                panelContent.appendChild(hdr);

                if(rel.note){
                    const note = document.createElement('div');
                    note.className = 'release-note';
                    note.textContent = rel.note;
                    panelContent.appendChild(note);
                }

                const ul = document.createElement('ul');
                ul.className = 'releases';
                rel.files.forEach(f => {
                    const li = document.createElement('li');
                    const a = document.createElement('a');
                    a.href = f.url;
                    a.target = '_blank';
                    a.rel = 'noopener';
                    a.textContent = f.name;
                    li.appendChild(a);

                    const meta = document.createElement('small');
                    meta.className = 'file-meta';
                    meta.textContent = ' — fetching info…';
                    li.appendChild(meta);

                    // If metadata provided in RELEASES, use it immediately
                    if(f.size || f.date){
                        const sizeLabel = f.size ? formatBytes(f.size) : 'unknown size';
                        const dateLabel = f.date ? formatDate(f.date) : 'unknown date';
                        meta.textContent = ` — ${sizeLabel} • ${dateLabel}`;
                    } else {
                        // try a HEAD request to fetch Content-Length and Last-Modified
                        getFileInfo(f.url).then(res => {
                            const sizeLabel = res.size ? formatBytes(res.size) : 'unknown size';
                            const dateLabel = res.date ? formatDate(res.date) : 'unknown date';
                            meta.textContent = ` — ${sizeLabel} • ${dateLabel}`;
                        }).catch(()=>{
                            meta.textContent = ' — size unknown • date unknown';
                        });
                    }

                    ul.appendChild(li);
                });
                panelContent.appendChild(ul);
            });

            setActiveButton(platform);

            panel.style.display = 'flex';
            panel.setAttribute('aria-hidden','false');
            document.body.style.overflow = 'hidden';
        }
[Uploading style.css…]()

        function closeDownloads(){
            panel.style.display = 'none';
            panel.setAttribute('aria-hidden','true');
            document.body.style.overflow = '';
            // clear active state
            btnWindows.classList.remove('btn-primary','active');
            btnLinux.classList.remove('btn-primary','active');
        }

        // close on Escape
        document.addEventListener('keydown', (e)=>{ if(e.key === 'Escape') closeDownloads(); });

        // close when clicking outside the panel
        panel.addEventListener('click', (e)=>{ if(e.target === panel) closeDownloads(); });

        // Helper: try to read headers via HEAD request. May be blocked by CORS.
        async function getFileInfo(url){
            try{
                const res = await fetch(url, {method: 'HEAD'});
                if(!res.ok) throw new Error('HEAD failed');
                const len = res.headers.get('content-length');
                const lm = res.headers.get('last-modified') || res.headers.get('date');
                return { size: len ? parseInt(len,10) : null, date: lm ? new Date(lm) : null };
            }catch(err){
                // Rethrow so callers can fallback gracefully
                throw err;
            }
        }

        function formatBytes(bytes){
            if(!bytes || isNaN(bytes)) return null;
            const thresh = 1024;
            if(bytes < thresh) return bytes + ' B';
            const units = ['KB','MB','GB','TB'];
            let u = -1;
            do{ bytes = bytes / thresh; ++u } while(bytes >= thresh && u < units.length - 1);
            return bytes.toFixed(1) + ' ' + units[u];
        }

        function formatDate(d){
            if(!d) return null;
            const dt = (d instanceof Date) ? d : new Date(d);
            if(isNaN(dt)) return null;
            return dt.toLocaleString();
        }

        // Local file tree data for the sample release (now rooted at handmaster_1.0.0)
        const LOCAL_TREE = {
            name: 'handmaster_1.0.0',
            type: 'dir',
            children: [
                {
                    name: 'handmaster (Copy)', type: 'dir', children: [
                        { name: 'MANIFEST.in', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/MANIFEST.in' },
                        { name: 'README.md', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/README.md' },
                        { name: 'requirements.txt', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/requirements.txt' },
                        { name: 'run.py', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/run.py' },
                        { name: 'setup.py', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/setup.py' },
                        { name: 'handmaster', type: 'dir', children: [
                            { name: '__init__.py', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/__init__.py' },
                            { name: 'core.py', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/core.py' },
                            { name: 'assets', type: 'dir', children: [
                                { name: 'icon.png', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/assets/icon.png' },
                                { name: 'logo.svg', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/assets/logo.svg' },
                                { name: 'splash.png', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/assets/splash.png' }
                            ]},
                            { name: '__pycache__', type: 'dir', children: [
                                { name: 'README.txt', type: 'file', path: 'handmaster_1.0.0/handmaster (Copy)/handmaster/__pycache__/README.txt' }
                            ]}
                        ]}
                    ]}
            ]
        };

        function renderTree(node, parentEl){
            if(!node) return;
            if(node.type === 'file'){
                const li = document.createElement('div');
                li.className = 'file-item';
                const a = document.createElement('a');
                // encodeURI to handle spaces
                a.href = encodeURI(node.path);
                a.textContent = node.name;
                a.target = '_blank';
                a.rel = 'noopener';
                li.appendChild(a);
                parentEl.appendChild(li);
                return;
            }
            // directory
            const wrapper = document.createElement('div');
            wrapper.className = 'dir-item';
            const title = document.createElement('div');
            title.className = 'dir-title';
            title.textContent = node.name;
            wrapper.appendChild(title);
            const childrenWrap = document.createElement('div');
            childrenWrap.className = 'dir-children';
            if(node.children && node.children.length){
                node.children.forEach(child => renderTree(child, childrenWrap));
            }
            wrapper.appendChild(childrenWrap);
            parentEl.appendChild(wrapper);
        }

        document.addEventListener('DOMContentLoaded', ()=>{
            const root = document.getElementById('local-tree');
            renderTree(LOCAL_TREE, root);
        });
    </script>
</body>
</html>
