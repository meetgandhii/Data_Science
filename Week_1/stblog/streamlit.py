import streamlit as st
from PIL import Image

# st.title("Hello Everyone!")
# st.header("Hello Everyone")
# st.subheader("Hello Everyone")
# st.text("Hello Everyone")
# st.markdown("# Hello Everyone")
# st.markdown("## Hello Everyone")
# st.markdown("### Hello Everyone")
# st.markdown("#### Hello Everyone")
# st.markdown("##### Hello Everyone")

# st.success("Hello Everyone")
# st.info("Hello Everyone")
# st.warning("Hello Everyone")
# st.error("Hello Everyone")

# def ten():
#     for i in range(10):
#         st.write(i)

# ten()

# st.write(222/2)
# st.text(222/2)

# img = Image.open("sunrise-over-beach-cancun-beautiful-mexico-40065727.jpg ")
# st.image(img)

# img2 = Image.open("photo-1507525428034-b723cf961d3e.jpg ")
# st.image(img2)

# img3 = Image.open("istockphoto-1150862958-170667a.jpg ")
# st.image(img3)

# if st.checkbox("Show/Hide"):
#   st.image(img3)

# genderselected = st.radio("Select Gender: ", ("Male", "Female"))
# st.success(genderselected)

# hobby = st.selectbox("Select your hobbies: ", ["Sleeping", "Eating", "Watching TV", "Playing"])
# st.success(hobby)

# hobby = st.multiselect("Select your hobbies: ", ["Sleeping", "Eating", "Watching TV", "Playing"])
# hobbyprint = ""
# for i in hobby:
#     hobbyprint += i + ", "
# st.success(hobbyprint)

# if(st.button("About")):
#     st.success("Done!!!")

# name = st.text_input("Enter name", "hint text")
# if (st.button("submit")):
#     st.success(name)
    
# slider = st.slider("Select your height", 130, 210)
# st.success(slider)

#############################################
#############################################
########## MINI PROJECT BMI APP ############# 
############################################# 
############################################# 

st.title("BMI APP")

weight = st.number_input("Enter your weight in kgs", 10.0, 100.0, step=0.1)
st.success("You have entered your weight as {} kgs".format(weight))

heightlabel = st.markdown("### Choose which format you want your height to be entered in")
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.button("Cms")
# with col1:
#     st.button("Feet")
# with col1:
#     st.button("Meters")
# if(col1):
#     pass
# if(col2):
#     pass
# if(col3):
#     pass
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.button("Feet")
# with col2:
#     st.button("Cms")
# with col3:
#     st.button("Meters")
# if col1:
#     st.success("Feet")
# if(col2):
#     st.success("Cms")
# if(col3):
#     st.success("Meters")

heightformat = st.radio("", ["Cms", "Feet", "Meters"])

if heightformat=="Cms":
    height = st.slider("Select your height in cms", 120.0, 210.0, 120.0,0.1 )/100
elif heightformat=="Feet":
    heightfeet = st.number_input("Enter your height in feet", 3, help="Write only the feet part")
    heightinch = st.number_input("Enter your height in inches", min_value=0, help="Write only the inch part")
    height = (heightfeet*12 + heightinch)/39.37
elif heightformat == "Meters":
    height = st.slider("Select your height in meters", 1.200, 2.100, 1.200, 0.001)
if(st.button("Click here to find your BMI")):
    bmi = str(weight/height**2)
    st.title(bmi)
    st.balloons()