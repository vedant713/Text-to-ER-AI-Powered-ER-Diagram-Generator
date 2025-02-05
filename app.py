import streamlit as st
from src.parser import ERParser
from src.diagram_generator import ERDiagramGenerator
from PIL import Image

# Set Streamlit page configuration
st.set_page_config(
    page_title="ER Diagram Generator",
    page_icon="🗂️",
    layout="wide",
)

# Add title and description
st.title("🛠️ Text-to-ER Diagram Generator")
st.subheader("Generate Entity-Relationship Diagrams from Natural Language Descriptions")
st.markdown(
    """
    **How it works:**
    1. Enter a natural language description of your entities and relationships.
    2. Click on **"Generate ER Diagram"**.
    3. View the generated diagram directly in the app and download it as a PNG, PPTX, or DOT file.
    """
)

# Sidebar for filename configuration
st.sidebar.header("Settings")
filename = st.sidebar.text_input("Output File Name (without extension):", value="output")
pptx_option = st.sidebar.checkbox("Generate PPTX File", value=True)
dot_option = st.sidebar.checkbox("Generate DOT File", value=True)

# Text area for user input
user_input = st.text_area(
    "Enter ER description:",
    "A hotel has many rooms. A customer makes bookings.",
    height=150,
    help="Describe your entities and relationships in plain language.",
)

# Button to generate the ER diagram
if st.button("Generate ER Diagram"):
    with st.spinner("Processing your request..."):
        parser = ERParser()
        parser.parse(user_input)

        generator = ERDiagramGenerator(parser.entities, parser.relationships)

        if generator.generate(f"{filename}.png"):
            # Display the generated image in the UI
            st.success("ER Diagram generated successfully!")
            image = Image.open(f"{filename}.png")
            st.image(image, caption="Generated ER Diagram", use_container_width=True)

            # Optionally generate and provide the PPTX file for download
            if pptx_option:
                try:
                    generator.export_to_pptx(f"{filename}.pptx")
                    with open(f"{filename}.pptx", "rb") as file:
                        st.download_button(
                            "Download as PPTX", file, f"{filename}.pptx", "application/vnd.openxmlformats-officedocument.presentationml.presentation"
                        )
                except Exception as e:
                    st.error(f"Failed to generate PPTX file: {e}")

            # Optionally generate and provide the DOT file for download
            if dot_option:
                try:
                    generator.export_to_dot(f"{filename}.dot")
                    with open(f"{filename}.dot", "rb") as file:
                        st.download_button(
                            "Download DOT File", file, f"{filename}.dot", "text/plain"
                        )
                except Exception as e:
                    st.error(f"Failed to generate DOT file: {e}")

            # Allow the user to download the PNG file
            with open(f"{filename}.png", "rb") as file:
                st.download_button(
                    "Download as PNG", file, f"{filename}.png", "image/png"
                )
        else:
            st.error("Failed to generate ER diagram. Please check your input.")
else:
    st.info("Enter your description and click 'Generate ER Diagram' to begin.")

# Footer
st.markdown(
    """
    ---
    Created with ❤️ using [Streamlit](https://streamlit.io/).  
    Need help? Contact us at [support@example.com](mailto:support@example.com).
    """
)
