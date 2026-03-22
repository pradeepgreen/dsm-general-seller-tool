import streamlit as st
import hashlib

# -- PAGE CONFIG
st.set_page_config(
    page_title='DSM_General_Seller_Tool',
    page_icon='lightning',
    layout='wide'
)

# -- CREDENTIALS
config = {
    'credentials': {
        'usernames': {
            'admin': {
                'name': 'Administrator',
                'email': 'admin@yourorg.com',
                'password': 'Admin@123'
            }
        }
    }
}

# -- VERIFY LOGIN
def verify_login(username, password):
    users = config['credentials']['usernames']
    if username in users:
        stored = users[username]['password']
        if stored == hashlib.sha256(password.encode()).hexdigest() or stored == password:
            return users[username]['name']
    return None

# -- SESSION STATE
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'name' not in st.session_state:
    st.session_state.name = ''

# -- LOGIN PAGE
def show_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('## DSM_General_Seller_Tool')
        st.markdown('### Please Login')
        st.markdown('---')
        username = st.text_input('Username', key='inp_user')
        password = st.text_input('Password', type='password', key='inp_pass')
        if st.button('Login', use_container_width=True, type='primary'):
            name = verify_login(username, password)
            if name:
                st.session_state.logged_in = True
                st.session_state.name = name
                st.rerun()
            else:
                st.error('Incorrect Username or Password')

