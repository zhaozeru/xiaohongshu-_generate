# 这里写UI展示的代码
import streamlit as st
import openai
from generate_script import generate_xiaohongshu

st.title("✍️ 爆款小红书AI生成助手！！")
st.divider()
with st.sidebar:
    openai_apikey = st.text_input("请输入您的OpenAI API密钥：", type='password')
    st.markdown("[获取OpenAI API密钥地址 🔑](https://platform.openai.com/account/api_keys)")
theme = st.text_input('🏷️ 请输入主题：')
st.divider()
submit = st.button('开始生成')

if submit and not openai_apikey:
    st.info('请输入您的OpenAI API密钥！！')
    st.stop()
if submit and not theme:
    st.info('请输入主题！！')
    st.stop()
if submit:
    try:
        with st.spinner("💦 内容正在路上..."):
            result = generate_xiaohongshu(theme, openai_apikey)
        st.divider()
        left,right = st.columns(2)
        with left:
            st.markdown('##### 小红书标题1：')
            st.write(result.titles[0])
            st.markdown('##### 小红书标题2：')
            st.write(result.titles[1])
            st.markdown('##### 小红书标题3：')
            st.write(result.titles[2])
            st.markdown('##### 小红书标题4：')
            st.write(result.titles[3])
            st.markdown('##### 小红书标题5：')
            st.write(result.titles[4])
        with right:
            st.markdown('##### 小红书正文：')
            st.write(result.content)
    except openai.AuthenticationError:
        st.error('OpenAI API密钥无效，请检查您的输入！！')
    except Exception as e:
        st.error(f'生成脚本时发生未知错误：{e}')
