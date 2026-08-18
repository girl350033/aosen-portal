import streamlit as st

st.set_page_config(page_title="澳森 AI 工具中心", page_icon="🧸", layout="wide")

st.title("🌱行政工具")
st.write("歡迎使用，請選擇您要操作的工具：")

# 使用卡片式排列 (Columns)
col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 教學與紀錄")
    st.page_link("https://aosen-leappn-plan-lepkegu2y65tjdwqru7vjh.streamlit.app/", label="教案設計系統", icon="📝")
    st.page_link("https://aosen-observation-egcfxfbk8wnvttxc5eqbmn.streamlit.app/", label="教學觀察工具", icon="👀")

with col2:
    st.subheader("🛠 行政與盤點")
    st.page_link("https://aosen-monthlycleaning-6oyx3grsulh5fwzaxhbieo.streamlit.app/#920fe149", label="環境清潔紀錄", icon="🧹")
    st.page_link("https://nursery-inventory-angkizkysrp7wxqtad3fxg.streamlit.app/", label="西湖庫存盤點", icon="📦")
    st.page_link("https://nursery-inventory-xihu-vpfnntbsxxnpee76hpushc.streamlit.app/", label="文德庫存盤點", icon="🏥")

st.divider()
st.info("💡 提示：點擊上方連結即可切換到對應的網頁。")
