import urllib3.request
import numpy as np
import pandas as pd
import plotly.express as px
import requests
import streamlit as st
import xmltodict
from pandas import json_normalize
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_lottie import st_lottie
import folium
import googlemaps
from streamlit_folium import st_folium
from folium import plugins
from folium.plugins import MarkerCluster
from folium import Map, Popup, Marker, Icon, IFrame



st.set_page_config(page_title="Python analysis Streamlit Project.", layout="wide")

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns(
    (0.1, 6, 0.2, 2, 0.1)
)

row0_1.title("Python analysis Streamlit Project.")

with row0_2:
    add_vertical_space()
    st.markdown("###### Cho.HyunJun")

def visitor_area():
        st.subheader("방문자 거주지 분포.")
        st.markdown("###### 방문자 거주지 분포 시각화를 통해 경기도, 인천광역시, 강원도등 순으로 방문객 비율을 보이고 있다.")
        visitorArea = pd.read_csv('https://raw.githubusercontent.com/CHJun47/Data/main/visitor_area.csv', encoding = 'CP949')
        fig3 = px.treemap(visitorArea, path = [px.Constant('대한민국'),'광역지자체명','기초지자체명'], values = '방문자 수(합)',
                            color = '방문자 수(합)',
                            color_continuous_scale = 'GnBu')
        fig3.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig3, theme = "streamlit", use_container_width = True)

def visitor_seoul():
    line1_spacer1, line1_1, line1_spacer2 = st.columns((0.1, 3.2, 0.1))

    with line1_1:
        st.header("Analysis of Seoul Data.")
        st.markdown("###### 서울은 대한민국의 수도이자 많은 관광객들이 몰려 있는 곳이다. 한국을 찾는 많은 관광객들이 주로 서울을 방문하는 경우들이 많다. 서울관광지 Top10 데이터를 분석하여 관광지를 추천해주고자 한다.") 
    row3_space1, row3_1, row3_space2, row3_2, row3_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )
    with row3_1:
        st.subheader("서울 방문자 수")
        st.markdown("###### 코로나19 유행 기간 서울 방문자 수가 급격히 줄어 들었지만, 거리두기가 풀린 뒤 서울 방문객들이 점차 증가하는 추세를 보이고 있다.")
        visitorData = pd.read_csv('https://raw.githubusercontent.com/CHJun47/Data/main/visitorData_seoul.csv', encoding='CP949')
        visitorData.columns = ["기준연월","지역명","방문자 수"]
        fig = px.line(
            visitorData,
            x = '기준연월',
            y = '방문자 수',
            color_discrete_sequence = ["lightgoldenrodyellow"]
        )
        st.plotly_chart(fig, theme = "streamlit", use_container_width = True)

    with row3_2:
        visitor_area()      

visitor_seoul()

def inflow_ouflow_chart():
    row4_spacer1, row4_1, row4_spacer2 = st.columns((0.1, 5, 0.1))
    with row4_1:
        st.subheader("유입 유출 분석")
        st.markdown("###### 서울의 유입 유출 방문객의 분석을 통해 첫 번째로 많이 나타는 경기도 유입은 86.9% ,유출은 85.5%, 두 번째는 인천광역시 유입9.9% ,유출8.2%, 세 번째는 강원도 유입1.1% ,유출3.7%를 나타내고 있음.")
        flowData = pd.read_csv("https://raw.githubusercontent.com/CHJun47/Data/main/inflow_outflow.csv", encoding = 'CP949')
        fig1 = px.parallel_categories(
            flowData,
            color = "유입 비율",
            color_continuous_scale = "GnBu"
            )
        st.plotly_chart(fig1, theme = "streamlit", use_container_width = True)

inflow_ouflow_chart()

