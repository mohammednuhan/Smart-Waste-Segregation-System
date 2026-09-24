# app.py - EcoSort: Smart Waste Segregation System
# Conservation of Natural Resources - 2026

from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime
from waste_data import WASTE_DATABASE, search_items

app = Flask(__name__)
app.secret_key = 'ecosort-waste-project-2026'


# ============================================================
# DATABASE
# ============================================================

def init_db():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect('data/waste_tracker.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS waste_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT,
        category TEXT,
        sub_category TEXT,
        recommendation TEXT,
        date_added TEXT
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS user_stats (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total_items INTEGER DEFAULT 0,
        organic_count INTEGER DEFAULT 0,
        recyclable_count INTEGER DEFAULT 0,
        hazardous_count INTEGER DEFAULT 0,
        other_count INTEGER DEFAULT 0
    )''')
    c.execute("SELECT count(*) FROM user_stats")
    if c.fetchone()[0] == 0:
        c.execute("INSERT INTO user_stats DEFAULT VALUES")
    conn.commit()
    conn.close()


# ============================================================
# CLASSIFICATION LOGIC
# ============================================================

def classify_waste(item_name):
    results = search_items(item_name)
    if results:
        item = results[0]
        return {
            "category": item["category_name"],
            "category_key": item["category"],
            "color": item["color"],
            "bin_color": item.get("bin_color", "General Waste"),
            "item_name": item["name"].title(),
            "icon": item.get("icon", "circle-question"),
            "description": item["data"]["description"],
            "recycling_method": item["data"]["recycling_method"],
            "decomposition_time": item["data"]["decomposition_time"],
            "environmental_impact": item["data"]["environmental_impact"],
            "recycling_process": item["data"].get("recycling_process", "Follow local waste guidelines")
        }
    return None


# ============================================================
# ROUTES
# ============================================================

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/recycling')
def recycling():
    return render_template('recycling.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/stats')
def stats():
    try:
        conn = sqlite3.connect('data/waste_tracker.db')
        c = conn.cursor()
        
        c.execute("SELECT category, COUNT(*) FROM waste_logs GROUP BY category")
        category_counts = dict(c.fetchall())
        
        c.execute("SELECT COUNT(*) FROM waste_logs")
        total = c.fetchone()[0]
        
        c.execute("SELECT item_name, category, date_added FROM waste_logs ORDER BY id DESC LIMIT 10")
        recent_items = c.fetchall()
        
        c.execute("SELECT item_name, COUNT(*) as cnt FROM waste_logs GROUP BY item_name ORDER BY cnt DESC LIMIT 5")
        common_items = c.fetchall()
        
        conn.close()
        
        return render_template('stats.html', 
                             total=total,
                             category_counts=category_counts,
                             recent_items=recent_items,
                             common_items=common_items)
    except Exception as e:
        return render_template('stats.html', total=0, category_counts={}, recent_items=[], common_items=[])

@app.route('/classify', methods=['POST'])
def classify():
    item_name = request.form.get('item_name', '')
    
    if not item_name.strip():
        return jsonify({"error": "Please enter an item name"}), 400
    
    result = classify_waste(item_name)
    
    if result:
        try:
            conn = sqlite3.connect('data/waste_tracker.db')
            c = conn.cursor()
            c.execute("INSERT INTO waste_logs (item_name, category, sub_category, recommendation, date_added) VALUES (?, ?, ?, ?, ?)",
                     (item_name, result["category_key"], result["item_name"], result["recycling_method"], datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            conn.commit()
            conn.close()
        except Exception as e:
            print("Database error:", e)
        
        return jsonify(result)
    else:
        return jsonify({
            "not_found": True,
            "suggestion": "This item was not found in our database.",
            "tips": [
                "Try searching with simpler terms (e.g., 'plastic' instead of 'plastic water bottle cap')",
                "Check if the item belongs to any of our categories: Organic, Recyclable, or Hazardous",
                "When in doubt, contact your local waste management authority"
            ]
        }), 200

@app.route('/api/search')
def api_search():
    query = request.args.get('q', '')
    results = search_items(query)
    return jsonify(results)


# ============================================================
# MAIN
# ============================================================

if __name__ == '__main__':
    init_db()
    print("=" * 50)
    print("  EcoSort - Smart Waste Segregation System")
    print("  Conservation of Natural Resources - 2026")
    print("=" * 50)
    print("  Server: http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
