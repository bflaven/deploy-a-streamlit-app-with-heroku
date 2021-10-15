#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
[env]

[path]
cd /Users/brunoflaven/Documents/03_git/deploy-a-streamlit-app-with-heroku/

[file]
streamlit run app.py


TabError: inconsistent use of tabs and spaces in indentation

"""
# require in this file
import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt

# from streamlit
import altair as alt




def main():
	""" A simple attempt for heroku"""
	st.title('Attempt streamlit-dashboard app on Heroku')
	st.write('Change again')
 
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


