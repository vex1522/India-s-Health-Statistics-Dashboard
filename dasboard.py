import folium
import pandas as pd
import requests

india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5, tiles="OpenStreetMap")

geojson_url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

try:
    print("Fetching verified India GeoJSON mirror...")
    response = requests.get(geojson_url, timeout=15)
    state_geojson = response.json()
    print("Success: GeoJSON loaded perfectly.")
except Exception as e:
    raise RuntimeError(f"Could not parse the GeoJSON data: {e}")

folium.Choropleth(
    geo_data=state_geojson,
    name="Choropleth (Obesity in Women)",
    data=cleaned_df,
    columns=["State", "Obesity_Women"],
    key_on="feature.properties.ST_NM",  # Matches the state identity key in this specific file
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.3,
    legend_name="Prevalence of Overweight or Obese Women (%)",
    highlight=True
).add_to(india_map)

state_metadata = {
    "Andhra Pradesh": {"capital": "Amaravati", "coords": [16.5448, 80.5181]},
    "Arunachal Pradesh": {"capital": "Itanagar", "coords": [27.102, 93.6166]},
    "Assam": {"capital": "Dispur", "coords": [26.1433, 91.7898]},
    "Bihar": {"capital": "Patna", "coords": [25.5941, 85.1376]},
    "Chhattisgarh": {"capital": "Raipur", "coords": [21.2514, 81.6296]},
    "Goa": {"capital": "Panaji", "coords": [15.4909, 73.8278]},
    "Gujarat": {"capital": "Gandhinagar", "coords": [23.2156, 72.6369]},
    "Haryana": {"capital": "Chandigarh", "coords": [30.7333, 76.7794]},
    "Himachal Pradesh": {"capital": "Shimla", "coords": [31.1048, 77.1734]},
    "Jharkhand": {"capital": "Ranchi", "coords": [23.3441, 85.3094]},
    "Karnataka": {"capital": "Bengaluru", "coords": [12.9716, 77.5946]},
    "Kerala": {"capital": "Thiruvananthapuram", "coords": [8.5241, 76.9366]},
    "Madhya Pradesh": {"capital": "Bhopal", "coords": [23.2599, 77.4126]},
    "Maharashtra": {"capital": "Mumbai", "coords": [19.0760, 72.8777]},
    "Manipur": {"capital": "Imphal", "coords": [24.8170, 93.9368]},
    "Meghalaya": {"capital": "Shillong", "coords": [25.5788, 91.8831]},
    "Mizoram": {"capital": "Aizawl", "coords": [23.7307, 92.7173]},
    "Nagaland": {"capital": "Kohima", "coords": [25.6751, 94.1086]},
    "Odisha": {"capital": "Bhubaneswar", "coords": [20.2961, 85.8245]},
    "Punjab": {"capital": "Chandigarh", "coords": [30.7333, 76.7794]},
    "Rajasthan": {"capital": "Jaipur", "coords": [26.9124, 75.7873]},
    "Sikkim": {"capital": "Gangtok", "coords": [27.3314, 88.6138]},
    "Tamil Nadu": {"capital": "Chennai", "coords": [13.0827, 80.2707]},
    "Telangana": {"capital": "Hyderabad", "coords": [17.3850, 78.4867]},
    "Tripura": {"capital": "Agartala", "coords": [23.8315, 91.2868]},
    "Uttar Pradesh": {"capital": "Lucknow", "coords": [26.8467, 80.9462]},
    "Uttarakhand": {"capital": "Dehradun", "coords": [30.3165, 78.0322]},
    "West Bengal": {"capital": "Kolkata", "coords": [22.5726, 88.3639]},
    "Delhi": {"capital": "New Delhi", "coords": [28.6139, 77.2090]},
    "Jammu & Kashmir": {"capital": "Srinagar", "coords": [34.0837, 74.7973]}
}

for _, row in cleaned_df.iterrows():
    state_name = row['State']
    
    if state_name in state_metadata:
        coords = state_metadata[state_name]['coords']
        capital = state_metadata[state_name]['capital']
        
        popup_html = f"""
        <div style="font-family: Arial, sans-serif; width: 220px; font-size: 12px; color: #333;">
            <h4 style="margin: 0 0 8px 0; color: #d9534f; border-bottom: 1px solid #ddd; padding-bottom: 4px;">
                {state_name}
            </h4>
            <table style="width: 100%; border-collapse: collapse;">
                <tr><td><b>Capital:</b></td><td style="text-align: right;">{capital}</td></tr>
                <tr><td><b>Blood Sugar (W):</b></td><td style="text-align: right;">{row['High_Blood_Sugar_Women']:.1f}%</td></tr>
                <tr><td><b>Blood Sugar (M):</b></td><td style="text-align: right;">{row['High_Blood_Sugar_Men']:.1f}%</td></tr>
                <tr><td><b>Anaemia (Kids):</b></td><td style="text-align: right;">{row['Anaemia_Children']:.1f}%</td></tr>
                <tr><td><b>Anaemia (W):</b></td><td style="text-align: right;">{row['Anaemia_Women']:.1f}%</td></tr>
            </table>
        </div>
        """
        
        iframe = folium.IFrame(popup_html, width=240, height=140)
        popup_window = folium.Popup(iframe, max_width=260)
        
        folium.CircleMarker(
            location=coords,
            radius=6,
            popup=popup_window,
            color='#3186cc',
            fill=True,
            fill_color='#3186cc',
            fill_opacity=0.8,
            tooltip=f"Click for {state_name} summary"
        ).add_to(india_map)

folium.LayerControl().add_to(india_map)
india_map.save("india_public_health_dashboard.html")

print("Dashboard built successfully! Open 'india_public_health_dashboard.html' to view your interactive map.")