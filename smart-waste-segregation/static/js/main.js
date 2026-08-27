// EcoSort - Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('wasteForm');
    var input = document.getElementById('itemInput');
    var result = document.getElementById('resultArea');

    // Form submit
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        classify(input.value);
    });

    // Quick buttons
    document.querySelectorAll('.qbtn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            var item = this.getAttribute('data-item');
            input.value = item;
            classify(item);
        });
    });

    function classify(itemName) {
        if (!itemName.trim()) return;

        result.innerHTML = '<div class="loading"><div class="spinner"></div><p>Searching...</p></div>';
        result.style.display = 'block';

        fetch('/classify', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: 'item_name=' + encodeURIComponent(itemName)
        })
        .then(function(r) { return r.json(); })
        .then(function(data) {
            if (data.error) {
                result.innerHTML = '<div class="result-card hazardous"><p>' + data.error + '</p></div>';
            } else if (data.not_found) {
                result.innerHTML = '<div class="result-card hazardous">' +
                    '<div class="result-top"><i class="fa-solid fa-circle-question" style="color:#f59e0b;"></i>' +
                    '<div><h3>Not Found</h3><p>Try simpler terms like "plastic" or "battery"</p></div></div></div>';
            } else {
                showResult(data);
            }
        })
        .catch(function() {
            result.innerHTML = '<div class="result-card hazardous"><p>Something went wrong. Try again.</p></div>';
        });
    }

    function showResult(data) {
        var cat = data.category_key;
        var icon = cat === 'organic' ? 'fa-seedling' : cat === 'recyclable' ? 'fa-recycle' : cat === 'hazardous' ? 'fa-radiation' : 'fa-triangle-exclamation';
        var color = cat === 'organic' ? '#22c55e' : cat === 'recyclable' ? '#2563eb' : cat === 'hazardous' ? '#ef4444' : '#f59e0b';

        var html = '<div class="result-card ' + cat + '">';
        html += '<div class="result-top">';
        html += '<i class="fa-solid ' + icon + '" style="color:' + color + '; font-size:1.8rem;"></i>';
        html += '<div><h3>' + data.item_name + '</h3><p>' + data.description + '</p></div>';
        html += '</div>';
        html += '<div style="margin-bottom:10px;"><span style="background:' + color + '; color:#fff; padding:4px 12px; border-radius:20px; font-size:0.8rem;">' + data.bin_color + '</span></div>';
        html += '<div class="result-grid">';
        html += '<div class="result-box"><small>How to Dispose</small><p>' + data.recycling_method + '</p></div>';
        html += '<div class="result-box"><small>Decomposition Time</small><p>' + data.decomposition_time + '</p></div>';
        html += '<div class="result-box"><small>Environmental Impact</small><p>' + data.environmental_impact + '</p></div>';
        if (data.recycling_process) {
            html += '<div class="result-box"><small>Recycling Process</small><p>' + data.recycling_process + '</p></div>';
        }
        html += '</div></div>';

        result.innerHTML = html;
    }
});
