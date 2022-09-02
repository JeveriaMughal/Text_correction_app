import streamlit as st
import os
import ocr_core
import closest_match
import time


def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('فائل منتخب کریں', filenames)
    return os.path.join(folder_path, selected_filename)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def app():
	local_css("style.css")
	st.image("left-1 - Copy.jpg")
	st.markdown('<h1 class="urdu-font-big">تصویر سے اردو تحریر</h1>', unsafe_allow_html=True)
	filename = file_selector(folder_path="/run/user/1000/gvfs/sftp:host=192.168.18.17/home/j-mughal/Documents/tess_test/test_data")
	st.image(filename)


	if not filename:
		st.warning('Please input a file name.')
		st.stop()
	images=[]
	num= 0
	message=""
	# progress=st.progress(0)
	# i=0
	# for i in range (1,50,1):
	# 	time.sleep(.01)
	# 	progress.progress(i*2)

	message=ocr_core.ocr_core(filename)
	st.markdown('<p class="urdu-font-big">شناخت شدہ الفاظ</p>', unsafe_allow_html=True)	
	st.markdown('<p class="urdu-font">'+message+'</p>', unsafe_allow_html=True)
	st.download_button('تحریر ڈاؤن لوڈ کریں', message)
	st.image("partition.png")
	word=[]
	word=message.split()
	
	# st.write(len(message),"الفاظ")
	# correct_this_word=st.selectbox('آپ کون سا لفظ بدلنا چاہیں گے؟',word)
	# form=st.form("change_text")
	# submitted=form.form_submit_button("اصلاح")
	# if submitted:
	# 	new_word=closest_match.closest_match(correct_this_word)
	# 	st.write("closest match is : ", new_word)
	# 	message=message.replace(str(correct_this_word),str(new_word))
	# 	st.markdown('<p class="urdu-font-big">درست تحریر</p>', unsafe_allow_html=True)	
	# 	st.markdown('<p class="urdu-font">'+message+'</p>', unsafe_allow_html=True)	
	# 	st.download_button('درست تحریر ڈاؤن لوڈ کریں', message)


	
	# #st.button(label="start data exctraction",on_click=([num,images]=main.start(URL=name,category=cat)))
	
