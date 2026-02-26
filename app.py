import streamlit as st
import streamlit.components.v1 as components
import json

st.set_page_config(page_title="GPS Tracker")

st.title("📍 Device GPS Location")

location = components.html(
    """
    <script>
    navigator.geolocation.getCurrentPosition(
        function(position) {
            const coords = {
                latitude: position.coords.latitude,
                longitude: position.coords.longitude,
                accuracy: position.coords.accuracy
            };
            window.parent.postMessage(
                {type: "streamlit:setComponentValue", value: JSON.stringify(coords)},
                "*"
            );
        },
        function(error) {
            window.parent.postMessage(
                {type: "streamlit:setComponentValue", value: null},
                "*"
            );
        }
    );
    </script>
    """,
    height=0,
)

if location is not None:
    try:
        data = json.loads(location)

        st.success("✅ Location Retrieved Successfully!")
        st.write("Latitude:", data["latitude"])
        st.write("Longitude:", data["longitude"])
        st.write("Accuracy:", data["accuracy"], "meters")

        st.map({"lat": [data["latitude"]], "lon": [data["longitude"]]})

    except Exception as e:
        st.error("Location received but parsing failed.")
        st.write("Raw value:", location)

else:
    st.warning("Waiting for location permission...")