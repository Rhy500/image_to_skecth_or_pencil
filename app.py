import streamlit as st
from PIL import Image
from io import BytesIO
import numpy as np 
import cv2

def convert_to_watercolor_sketch(inp_img):
    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
    img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5)
    return img_water_color

def pencil_sketch(inp_img):
    img_pencil_sketch, _ = cv2.pencilSketch(inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825)
    return img_pencil_sketch

def main():
    st.title('IMAGE TO SKETCH CONVERTER')
    st.write("Transform your image into a watercolor sketch or pencil sketch")
    st.subheader("Upload Your Image")
    
    image_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
    
    if image_file is not None:
        option = st.selectbox(
            'Select conversion type:',
            ('Convert to watercolor sketch', 'Convert to pencil sketch')
        )
        
        # Open the image only once
        image = Image.open(image_file)
        
        if option == 'Convert to watercolor sketch':
            final_sketch = convert_to_watercolor_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(image, width=250)
            
            with col2:
                st.header("Watercolor Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                im_pil.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="watercolor_sketch.png",
                    mime="image/png"
                )
        
        elif option == 'Convert to pencil sketch':
            final_sketch = pencil_sketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            
            col1, col2 = st.columns(2)
            with col1:
                st.header("Original Image")
                st.image(image, width=250)
            
            with col2:
                st.header("Pencil Sketch")
                st.image(im_pil, width=250)
                buf = BytesIO()
                im_pil.save(buf, format="PNG")
                byte_im = buf.getvalue()
                st.download_button(
                    label="Download image",
                    data=byte_im,
                    file_name="pencil_sketch.png",
                    mime="image/png"
                )

if __name__ == '__main__':
    main()