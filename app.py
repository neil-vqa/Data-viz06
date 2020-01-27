import plotly.graph_objects as do
import pandas as pd
import streamlit as st

@st.cache
def data_load():
	return pd.read_csv('novel_coronavirus.csv')


def main():
	
	df = data_load()
	country = list(df['Country'])
	confirmed = list(df['Confirmed'])
	deaths = list(df['Deaths'])
	suspect = list(df['Suspected'])


	hover_text = ['<b>{}</b>'.format(x) + '<br>Confirmed Cases: ' + '{}'.format(y) + '<br>Deaths: ' + '{}'.format(z) + '<br>Suspected: ' + '{}'.format(v) for x,y,z,v in zip(country,confirmed,deaths,suspect)]

	st.title('Outbreak Watch: Wuhan Coronavirus (2019-nCoV)')
	st.markdown('As of 27 January 2020 11:00AM PST')
	st.header('Confirmed Cases: ' + str(df['Confirmed'].sum()))
	st.header('Deaths: ' + str(df['Deaths'].sum()))
	st.markdown('-----------------------')
	st.markdown('*View full screen control in the upper right corner of the map.*')

	plot = do.Figure(
		data= do.Choropleth(
			locations = df['Code'],
			z= df['Confirmed'],
			text= hover_text,
			hoverinfo= 'text',
			colorscale = 'armyrose',
			reversescale=True,
			autocolorscale=False,
			showscale=False
		)
	)

	plot.update_layout(
		geo={'showframe':False, 'projection_type':'equirectangular',
	      	'landcolor':'#cfcfc4'}
	)


	st.plotly_chart(plot,use_container_width=True)

	st.markdown('Data Sources:  WHO, CDC, NHC and Dingxiangyuan | Viz by: nvqa')

if __name__ == '__main__':
	main()

