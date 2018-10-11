from flask import Flask, jsonify

# Dicionary 
station_query = [('USC00519281', 2772),
 {('USC00519397', 2724),
 ('USC00513117', 2709),
 ('USC00519523', 2669),
 ('USC00516128', 2612),
 ('USC00514830', 2202),
 ('USC00511918', 1979),
 ('USC00517948', 1372),
 ('USC00518838', 511)}]

 # Flask setup
app = Flask(__name__)

#Flask route
@app.route("/api/v1.0/stations")
def stations():
    return(f"Station Query")