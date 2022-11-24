import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40],
})

st.dataframe(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)
st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)


df = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.map(df)

img = Image.open('sample.jpg')
st.image(img,caption='フィンセント・ファン・ゴッホ「ローヌ川の星月夜」（1888年）',use_column_width=True)



#  インタラクティブなウィジェット

if st.checkbox('Show Image'):
    img = Image.open('sample.jpg')
    st.image(img,caption='フィンセント・ファン・ゴッホ「ローヌ川の星月夜」（1888年）',use_column_width=True)


option = st.selectbox(
    'あたなが好きな数字を教えてください。',
    list(range(1,11))
)

'あたなが好きな数字は',option,'です。'


st.title('Interactive Widgts')


# レイアウトを整える

# text = st.sidebar.text_input('あなたの趣味を教えてください。')
# condition = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あたなたの趣味：', text
# 'コンディション：', condition


text = st.text_input('あなたの趣味を教えてください。')
'あたなたの趣味：', text

condition = st.slider('あなたの今の調子は？',0,100,50)
'コンディション：', condition


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')


expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


# プログレスバーの表示

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!!!'

