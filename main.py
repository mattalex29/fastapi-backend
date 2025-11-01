from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 1️⃣ Predefined districts (for dropdown)
districts = [
    "Kuala Lumpur",
    "Petaling Jaya",
    "Subang Jaya",
    "Shah Alam",
    "Puchong",
    "Cheras",
    "Klang",
    "Ampang",
    "Kajang",
    "Cyberjaya",
    "Putrajaya",
    "Sungai Buloh",
]

@app.get("/districts")
def get_districts():
    """Return top-level districts for dropdown"""
    return {"districts": districts}


# 2️⃣ Expanded property size brackets (up to 5000 sqft)
@app.get("/stats/by-location")
def get_stats(district: str, township: str = None, development: str = None):
    """Return dummy data for given location with larger size ranges"""
    # In the future, replace these with real averages from scraped data
    return {
        "district": district,
        "township": township,
        "development": development,
        "size_bracket_stats": [
            {"size_range": "500-800", "average_rent_rm": 1500, "average_sale_rm": 450000, "average_roi_percent": 4.0},
            {"size_range": "801-1200", "average_rent_rm": 2500, "average_sale_rm": 750000, "average_roi_percent": 4.0},
            {"size_range": "1201-1600", "average_rent_rm": 3500, "average_sale_rm": 1100000, "average_roi_percent": 3.8},
            {"size_range": "1601-2000", "average_rent_rm": 4200, "average_sale_rm": 1400000, "average_roi_percent": 3.6},
            {"size_range": "2001-2500", "average_rent_rm": 4800, "average_sale_rm": 1650000, "average_roi_percent": 3.5},
            {"size_range": "2501-3000", "average_rent_rm": 5500, "average_sale_rm": 1900000, "average_roi_percent": 3.47},
            {"size_range": "3001-4000", "average_rent_rm": 6500, "average_sale_rm": 2300000, "average_roi_percent": 3.4},
            {"size_range": "4001-5000", "average_rent_rm": 8000, "average_sale_rm": 3000000, "average_roi_percent": 3.2},
        ],
    }
