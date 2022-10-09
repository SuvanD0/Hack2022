import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

st.set_page_config(page_title="Hackthon 2022", page_icon=":tada:", layout="wide")
 
df = pd.read_csv('WTG A.csv')
headerBlock = st.container()
turbines = st.container()
modelTraining = st.container()
conclusion = st.container()


with headerBlock:
    col1,col2 = st.columns([1,1])
    with col2:
        st.caption("**Created by Suvan Dommeti, Kathir Maarikarthykeyan, Aaron Dhillon, Frank Li**")    
    image1 = Image.open('AEPCover.png')
    st.image(image1,width = 1000)
    
    image2 = Image.open('WindTurbine.webp')
    st.image(image2, "science.com")
    st.markdown("""---""") 
    df = pd.read_csv('turbinefinalnobad2.csv')
    df = df.drop(df.columns[0], axis=1)


   
    col1,col2 = st.columns([1,7])
    with col2:
        imageEnergy = Image.open('energy.png')
        st.image(imageEnergy)

    st.subheader("Lets explore some of the Data!")
    st.write("Press turbine icons on right side of graph to view specific turbines!")
    st.text(" ")
    st.text(" ")

    # sampleDF = df.sample(frac=1/20)
    # sampleDF
    sampleDF = df.head(20)




    # fig1 = px.scatter(df,x= "turbine" ,y = 'blade1actual', opacity = .5, title = "Turbine 2 - BLADE 1 - SET VALUE")
    # st.write(fig1)
    xChoice = st.selectbox('X',df.columns)
    yChoice = st.selectbox('Y',df.columns)
    fig1 = px.scatter(df,y= yChoice ,x = xChoice ,color='turbine', opacity = .5, title = "Turbine Data Values")
    fig1.update_layout(autotypenumbers='convert types')

    st.write(fig1)
    col1,col2,col3 = st.columns([1,4,1])
    col2.write("Press turbine icons on right side of graph to view specific turbines!")
    
    
    
    



with turbines:
    st.markdown("""---""") 
    st.header('Which Turbines Had Issue')

    st.markdown("### The turbines we determined were underpreforming were:")
    wTCol1, wTCol2, wTCol3, wTCol4, wTCol5 = st.columns(5)
    wTCol1.metric('Turbine', "A")
    wTCol2.metric('Turbine', "B")
    wTCol3.metric('Turbine', "D")
    wTCol4.metric('Turbine', "H")
    wTCol5.metric('Turbine', "I")


    

    


with modelTraining:
    st.markdown("""---""") 
    col1,col2,col3 = st.columns([1,2,1]) 
    with col2:
        st.header('Machine Learning Model')
    st.markdown("To take the project one step further, we devloped an algorithm to predict future turbine failures. This model can be implemented in the future by responce teams in order to prevent offline turbines. Responders can identify a potential porblem, solving before it gets worse, saving thousands of dollars")
    image3 = Image.open('IMG_8117.jpeg')
    st.image(image3, caption='Using machine and deep learning, we trained a neural network in order to recognize the quality of a wind turbine, trained using over 1500 cleaned data points.')


with conclusion:
    st.markdown("""---""") 
    imageEnd1 = Image.open('EndPic1.png')
    st.image(imageEnd1)
    col1,col2,col3 = st.columns([3,2,2])
    with col2:
        if st.button('PRESS!'):
            st.header('OUR VERY OWN LAKE ERIE!!!')
            st.balloons()
        
        else:
            st.subheader('Press the button')
    
