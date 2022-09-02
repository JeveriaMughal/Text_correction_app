import streamlit as st
import os
import ocr_core
import closest_match

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
class data:
	msg_modified=""
def app():
	local_css("style.css")
	st.image("left-1 - Copy.jpg")
	st.markdown('<h1 class="urdu-font-big">صحیح لفظ کا انتخاب کریں</h1>', unsafe_allow_html=True)
	message=st.text_input("جملہ درج کریں",value =data.msg_modified)
	st.markdown('<p class="urdu-font">'+message+'</p>', unsafe_allow_html=True)
	word=[]
	new_words=[]
	word=message.split()
	st.write(len(message),"الفاظ")
	correct_this_word=st.selectbox('آپ کون سا لفظ بدلنا چاہیں گے؟',word)
	#form=st.form("change_text")
	buttonTranslate = st.button('تجاویز')

	if st.session_state.get('button') != True:

		st.session_state['button'] = buttonTranslate

	if st.session_state['button'] == True:

		new_words=closest_match.closest_match_multiple(correct_this_word)
		new_word=st.selectbox("ایک متبادل لفظ منتخب کریں۔",new_words)

		if st.button('تبدیل'):
			message=message.replace(str(correct_this_word),str(new_word))
			st.markdown('<p class="urdu-font-big">درست تحریر</p>', unsafe_allow_html=True)
			st.markdown('<p class="urdu-font">"'+message+'"</p>', unsafe_allow_html=True)	
			st.session_state['button'] = False
			st.download_button('درست تحریر ڈاؤن لوڈ کریں', message)
			st.checkbox("مزید تبدیلیاں کریں")
			data.msg_modified=message

	


	
	
