import time
import streamlit as st
from together import Together
import pandas as pd

def runPrompt():
    client = Together()
    response = client.chat.cfompletions.create(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
    messages=[{"role": "user", "content": f"""Given that i am an Hong Kong Auxiliary Medical Service (醫療輔助隊) member, 
               help me to write a letter to resign.
               
               If these fields are not empty, help me to include in the content:
               Name: {name}, Number: {number}, Team: {team}.

               In my letter, follow the below requirements (if any): {prompt}

               The golden rule of generation result is to stick to my requirement: answer as a resign letter only,
               do not output anything else.

               output in the following languages:
               {langSelection}

                When using cantonese, use Hong Kong Cantonese.
               
               """}],)
    return response
############################################################################################################
df = pd.DataFrame(
    {
        "Region": ["Hong Kong", "Kowloon", "NT East", "NT West"],
        "OTO Email": ["otoh@ams.gov.hk", "otok@ams.gov.hk", "otonte@ams.gov.hk", "otontw@ams.gov.hk"],
        "Tel": ["2762 2045", "2762 2037", "2762 2042", "2762 2044"]
    }
)


st.title("退隊易 AMS Quit")
st.title("""
退隊易
""")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Name (Optional)" , placeholder="你個名")
    number = st.text_input("Number (Optional)", placeholder="你冧把")
    team = st.text_input("Team (Optional)")
    prompt = st.text_area("Extra instructions (Optional)", placeholder="有咩額外要求")

    options = ["English", "中文", "廣東話"]
    langSelection = st.pills("Language", options, selection_mode="multi")

    if st.button("退!", icon=":material/mood:", use_container_width=True) :
        # If no language is selected, prompt user to select one
        if not langSelection:
            st.error("Please select a language")
        else:
            with col2:
                st.write(runPrompt().choices[0].message.content)
                st.toast('Hip!')
                time.sleep(.5)
                st.toast('Hip!')
                time.sleep(.5)
                st.toast('Hooray!', icon='🎉')

    st.table(df)




