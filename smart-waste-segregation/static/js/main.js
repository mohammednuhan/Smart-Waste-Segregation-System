// ============================================================
// EcoSort — Main JavaScript
// ============================================================

document.addEventListener('DOMContentLoaded', function () {

    // ---- Mobile Nav Toggle ----
    const navToggle = document.getElementById('navToggle');
    const navLinks = document.getElementById('navLinks');

    if (navToggle && navLinks) {
        navToggle.addEventListener('click', function () {
            navLinks.classList.toggle('open');
        });
        // close on link click
        navLinks.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                navLinks.classList.remove('open');
            });
        });
    }

    // ---- Navbar shadow on scroll ----
    const navbar = document.querySelector('.eco-navbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            navbar.classList.toggle('scrolled', window.scrollY > 10);
        });
    }

    // ---- Classifier ----
    const form = document.getElementById('wasteForm');
    const input = document.getElementById('itemInput');
    const resultArea = document.getElementById('resultArea');
    const loading = document.getElementById('loading');
    const suggestionsBox = document.getElementById('suggestions');

    if (form && input && resultArea) {

        // ---- Live suggestions ----
        let debounceTimer = null;

        input.addEventListener('input', function () {
            const q = input.value.trim();
            clearTimeout(debounceTimer);
            if (q.length < 2) {
                suggestionsBox.classList.remove('show');
                return;
            }
            debounceTimer = setTimeout(function () {
                fetch('/api/search?q=' + encodeURIComponent(q))
                    .then(function (r) { return r.json(); })
                    .then(function (data) {
                        if (!data || data.length === 0) {
                            suggestionsBox.innerHTML = '<div class="sug-empty"><i class="fa-solid fa-ban"></i> No exact matches — press classify to try anyway</div>';
                            suggestionsBox.classList.add('show');
                            return;
                        }
                        suggestionsBox.innerHTML = data.slice(0, 6).map(function (item) {
                            const color = item.color || '#10b981';
                            return '<div class="sug-item" data-name="' + item.name + '">' +
                                '<span class="sug-icon" style="background:' + color + '20; color:' + color + ';"><i class="fa-solid fa-' + iconFor(item.category) + '"></i></span>' +
                                '<div><div class="sug-name">' + item.name.replace(/\b\w/g, function (c) { return c.toUpperCase(); }) + '</div>' +
                                '<div class="sug-cat">' + item.category_name + '</div></div></div>';
                        }).join('');
                        suggestionsBox.classList.add('show');

                        suggestionsBox.querySelectorAll('.sug-item').forEach(function (el) {
                            el.addEventListener('click', function () {
                                input.value = this.getAttribute('data-name');
                                suggestionsBox.classList.remove('show');
                                classify(input.value);
                            });
                        });
                    });
            }, 150);
        });

        document.addEventListener('click', function (e) {
            if (!input.contains(e.target) && !suggestionsBox.contains(e.target)) {
                suggestionsBox.classList.remove('show');
            }
        });

        // ---- Chip quick buttons ----
        document.querySelectorAll('.chip[data-item]').forEach(function (chip) {
            chip.addEventListener('click', function () {
                input.value = this.getAttribute('data-item');
                classify(input.value);
            });
        });

        // ---- Form submit ----
        form.addEventListener('submit', function (e) {
            e.preventDefault();
            classify(input.value);
        });

        function classify(itemName) {
            if (!itemName.trim()) return;

            suggestionsBox.classList.remove('show');
            resultArea.classList.remove('show');

            loading.classList.add('show');
            loading.style.display = 'block';

            fetch('/classify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                body: 'item_name=' + encodeURIComponent(itemName)
            })
                .then(function (r) { return r.json(); })
                .then(function (data) {
                    loading.classList.remove('show');
                    loading.style.display = 'none';
                    if (data.error) {
                        renderResult('error', '<i class="fa-solid fa-circle-exclamation"></i>', '#ef4444', 'Error', data.error);
                    } else if (data.not_found) {
                        renderNotFound(data);
                    } else {
                        renderSuccess(data);
                    }
                })
                .catch(function () {
                    loading.classList.remove('show');
                    loading.style.display = 'none';
                    renderResult('error', '<i class="fa-solid fa-triangle-exclamation"></i>', '#ef4444', 'Something went wrong', 'Please try again.');
                });
        }

        function iconFor(cat) {
            const map = {
                organic: 'seedling',
                recyclable: 'recycle',
                hazardous: 'radiation',
                domestic_hazardous: 'triangle-exclamation',
                construction: 'helmet-safety'
            };
            return map[cat] || 'circle-question';
        }

        function colorFor(cat) {
            const map = {
                organic: '#10b981',
                recyclable: '#3b82f6',
                hazardous: '#ef4444',
                domestic_hazardous: '#f59e0b',
                construction: '#8b5cf6'
            };
            return map[cat] || '#64748b';
        }

        function labelFor(cat) {
            const map = {
                organic: 'Organic / Wet Waste',
                recyclable: 'Recyclable / Dry Waste',
                hazardous: 'Hazardous Waste',
                domestic_hazardous: 'Domestic Hazardous',
                construction: 'Construction & Demolition'
            };
            return map[cat] || cat;
        }

        function renderResult(cls, icon, color, title, msg) {
            resultArea.className = 'result show ' + cls;
            resultArea.style.borderLeftColor = color;
            resultArea.innerHTML =
                '<div class="result-head">' +
                '<div class="result-head-icon" style="background:' + color + ';">' + icon + '</div>' +
                '<div><h3>' + title + '</h3><p>' + msg + '</p></div></div>';
        }

        function renderNotFound(data) {
            resultArea.className = 'result show not-found';
            resultArea.style.borderLeftColor = '#f59e0b';
            let tips = (data.tips || []).map(function (t) {
                return '<div class="result-item full"><small>Try this</small><p>' + t + '</p></div>';
            }).join('');
            resultArea.innerHTML =
                '<div class="result-head">' +
                '<div class="result-head-icon" style="background:#f59e0b;"><i class="fa-solid fa-circle-question"></i></div>' +
                '<div><h3>Item Not Found</h3><p>' + data.suggestion + '</p></div></div>' +
                '<div class="result-grid">' + tips + '</div>';
        }

        function renderSuccess(data) {
            const cat = data.category_key;
            const color = data.color || colorFor(cat)
            resultArea.className = 'result show ' + cat;
            resultArea.style.borderLeftColor = color;

            const dispose = (data.recycling_method || 'Follow local waste guidelines').split('>');
            const process = (data.recycling_process || data.recycling_method || '').split('>');

            resultArea.innerHTML =
                '<div class="result-head">' +
                '<div class="result-head-icon" style="background:' + color + ';"><i class="fa-solid fa-' + (data.icon || iconFor(cat)) + '"></i></div>' +
                '<div><h3>' + data.item_name + '</h3><p>' + labelFor(cat) + '</p></div></div>' +

                '<span class="bin-badge" style="background:' + color + ';"><i class="fa-solid fa-trash-can"></i> ' + (data.bin_color || 'General Waste') + '</span>' +

                '<div class="result-grid">' +
                '<div class="result-item full"><small>How to handle</small><p>' + dispose.join(' → ') + '</p></div>' +
                '<div class="result-item"><small>Decomposition time</small><p>' + (data.decomposition_time || '—') + '</p></div>' +
                '<div class="result-item"><small>Environmental impact</small><p>' + (data.environmental_impact || '—') + '</p></div>' +
                (process.length > 1 ? '<div class="result-item full"><small>Recycling process</small><p>' + process.join(' → ') + '</p></div>' : '') +
                '</div>';
        }
    }

    // ---- Animated counters ----
    const counters = document.querySelectorAll('.stat-num[data-count]');

    if (counters.length && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                const target = parseInt(el.getAttribute('data-count'), 10);
                const suffix = target >= 1000 ? 'T' : '+';
                const dur = 1200;
                const start = performance.now();
                function tick(now) {
                    const p = Math.min((now - start) / dur, 1);
                    const eased = 1 - Math.pow(1 - p, 3);
                    el.textContent = Math.round(eased * target).toLocaleString();
                    if (p < 1) requestAnimationFrame(tick);
                }
                requestAnimationFrame(tick);
                observer.unobserve(el);
            });
        }, { threshold: 0.4 });
        counters.forEach(function (el) { observer.observe(el); });
    } else {
        counters.forEach(function (el) {
            el.textContent = parseInt(el.getAttribute('data-count'), 10).toLocaleString();
        });
    }

    // ---- Animated progress bars ----
    const bars = document.querySelectorAll('.bar-fill[data-width]');

    if (bars.length && 'IntersectionObserver' in window) {
        const barObserver = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                const bar = entry.target;
                bar.style.width = bar.getAttribute('data-width');
                barObserver.unobserve(bar);
            });
        }, { threshold: 0.4 });
        bars.forEach(function (bar) { barObserver.observe(bar); });
    } else {
        bars.forEach(function (bar) {
            bar.style.width = bar.getAttribute('data-width');
        });
    }
});