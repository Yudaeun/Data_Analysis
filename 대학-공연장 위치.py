import pandas as pd
from folium import Marker

df=pd.read_excel("서울지역 대학교 위치.xlsx")
df2=pd.read_excel("서울시 문화공간 정보.xlsx")
df2=df2.dropna()
df2['X좌표']=df2['X좌표'].astype(float)
df2['Y좌표']=df2['Y좌표'].astype(float)

seoul_map=folium.Map(location=[37.55,126.98],zoom_start=12)

for _, row in df.iterrows():
  Marker(location=[row['위도'],row['경도']],popup=row['index'],
         icon=folium.Icon(color='blue')).add_to(seoul_map)

for a, row in df2.iterrows():
  if df2['주제분류'][a]=='공연장':
    Marker(location=[row['X좌표'],row['Y좌표']],popup=row['문화시설명'],icon=folium.Icon(icon='star',color='pink')).add_to(seoul_map)
  elif df2['주제분류'][a]=='미술관':
    Marker(location=[row['X좌표'],row['Y좌표']],popup=row['문화시설명'],icon=folium.Icon(icon='star',color='darkblue')).add_to(seoul_map)


seoul_map.save('seoul_universities.html')