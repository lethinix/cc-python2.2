import rhinoscriptsyntax as rs
import csv
import time
import scriptcontext as sc

# scaling
GEO_SCALE = 1          
TOWER_SCALE = 0.01    
ROTOR_SCALE = 0.01      
MAX_TURBINES = 50      
UPDATE_INTERVAL = 10   # keeping track of proccessing progress


def load_turbine_data():
    turbines = []
    with open("data/iowa_turbines_clean.csv") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= MAX_TURBINES: 
                break
            try:
                turbines.append({
                    "x": float(row["xlong"]), 
                    "y": float(row["ylat"]),  
                    "height": float(row["t_hh"]) * TOWER_SCALE,
                    "diameter": float(row["t_rd"]) * ROTOR_SCALE,
                    "capacity": float(row["t_cap"])
                })
            except:
                print("Skipped row {0}: Bad data".format(i+1))
    return turbines

def create_turbine_visualization(turbines):
    rs.EnableRedraw(False)
    start_time = time.time()
    
    for i, turbine in enumerate(turbines):
        try:
            # turbine tower
            tower = rs.AddLine(
                [turbine["x"], turbine["y"], 0],
                [turbine["x"], turbine["y"], turbine["height"]]
            )
            
            # rotor disk
            rotor = rs.AddCylinder(
                [turbine["x"], turbine["y"], turbine["height"]],  # Base point
                0.05 * turbine["diameter"],  # Height (thin disc)
                turbine["diameter"]/2        # Radius
            )
            
            # adding tilt
            rs.RotateObject(rotor, 
                          [turbine["x"], turbine["y"], turbine["height"]], 
                          5,  # 5 degree tilt
                          [1, 0, 0])  # X-axis rotation
            
            # color mapping
            norm_cap = min(turbine["capacity"] / 5000, 1.0)
            color = rs.CreateColor(
                int(255 * (1 - norm_cap)),  # red
                0,
                int(255 * norm_cap)         # blue
            )
            rs.ObjectColor([tower, rotor], color)
            
            if (i+1) % UPDATE_INTERVAL == 0:
                rs.EnableRedraw(True)
                print("Processed {0}/{1}".format(i+1, len(turbines)))
                rs.EnableRedraw(False)
                
        except Exception as e:
            print("Error on turbine {0}: {1}".format(i+1, str(e)))
    
    rs.EnableRedraw(True)
    rs.ZoomExtents()
    runtime = time.time() - start_time
    print("Created {0} turbines in {1:.1f}s".format(len(turbines), runtime))

# main script
if __name__ == "__main__":
    print("\nStarting turbine visualization...")
    
    # loading data
    turbines = load_turbine_data()
    
    # running geometry function
    create_turbine_visualization(turbines)
    
   
    rs.Command("_-Shaded")  # setting display mode
    print("\nDone!")
   