# EcoSort - Smart Waste Segregation & Recycling System

## Conservation of Natural Resources - 2026

### About
An AI-powered system to help users classify waste properly and learn about recycling. Built for the Conservation of Natural Resources course assignment.

### Features
- Real-time waste classification (85+ items)
- 5 categories: Organic, Recyclable, Hazardous, Domestic Hazardous, Construction
- Recycling process guides (Paper, Plastic, Glass, Metal, E-waste, Composting)
- Environmental impact information
- Usage statistics tracking
- Educational content about waste management

### How to Run
1. Install Python 3.8+
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Open browser: http://localhost:5000

### Project Structure
```
smart-waste-segregation/
├── app.py              # Main Flask application
├── waste_data.py       # Waste database (85+ items)
├── requirements.txt    # Dependencies
├── README.md          # This file
├── data/              # SQLite database
├── static/
│   ├── css/style.css  # Styles
│   └── js/main.js     # Frontend logic
└── templates/
    ├── index.html      # Home page
    ├── education.html  # Learn about waste management
    ├── recycling.html  # How recycling works
    ├── stats.html      # Usage statistics
    └── about.html      # About the project
```

### Technologies
- **Backend:** Python, Flask
- **Database:** SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Font Awesome

### References
- CPCB (Central Pollution Control Board) Guidelines
- MoEF&CC (Ministry of Environment, Forest and Climate Change)
- UNEP (United Nations Environment Programme)
