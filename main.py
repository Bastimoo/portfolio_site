import streamlit as st
import csv

#setup layout
#print("Monkey")
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
st.write("Testtext")
col3, col4 = st.columns(2)
#create header with photo, description, short text
with col1:
    st.image("images/photo.png", width=500)
with col2:
    st.title("Bastian Hörger")
    selfdescription = """
    This is a placeholder for text about me!
    """
    st.info(selfdescription)


#iterate over data.csv to create the different app-tabs

with open("data.csv", newline="") as datafile:
    datacontent = csv.reader(datafile, delimiter=";")
    datacontentlength = sum(1 for line in datacontent)
    print("Datacontentlength is " + str(datacontentlength))

print("Johnny")
with open("data.csv", newline="") as datafile:
    datacontent = csv.reader(datafile, delimiter=";")
    linecount = 0
    #print(type(datacontent))
    for row in datacontent:
        if linecount == 0:
            print(f'The columns are structured {", ".join(row)}')
            #print("Johnson")
            linecount += 1
        elif linecount < datacontentlength/2:
            with col3:
                st.title(f"{row[0]}")
                st.image(f"images/{row[3]}", width=400)
                st.write(f"{row[1]}")
                st.write(f"{row[2]}")
            #print(f'Titless is {row[0]}. Description is {row[1]}, URL is {row[2]}, image is {row[3]}' + f'first half number is {linecount}')
            linecount += 1
        else:
            with col4:
                st.title(f"{row[0]}")
                st.image(f"images/{row[3]}", width=400)
                st.write(f"{row[1]}")
                st.write(f"{row[2]}")
            print(f'The number is {linecount}')
            linecount += 1
