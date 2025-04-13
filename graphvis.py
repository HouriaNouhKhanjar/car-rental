from graphviz import Digraph

# Create a detailed ERD with attributes and data types
erd_detailed = Digraph('ERD_Detailed', filename='car_rental_erd_detailed', format='png')

# Entities with attributes
entities_detailed = {
    "Car": [
        "CarID (PK, INT)", "Model (VARCHAR)", "Brand (VARCHAR)", 
        "Year (INT)", "PricePerDay (DECIMAL)", "CategoryID (FK, INT)",
        "Publish (INT)", "Description (TEXT)"
    ],
    "Customer": [
        "CustomerID (PK, INT)", "Name (VARCHAR)", "Email (VARCHAR)", 
        "Phone (VARCHAR)", "Password (VARCHAR)"
    ],
    "Review": [
        "ReviewID (PK, INT)", "CustomerID (FK, INT)", "CarID (FK, INT)", 
        "Rating (INT)", "Comment (TEXT)", "ReviewDate (DATETIME)"
    ],
    "Like": [
        "LikeID (PK, INT)", "CustomerID (FK, INT)", "CarID (FK, INT)"
    ],
    "Car_Category": [
        "CategoryID (PK, INT)", "CategoryName (VARCHAR)"
    ],
    "Car_Images": [
        "ImageID (PK, INT)", "CarID (FK, INT)", "ImageURL (TEXT)"
    ],
    "Booking": [
        "BookingID (PK, INT)", "CustomerID (FK, INT)", "CarID (FK, INT)", 
        "StartDate (DATETIME)", "EndDate (DATETIME)", "TotalPrice (DECIMAL)", "Status (INT)"
    ],
    "Customer_Support": [
        "SupportID (PK, INT)", "CustomerID (FK, INT)", "Message (TEXT)", "Status (INT)", "Date (DATETIME)"
    ]
}

# Add entities and attributes to the ERD
for entity, attributes in entities_detailed.items():
    label = f"{entity} | " + " \\n ".join(attributes)
    erd_detailed.node(entity, label=label, shape='record')

# Relationships
relations_detailed = [
    ("Car_Category", "Car"),
    ("Car", "Car_Images"),
    ("Customer", "Review"),
    ("Car", "Review"),
    ("Customer", "Like"),
    ("Car", "Like"),
    ("Customer", "Booking"),
    ("Car", "Booking"),
    ("Customer", "Customer_Support")
]

for src, dst in relations_detailed:
    erd_detailed.edge(src, dst)

# Save ERD as PNG image
erd_detailed.render('car_rental_erd_detailed', format='png', cleanup=False)

