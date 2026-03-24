import streamlit as st
import hashlib

# ── PAGE CONFIG
st.set_page_config(
    page_title='DSM_General_Seller_Tool',
    page_icon='⚡',
    layout='wide'
)

# ── CREDENTIALS (SHA256 Hashed | Managed by Admin)
config = {
    'credentials': {
        'usernames': {
            'user1': {
                'name'    : 'user1',
                'email'   : 'user1@yourorg.com',
                'password': '2533a3996a9069b9ac809867e5f2bd9f150c08c1334519d2e30827f8c23e559f'
            },
        }
    }
}

# ── VERIFY LOGIN
def verify_login(username, password):
    users = config['credentials']['usernames']
    if username in users:
        stored = users[username]['password']
        entered_hash = hashlib.sha256(password.encode()).hexdigest()
        if stored == entered_hash or stored == password:
            return users[username]['name']
    return None

# ── SESSION STATE
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''
if 'name' not in st.session_state:
    st.session_state.name = ''

# ── LOGIN PAGE
def show_login():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('## ⚡ DSM_General_Seller_Tool')
        st.markdown('### 🔐 Please Login')
        st.markdown('---')
        username = st.text_input('Username', key='inp_user')
        password = st.text_input('Password', type='password', key='inp_pass')
        if st.button('Login', use_container_width=True, type='primary'):
            name = verify_login(username, password)
            if name:
                st.session_state.logged_in  = True
                st.session_state.username   = username
                st.session_state.name       = name
                st.rerun()
            else:
                st.error('❌ Incorrect Username or Password')

# ── MAIN APP
def show_app():
    with st.sidebar:
        st.markdown('### 👤 Welcome!')
        st.markdown('**' + st.session_state.name + '**')
        st.caption('Logged in as: ' + st.session_state.username)
        st.markdown('---')
        if st.button('🚪 Logout', use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username  = ''
            st.session_state.name      = ''
            st.rerun()
    st.title('⚡ DSM_General_Seller_Tool')
    st.markdown('---')
    try:
        with open('DSM_Audit_General_Seller_44.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
        st.components.v1.html(html_content, height=900, scrolling=True)
    except Exception as e:
        st.error('Error loading tool: ' + str(e))

# ── ROUTER
if st.session_state.logged_in:
    show_app()
else:
    show_login()
