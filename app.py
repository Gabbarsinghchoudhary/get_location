import streamlit as st
from streamlit_js_eval import get_geolocation

st.set_page_config(page_title="GPS Location Tracker", page_icon="📍")

st.title("📍 Device GPS Location Tracker")

st.write("Click the button below to get your current GPS location.")

# Button to trigger location request
if st.button("Get Current Location"):

    # Get location from browser
    location = get_geolocation()

    if location is None:
        st.error("❌ Unable to retrieve location. Please allow location access and refresh the page.")
    else:
        try:
            lat = location["coords"]["latitude"]
            lon = location["coords"]["longitude"]
            accuracy = location["coords"]["accuracy"]

            st.success("✅ Location Retrieved Successfully!")

            st.write("### 📌 Coordinates")
            st.write(f"**Latitude:** {lat}")
            st.write(f"**Longitude:** {lon}")
            st.write(f"**Accuracy:** {accuracy} meters")

            # Show on map
            st.write("### 🗺️ Location on Map")
            st.map({"lat": [lat], "lon": [lon]})

        except Exception as e:
            st.error(f"Error reading location data: {e}")

st.markdown("---")
st.info("⚠️ Make sure you allow location permission in your browser.")