# -- MAIN APP
def show_app():
    with st.sidebar:
        st.markdown('### Welcome!')
        st.markdown('**' + st.session_state.name + '**')
        st.markdown('---')
        if st.button('Logout', use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.name = ''
            st.rerun()
    st.title('DSM_General_Seller_Tool')
    st.markdown('---')
    tabs = st.tabs(['dsm-WS_Pumping_20', 'DSM_Audit_Complete_Final_38', 'DSM_Audit_Complete_Final_39', 'DSM_Audit_Dashboard_FIXED (1)', 'DSM_Audit_Dashboard_General Seller_41', 'DSM_Audit_General_Seller_42', 'DSM_Audit_General_Seller_43', 'DSM_Audit_General_Seller_44', 'DSM_Audit_Result_24', 'DSM_Audit_Result_25', 'DSM_Audit_Result_26', 'DSM_Audit_Result_27', 'DSM_Audit_Result_28', 'DSM_Audit_Result_29', 'DSM_Audit_Result_30', 'DSM_Audit_Result_31', 'DSM_Audit_Result_32', 'DSM_Audit_Result_33', 'DSM_Audit_Result_34', 'DSM_Audit_Result_35', 'DSM_Audit_Result_36', 'DSM_Audit_Result_37', 'Final_DSM_Dashboard_General_Seller_40', 'Generation_New text document', 'New text document_10', 'New text document_11', 'New text document_12', 'New text document_13', 'New text document_14', 'New text document_15', 'New text document_16', 'New text document_17', 'New text document_18', 'New text document_19', 'New text document_20', 'New text document_21', 'New text document_22', 'New text document_23', 'New text document_7', 'New text document_8', 'New text document_9'])
    with tabs[0]:
        try:
            with open('dsm-WS_Pumping_20.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading dsm-WS_Pumping_20.html: ' + str(e))
    with tabs[1]:
        try:
            with open('DSM_Audit_Complete_Final_38.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Complete_Final_38.html: ' + str(e))
    with tabs[2]:
        try:
            with open('DSM_Audit_Complete_Final_39.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Complete_Final_39.html: ' + str(e))
    with tabs[3]:
        try:
            with open('DSM_Audit_Dashboard_FIXED (1).html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Dashboard_FIXED (1).html: ' + str(e))
    with tabs[4]:
        try:
            with open('DSM_Audit_Dashboard_General Seller_41.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Dashboard_General Seller_41.html: ' + str(e))
    with tabs[5]:
        try:
            with open('DSM_Audit_General_Seller_42.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_General_Seller_42.html: ' + str(e))
    with tabs[6]:
        try:
            with open('DSM_Audit_General_Seller_43.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_General_Seller_43.html: ' + str(e))
    with tabs[7]:
        try:
            with open('DSM_Audit_General_Seller_44.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_General_Seller_44.html: ' + str(e))
    with tabs[8]:
        try:
            with open('DSM_Audit_Result_24.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_24.html: ' + str(e))
    with tabs[9]:
        try:
            with open('DSM_Audit_Result_25.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_25.html: ' + str(e))
    with tabs[10]:
        try:
            with open('DSM_Audit_Result_26.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_26.html: ' + str(e))
    with tabs[11]:
        try:
            with open('DSM_Audit_Result_27.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_27.html: ' + str(e))
    with tabs[12]:
        try:
            with open('DSM_Audit_Result_28.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_28.html: ' + str(e))
    with tabs[13]:
        try:
            with open('DSM_Audit_Result_29.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_29.html: ' + str(e))
    with tabs[14]:
        try:
            with open('DSM_Audit_Result_30.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_30.html: ' + str(e))
    with tabs[15]:
        try:
            with open('DSM_Audit_Result_31.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_31.html: ' + str(e))
    with tabs[16]:
        try:
            with open('DSM_Audit_Result_32.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_32.html: ' + str(e))
    with tabs[17]:
        try:
            with open('DSM_Audit_Result_33.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_33.html: ' + str(e))
    with tabs[18]:
        try:
            with open('DSM_Audit_Result_34.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_34.html: ' + str(e))
    with tabs[19]:
        try:
            with open('DSM_Audit_Result_35.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_35.html: ' + str(e))
    with tabs[20]:
        try:
            with open('DSM_Audit_Result_36.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_36.html: ' + str(e))
    with tabs[21]:
        try:
            with open('DSM_Audit_Result_37.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading DSM_Audit_Result_37.html: ' + str(e))
    with tabs[22]:
        try:
            with open('Final_DSM_Dashboard_General_Seller_40.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading Final_DSM_Dashboard_General_Seller_40.html: ' + str(e))
    with tabs[23]:
        try:
            with open('Generation_New text document.html.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading Generation_New text document.html.html: ' + str(e))
    with tabs[24]:
        try:
            with open('New text document_10.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_10.html: ' + str(e))
    with tabs[25]:
        try:
            with open('New text document_11.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_11.html: ' + str(e))
    with tabs[26]:
        try:
            with open('New text document_12.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_12.html: ' + str(e))
    with tabs[27]:
        try:
            with open('New text document_13.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_13.html: ' + str(e))
    with tabs[28]:
        try:
            with open('New text document_14.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_14.html: ' + str(e))
    with tabs[29]:
        try:
            with open('New text document_15.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_15.html: ' + str(e))
    with tabs[30]:
        try:
            with open('New text document_16.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_16.html: ' + str(e))
    with tabs[31]:
        try:
            with open('New text document_17.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_17.html: ' + str(e))
    with tabs[32]:
        try:
            with open('New text document_18.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_18.html: ' + str(e))
    with tabs[33]:
        try:
            with open('New text document_19.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_19.html: ' + str(e))
    with tabs[34]:
        try:
            with open('New text document_20.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_20.html: ' + str(e))
    with tabs[35]:
        try:
            with open('New text document_21.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_21.html: ' + str(e))
    with tabs[36]:
        try:
            with open('New text document_22.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_22.html: ' + str(e))
    with tabs[37]:
        try:
            with open('New text document_23.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_23.html: ' + str(e))
    with tabs[38]:
        try:
            with open('New text document_7.html.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_7.html.html: ' + str(e))
    with tabs[39]:
        try:
            with open('New text document_8.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_8.html: ' + str(e))
    with tabs[40]:
        try:
            with open('New text document_9.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            st.components.v1.html(html_content, height=900, scrolling=True)
        except Exception as e:
            st.error('Error loading New text document_9.html: ' + str(e))

# -- ROUTER
if st.session_state.logged_in:
    show_app()
else:
    show_login()