def touristDest():
    row5_space1, row5_1, row5_space2, row5_2, row5_space3 = st.columns(
        (0.1, 1, 0.1, 1, 0.1)
    )
    with row5_1:
        st.subheader("관광소비 유형.")
        st.markdown("###### 관광소비 유형으로 1위가 식음료이다. 음식은 그 나라의 문화와 전통을 가장 잘 나타낼 수 있는 관광 자원이다.") 
        st.markdown("###### 한 지역을 대표하는 음식은 때로는 그 자체만으로도 여행의 목적이 되기도 한다.")
        st.markdown("###### 2위로 쇼핑업을 볼 수 있다. 유행하는 옷이나 우리나라를 대표하는 한복을 입고 문화를 즐기고 향유하려는 것을 볼 수 있다.")
        st.markdown("###### 나머지는 운송업, 숙박업, 여가서비스등을 볼 수 있다.")

        tourrist_dest = pd.read_csv("https://raw.githubusercontent.com/CHJun47/Data/main/tourrist_dest.csv", encoding='CP949')
        fig4 = px.treemap(tourrist_dest, path = [px.Constant('점포'),'업종대분류명','업종중분류명'], values = '중분류 소비액(합)',
                            color = '중분류 소비액(합)',
                            color_continuous_scale = "GnBu")
        fig4.update_layout(margin = dict(t=50, l=25, r=25, b=25))
        st.plotly_chart(fig4, theme = "streamlit", use_container_width = True)
    with row5_2:
        st.subheader("SNS언급량.")
        st.markdown("###### 코로나19 거리두기로 여행이나 놀러갈 수 없는 상황이였지만,")
        st.markdown("###### 거리두기가 풀리고 나서부터 SNS에서도 여행, 놀러가는 사진을 SNS에서의 언급량이 점점 증가하고있다.")
        st.markdown("###### ")
        seoul_SNS = pd.read_csv('https://raw.githubusercontent.com/CHJun47/Data/main/seoul_SNS.csv', encoding = 'CP949')
        fig5 = px.bar(
            seoul_SNS,
            x = '기준연월',
            y = '검색량(건)',
            color_discrete_sequence = ["lightgoldenrodyellow"]
        )
        st.plotly_chart(fig5, theme = "streamlit", use_container_width = True)

touristDest()

