import streamlit as st
import clips
import logging

# Setup working enviroment
logging.basicConfig(level=15, format='%(message)')

env = clips.Enviroment()
router = clips.LoggingRouter()
env.add_router(router)

# Input 
name = st.text_input("Enter your name")

# Knowladge base
env.build('(deftemplate result(slot name))')

# Add facts to working memory
env.assert_string(f'(result (name "{name}))')

# Inference
env.run()

# Output
result = []
for fact in env.fact():
        if fact.templete.name == 'result':
                result.append(fact['name'])


st.write(result[0], "output")