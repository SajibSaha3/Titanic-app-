import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))
st.write("Model loaded successfully.")

st.title("Titanic survival Analysis system")
st.write("Identify a person is survived or not")

pclass = st.selectbox("Pclass:", [1, 2, 3])
age = st.slider("Age:", 1.0, 100.0, step=0.1)
sibsp = st.selectbox("Siblings/Spouses aboard (sibsp):", range(0, 6))
parch = st.selectbox("Parents/Children aboard (parch):", range(0, 6))
fare = st.slider("Fare:", 0.0, 300.0, step=0.1)
sex = st.selectbox("Sex (1 = male, 0 = female):", [0, 1])
embarked = st.selectbox("Embarked (0 = C, 1 = Q, 2 = S):", [0, 1, 2])
pclass_label = st.selectbox("Class (0 = First, 1 = Second, 2 = Third):", [0, 1, 2])
who = st.selectbox("Who (0 = child, 1 = man, 2 = woman):", [0, 1, 2])
adult_male = st.selectbox("Adult male (0 = No, 1 = Yes):", [0, 1])
embark_town = st.selectbox("Embark Town (0 = Cherbourg, 1 = Queenstown, 2 = Southampton):", [0, 1, 2])
alive = st.selectbox("Alive (0 = No, 1 = Yes):", [0, 1])
alone = st.selectbox("Alone (0 = No, 1 = Yes):", [0, 1])

# Submit button
if st.button("Submit"):
    features= [[pclass, sex, age, sibsp, parch, fare, embarked, pclass_label,
                            who, adult_male, embark_town, alive, alone]]
    
    prediction = model.predict(features)
    result = "Survived" if prediction[0]==1 else "Died"
    st.success(f'Prediction Result is {result} ')


