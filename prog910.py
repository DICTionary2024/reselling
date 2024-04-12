import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the web app
st.title('Product Reselling Statistical Analysis')

# Sidebar for user input
st.sidebar.title('Options')
selected_option = st.sidebar.selectbox(
    'Select a statistical representation:',
    ('Bar Plot', 'Pie Chart')
)

# Collecting user input for product data
st.sidebar.subheader('Enter Product Data')
num_products = st.sidebar.number_input('Number of Products', min_value=1, max_value=10, value=5)

products = []
units_sold = []
returns = []

for i in range(num_products):
    product_name = st.sidebar.text_input(f'Product {i+1} Name', f'Product {i+1}')
    product_units = st.sidebar.number_input(f'Units Sold for {product_name}', min_value=0, value=100)
    product_returns = st.sidebar.number_input(f'Returns for {product_name}', min_value=0, value=5)

    products.append(product_name)
    units_sold.append(product_units)
    returns.append(product_returns)

# Create DataFrame from user input
product_data = {
    'Product': products,
    'Units Sold': units_sold,
    'Returns': returns
}
df_product = pd.DataFrame(product_data)

# Based on user selection, display the corresponding plot
if selected_option == 'Bar Plot':
    st.subheader('Bar Plot')
    st.bar_chart(df_product.set_index('Product'))

elif selected_option == 'Pie Chart':
    st.subheader('Pie Chart')
    fig, ax = plt.subplots()
    ax.pie(df_product['Units Sold'], labels=df_product['Product'], autopct='%1.1f%%')
    st.pyplot(fig)



# Some statistical data representation
st.write('Here are some basic statistics:')
st.write(df_product.describe())