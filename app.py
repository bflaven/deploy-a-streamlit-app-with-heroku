#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
[env]
conda create --name heroku_python_getting_started_1 python=3.9.7
conda info --envs
source activate heroku_python_getting_started_1
conda deactivate



[path]
cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku/



[file]
streamlit run app.py

# remove from requirements.txt
numpy==1.18.4
pandas==1.0.3
seaborn==0.10.1
matplotlib==3.4.2
plotly-express==0.4.1
altair==4.1.0
pip==21.3

# no needed
# import seaborn as sns
# import datetime as dt
# import altair as alt


# st.write("seaborn :: ", sns.__version__)
# st.write("datetime :: ", dt.__version__)
# st.write("altair :: ", dt.__version__)



"""
# require in this file
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



def detectVersion():
    st.sidebar.markdown('**VERSIONS**')
    st.sidebar.write("panda ::", pd.__version__)
    st.sidebar.write("numpy :: ", np.__version__)
    


def main():
	""" A simple attempt for heroku"""
	st.title('Attempt_1 streamlit-dashboard app on Heroku')
	st.write('enable some libraries :: streamlit, pandas, numpy, matplotlib')
 
  
 
	df = pd.DataFrame(
            np.random.randn(45, 3),
            columns=['John', 'Dave', 'Yuri']
        )

	columns = st.multiselect(
			label='What column to you want to display', options=df.columns)

	#check if variable is empty
	if not columns:
		st.info("No column selected...")
	else:
		st.write(df[columns])
		fig, ax = plt.subplots()
		ax = plt.hist(df[columns])
		st.pyplot(fig)

	# if st.checkbox('Show another fake dataframe\'s example'):
	# 	st.dataframe(pd.DataFrame({
	# 		'first column': [1, 2, 3, 4],
	# 		'second column': [10, 20, 30, 40]
	# 	}))
 
 
if __name__ == '__main__':
    main()
    detectVersion()


