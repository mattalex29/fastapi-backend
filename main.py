from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/stats/by-size")
def get_stats(area: str = "Mont Kiara"):
    return {
        "size_bracket_stats": [
            {"size_range": "500-800", "average_rent_rm": 1500, "average_sale_rm": 500000, "average_roi_percent": 3.6},
            {"size_range": "801-1200", "average_rent_rm": 2500, "average_sale_rm": 800000, "average_roi_percent": 3.75},
            {"size_range": "1201-1600", "average_rent_rm": 3500, "average_sale_rm": 1200000, "average_roi_percent": 3.5},
        ]
    }
