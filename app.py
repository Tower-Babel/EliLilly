import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("eli_report_24.csv")

selected_columns = ['Immunology | U.S.', 'Immunology | Outside U.S.',
                    'Neuroscience | U.S.', 'Neuroscience | Outside U.S.',
                    'Diabetes and Obesity | U.S.', 'Diabetes and Obesity | Outside U.S.',
                    'Oncology | U.S.', 'Oncology | Outside U.S.']

means = data[selected_columns].mean()
stds = data[selected_columns].std()

cis = 1.96 * stds / np.sqrt(len(data))

st.title('Eli Lilly Revenue')

fig, ax = plt.subplots()
ax.bar(selected_columns, means, yerr=cis, capsize=5)

ax.set_xlabel('Drugs')
ax.set_ylabel('Revenue in Billions')
ax.set_title('')

plt.xticks(rotation=90)
st.pyplot(fig)

#Howdy Alex!!
