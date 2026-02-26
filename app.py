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
                {isStreamlitMessage: true, type: "streamlit:setComponentValue", value: coords},
                "*"
            );
        },
        function(error) {
            window.parent.postMessage(
                {isStreamlitMessage: true, type: "streamlit:setComponentValue", value: null},
                "*"
            );
        }
    );
    </script>
    """,
    height=0,
)

if location:
    st.success("✅ Location Retrieved Successfully!")
    st.write("Latitude:", location["latitude"])
    st.write("Longitude:", location["longitude"])
    st.write("Accuracy:", location["accuracy"], "meters")

    st.map({"lat": [location["latitude"]], "lon": [location["longitude"]]})
else:
    st.warning("Waiting for location permission...")