def Folium_visit():
    row6_spacer1, row6_1, row6_spacer2, row6_2, row_spacer3 = st.columns((0.1, 30, 0.1,5,0.1))
    with row6_1:
        gmaps_key = "AIzaSyCpqSO-mFH36wjjiqUlQPJHhwYkLE9WWns"
        gmaps = googlemaps.Client(key = gmaps_key)
        visitors = pd.read_csv('https://raw.githubusercontent.com/CHJun47/Data/main/visitor(2).csv', encoding='CP949')
        visitors_total = visitors.loc[visitors['내/외국인'] == '합계']
        visitors_total = visitors_total.iloc[:,0:31]
        visit_name = []
        visit_url = []
        for name in visitors.iloc[:,-1]:
            visit_url.append(name)
        
        for name in visitors_total['관광지']:
            visit_name.append('서울'+ str(name))

        visit_address = []
        visit_lat = []
        visit_lng = []

        for name in visit_name:
            tmp = gmaps.geocode(name, language='ko')
            tmp_loc = tmp[0].get("geometry")
            visit_lat.append(tmp_loc['location']['lat'])
            visit_lng.append(tmp_loc['location']['lng'])


        # food.
        food = pd.read_csv('https://raw.githubusercontent.com/CHJun47/Data/main/food(1).csv')
        food_address = []
        food_lat = []
        food_lng = []
        food_name = []

        food_info = []
        food1_info = []
        food2_info = []
        food3_info = []
        food4_info = []
        food5_info = []
        food6_info = []

        food1_name = []
        food2_name = []
        food3_name = []
        food4_name = []
        food5_name = []
        food6_name = []

        for name in food.iloc[:,1]:
            food_name.append(name)

        for add in food.iloc[:,2]:
            food_address.append(str('서울')+add)

        for name in food_address:
            tmp = gmaps.geocode(name, language='ko')
            tmp_loc = tmp[0].get("geometry")
            food_lat.append((tmp_loc['location']['lat']))
            food_lng.append(tmp_loc['location']['lng'])
        food['lat'] = food_lat
        food['lng'] = food_lng

        food1 = food[food['분류'] == '음식점기타']
        for name in food1.iloc[:,5]:
            food1_info.append(name)
        food2 = food[food['분류'] == '한식']
        for name in food2.iloc[:,5]:
            food2_info.append(name)
        food3 = food[food['분류'] == '카페/찻집']
        for name in food3.iloc[:,5]:
            food3_info.append(name)
        food4 = food[food['분류'] == '간이음식']
        for name in food4.iloc[:,5]:
            food4_info.append(name)
        food5 = food[food['분류'] == '전문음식']
        for name in food5.iloc[:,5]:
            food5_info.append(name)
        food6 = food[food['분류'] == '외국식']
        for name in food6.iloc[:,5]:
            food6_info.append(name)

        for name in food1.iloc[:,1]:
            food1_name.append(name)
        for name in food2.iloc[:,1]:
            food2_name.append(name)
        for name in food3.iloc[:,1]:
            food3_name.append(name)
        for name in food4.iloc[:,1]:
            food4_name.append(name)
        for name in food5.iloc[:,1]:
            food5_name.append(name)
        for name in food6.iloc[:,1]:
            food6_name.append(name)

        food1 = pd.pivot_table(food1, index = ['주소'])
        food2 = pd.pivot_table(food2, index = ['주소'])
        food3 = pd.pivot_table(food3, index = ['주소'])
        food4 = pd.pivot_table(food4, index = ['주소'])
        food5 = pd.pivot_table(food5, index = ['주소'])
        food6 = pd.pivot_table(food6, index = ['주소'])

        visitors_total['lat'] = visit_lat
        visitors_total['lng'] = visit_lng
        visitors_total1 = pd.pivot_table(visitors_total, index = ['관광지'])
        map = folium.Map(location=[37.566535, 126.9779692],
        tiles = "stamen Terrain",
        zoom_start= 11)

        marker_cluster = MarkerCluster().add_to(map)

        ######################### 수정.
        if st.checkbox('관광지'):
            for n in range(int(len(visitors_total1))):
                folium.Marker([visitors_total1['lat'][n],
                visitors_total1['lng'][n]],tooltip = '"'+visit_name[n]+'"').add_to(marker_cluster)
        elif st.checkbox('음식점기타'):
            for n1 in range(int(len(food1))):
                folium.Marker([food1['lat'][n1],
                food1['lng'][n1]],popup = "<a href="+'"'+food1_info[n1]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food1_name[n1]+'"',icon = folium.Icon(icon = 'star', color = 'red')).add_to(marker_cluster)
        elif st.checkbox('한식'):
            for n2 in range(int(len(food2))):
                folium.Marker([food2['lat'][n2],
                food2['lng'][n2]],popup = "<a href="+'"'+food2_info[n2]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food2_name[n2]+'"',icon = folium.Icon(icon = 'star', color = 'yellow')).add_to(marker_cluster)
        elif st.checkbox('카페/찻집'):
            for n3 in range(int(len(food3))):
                folium.Marker([food3['lat'][n3],
                food3['lng'][n3]],popup = "<a href="+'"'+food3_info[n3]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food3_name[n3]+'"',icon = folium.Icon(icon = 'star', color = 'green')).add_to(marker_cluster)
        elif st.checkbox('간이음식'):
            for n4 in range(int(len(food4))):
                folium.Marker([food4['lat'][n4],
                food4['lng'][n4]],popup = "<a href="+'"'+food4_info[n4]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food4_name[n4]+'"',icon = folium.Icon(icon = 'star', color = 'orange')).add_to(marker_cluster)
        elif st.checkbox('전문음식'):
            for n5 in range(int(len(food5))):
                folium.Marker([food5['lat'][n5],
                food5['lng'][n5]],popup = "<a href="+'"'+food5_info[n5]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food5_name[n5]+'"',icon = folium.Icon(icon = 'star', color = 'lightgray')).add_to(marker_cluster)
        elif st.checkbox('외국식'):
            for n6 in range(int(len(food6))):
                folium.Marker([food6['lat'][n6],
                food6['lng'][n6]],popup = "<a href="+'"'+food6_info[n6]+'"'+"target ="+"_blank"+">Site</a>",tooltip = '"'+food6_name[n6]+'"',icon = folium.Icon(icon = 'star', color = 'lightcyan')).add_to(marker_cluster)
        
        return map

st.subheader("주변 Search 지도.")
m = Folium_visit()
output = st_folium(m, key = "map", width = 1800, height = 600)