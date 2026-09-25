#to create virtual environment first =python -m venv env
# and then activate it through = .\env\Scripts\activate

import streamlit as st 
import os 
from diet import bmi_calculator,bmr_calculator,tdee_calculator,calorie_target
from rag import load_rag
from openai import OpenAI
from dotenv import load_dotenv

#-----------LLM importng---------


load_dotenv()
HF_token=os.getenv("HF_TOKEN")
client=OpenAI(base_url="https://router.huggingface.co/v1",api_key=HF_token)



#---------------------<><>-----------------------------------------------
st.set_page_config(page_title="Health Assistant",
              page_icon="🤸",
              layout="wide")
st.title("AI Health Assistant 🤸")
st.write("Personal Health and Diet Recommendation Agent")
st.header("Health Information🤏🏼")

#create a sidebar
#--------------------------------controrls---------------------------#
st.sidebar.header("💁🏼‍♂️Your Information ")
gender=st.sidebar.selectbox("Gender",["Male","Female"])
age=st.sidebar.number_input("Age",1,100)
weight =st.sidebar.number_input("weight(kg)",1,120)
height=st.sidebar.number_input("height(cm)",100,200)

activity = st.sidebar.selectbox(
    "🏃Activity",
    [
        "Sedentary",
        "Lightly_Active",
        "Moderately_Active",
        "Very_Active",
        "Extra_Active"
    ]
)
aim=st.sidebar.selectbox("🎯Aim",["Weight maintain","Weight loss","Weight gain"])

diet_type=st.sidebar.selectbox("🥗Diet Type",["Vegeterian","Non Vegeterian"])
allergies=st.sidebar.selectbox("⚠️Allergies",["Allergies","None"])


#------------------------------------------------------------------------------#
#calculations
bmi=bmi_calculator(weight,height)
bmr=bmr_calculator(gender,age,weight,height)
tdee=tdee_calculator(bmr,activity)
calories=calorie_target(tdee,aim)

#--------------------
col1,col2,col3,col4=st.columns(4)
col1.metric("BMI",bmi)
col2=col2.metric("BMR",f"{bmr}kcal🔥")
col3=col3.metric("TDEE",f"{tdee}kcal🔥")
col4=col4.metric("Calorie Target",f"{calories}kcal🔥")


tab1,tab2=st.tabs(['🥗Diet Recommandation',"🤖AI Health🩺Assitance"])

with tab1:
    if st.button("Recommend Diet"):
        if client:
            with st.spinner("creating Diet with 🤖......."):
                try:
                    db=load_rag()
                    search_query=f"""diet_type{diet_type}
                                     Healthy Food
                                     Protein
                                     Allergies{allergies}"""
                    docs=db.similarity_search(search_query,3)
                    context="\n\n".join([doc.page_content for doc in docs])
                    prompt=f"""
You are a helpful AI nutrition assistant.



Use the following nutrition knowledge

to create a simple one-day diet plan.



NUTRITION KNOWLEDGE:


{context}


USER INFORMATION:



Age: {age}



Gender: {gender}



Height: {height} cm



Weight: {weight} kg



Activity Level: {activity}


aim: {aim}


Diet Type: {diet_type}

Food Allergy: {allergies}

Estimated BMI: {bmi}

Estimated BMR: {bmr} kcal/day



Estimated TDEE: {tdee} kcal/day

Estimated Daily Calorie Target:

{calories} kcal/day

Create the following:

1\. Breakfast

2\. Morning Snack

3\. Lunch

4\. Evening Snack

5\. Dinner





For every meal provide:



\- Food

\- Portion

\- Approximate calories

\- Approximate protein





IMPORTANT RULES:



\- Respect the user's diet type.

\- Do not recommend foods containing

&#x20; the stated allergy.

\- Use the provided nutrition knowledge

&#x20; when possible.

\- Keep the plan simple and practical.

\- Do not diagnose diseases.

\- Do not prescribe medicines.

\- Do not claim to cure diseases.

\- This is general wellness information,

&#x20; not medical advice.
 """
            
                    response=client.chat.completions.create(
                         model="openai/gpt-oss-120b",
                         messages=[{
                             "role":"user",
                             "content":prompt
                         }]
                    
                    )   
                    answer=response.choices[0].message.content
                    st.markdown(answer)
                except:
                    st.error("Rag is not connected")

with tab2:
    question=st.text_area("Ask About Health",
                 placeholder="eg:Good source of veg protein")
    if st.button("Ask AI"):
        db=load_rag()
        docs=db.similarity_search(question,3)
        context="\n\n".join([doc.page_content for doc in docs])
        prompt=f""" 

You are an AI health and nutrition

assistant.

Use the following knowledge to answer

the user's question.

NUTRITION KNOWLEDGE:

{context}

USER QUESTION:

{question}

INSTRUCTIONS:


\- Answer clearly.

\- Keep the explanation beginner-friendly.

\- Use the provided knowledge when possible.

\- Do not invent medical facts.

\- Do not diagnose diseases.

\- Do not prescribe medicines.

\- Do not claim to cure diseases.

\- If the question concerns a serious

&#x20; medical problem, recommend consulting

&#x20; a qualified healthcare professional.


This application provides general health

and nutrition information for educational

and wellness purposes.

"""
        response=client.chat.completions.create(
                         model="openai/gpt-oss-120b",
                         messages=[{
                             "role":"user",
                             "content":prompt
                         }])
        answer=response.choices[0].message.content
        st.markdown(answer)
st.markdown(
    """
    <div class="footer">

        🩺 AI Health Assistant 
        Built with Python + Streamlit + RAG + LLM
        
        ⚠️ This application provides general educational information
        and is not a substitute for professional medical advice.
    </div>
    """,
    unsafe_allow_html=True
)




