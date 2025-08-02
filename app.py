import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# =====================================================
# 🎨 PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Sales & Profitability Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 🎨 CUSTOM CSS STYLING
# =====================================================
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .kpi-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        text-align: center;
        color: white;
        margin: 0.5rem;
    }
    
    .kpi-value {
        font-size: 2rem;
        font-weight: bold;
        margin: 0;
    }
    
    .kpi-label {
        font-size: 0.9rem;
        margin: 0;
        opacity: 0.9;
    }
    
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1f77b4;
    }
    
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
</style>
""", unsafe_allow_html=True)

# =====================================================
# 📊 DATA LOADING FUNCTION
# =====================================================
@st.cache_data
def load_data():
    """Load and prepare the dataset"""
    try:
        # Update this path to your actual file path
        file_path = r"C:\Users\kashif-pc\Desktop\DATA ANYALSYIS PROJECT\business intelligence project\cleanded_global_superstore.csv"
        df = pd.read_csv(file_path)
        
        # Data preprocessing
        df['Order Date'] = pd.to_datetime(df['Order Date'])
        df['Ship Date'] = pd.to_datetime(df['Ship Date'])
        df['Order Month'] = df['Order Date'].dt.to_period('M').astype(str)
        df['Order Year'] = df['Order Date'].dt.year
        df['Order Quarter'] = df['Order Date'].dt.quarter
        df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

# =====================================================
# 📈 KPI CALCULATION FUNCTIONS
# =====================================================
def calculate_kpis(df):
    """Calculate key performance indicators"""
    total_sales = df['Sales'].sum()
    total_profit = df['Profit'].sum()
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    total_customers = df['Customer ID'].nunique()
    total_orders = df['Order ID'].nunique()
    avg_order_value = total_sales / total_orders if total_orders > 0 else 0
    avg_profit_per_order = total_profit / total_orders if total_orders > 0 else 0
    total_products = df['Product ID'].nunique()
    
    return {
        'total_sales': total_sales,
        'total_profit': total_profit,
        'profit_margin': profit_margin,
        'total_customers': total_customers,
        'total_orders': total_orders,
        'avg_order_value': avg_order_value,
        'avg_profit_per_order': avg_profit_per_order,
        'total_products': total_products
    }

# =====================================================
# 🎯 MAIN APPLICATION
# =====================================================
def main():
    # Header
    st.markdown('<h1 class="main-header">📊 Sales & Profitability Dashboard</h1>', unsafe_allow_html=True)
    
    # Load data
    df = load_data()
    if df is None:
        st.stop()
    
    # =====================================================
    # 🔧 SIDEBAR FILTERS
    # =====================================================
    st.sidebar.header("🎛️ Dashboard Filters")
    
    # Date range filter
    min_date = df['Order Date'].min()
    max_date = df['Order Date'].max()
    
    date_range = st.sidebar.date_input(
        "📅 Select Date Range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Region filter
    regions = ['All'] + sorted(df['Region'].unique().tolist())
    selected_region = st.sidebar.selectbox("🌍 Select Region", regions)
    
    # Segment filter
    segments = ['All'] + sorted(df['Segment'].unique().tolist())
    selected_segment = st.sidebar.selectbox("👥 Select Customer Segment", segments)
    
    # Category filter
    categories = ['All'] + sorted(df['Category'].unique().tolist())
    selected_category = st.sidebar.selectbox("📦 Select Product Category", categories)
    
    # Ship Mode filter
    ship_modes = ['All'] + sorted(df['Ship Mode'].unique().tolist())
    selected_ship_mode = st.sidebar.selectbox("🚚 Select Ship Mode", ship_modes)
    
    # =====================================================
    # 🔍 APPLY FILTERS
    # =====================================================
    filtered_df = df.copy()
    
    # Apply date filter
    if len(date_range) == 2:
        start_date, end_date = date_range
        filtered_df = filtered_df[
            (filtered_df['Order Date'].dt.date >= start_date) & 
            (filtered_df['Order Date'].dt.date <= end_date)
        ]
    
    # Apply other filters
    if selected_region != 'All':
        filtered_df = filtered_df[filtered_df['Region'] == selected_region]
    
    if selected_segment != 'All':
        filtered_df = filtered_df[filtered_df['Segment'] == selected_segment]
    
    if selected_category != 'All':
        filtered_df = filtered_df[filtered_df['Category'] == selected_category]
    
    if selected_ship_mode != 'All':
        filtered_df = filtered_df[filtered_df['Ship Mode'] == selected_ship_mode]
    
    # Check if filtered data is empty
    if filtered_df.empty:
        st.warning("⚠️ No data available for the selected filters. Please adjust your selection.")
        return
    
    # Calculate KPIs
    kpis = calculate_kpis(filtered_df)
    
    # =====================================================
    # 📊 KPI DASHBOARD
    # =====================================================
    st.subheader("📈 Key Performance Indicators")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Total Sales",
            value=f"${kpis['total_sales']:,.0f}",
            delta=f"{len(filtered_df)} orders"
        )
    
    with col2:
        st.metric(
            label="💵 Total Profit",
            value=f"${kpis['total_profit']:,.0f}",
            delta=f"{kpis['profit_margin']:.1f}% margin"
        )
    
    with col3:
        st.metric(
            label="👥 Total Customers",
            value=f"{kpis['total_customers']:,}",
            delta=f"{kpis['total_orders']} orders"
        )
    
    with col4:
        st.metric(
            label="🛒 Avg Order Value",
            value=f"${kpis['avg_order_value']:,.0f}",
            delta=f"${kpis['avg_profit_per_order']:.0f} profit/order"
        )
    
    # =====================================================
    # 📊 CHARTS AND VISUALIZATIONS
    # =====================================================
    
    # Row 1: Time series and regional analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Monthly Sales Trend")
        monthly_sales = filtered_df.groupby('Order Month').agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index()
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=monthly_sales['Order Month'],
            y=monthly_sales['Sales'],
            mode='lines+markers',
            name='Sales',
            line=dict(color='#1f77b4', width=3),
            marker=dict(size=8)
        ))
        
        fig.update_layout(
            title="Monthly Sales Performance",
            xaxis_title="Month",
            yaxis_title="Sales ($)",
            hovermode='x unified',
            template="plotly_white"
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("🌍 Sales by Region")
        region_data = filtered_df.groupby('Region').agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index()
        
        fig = px.bar(
            region_data,
            x='Region',
            y='Sales',
            color='Profit',
            title="Regional Sales Performance",
            color_continuous_scale='viridis'
        )
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    # Row 2: Category and segment analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("👥 Sales by Customer Segment")
        segment_data = filtered_df.groupby('Segment')['Sales'].sum().reset_index()
        
        fig = px.pie(
            segment_data,
            values='Sales',
            names='Segment',
            title="Customer Segment Distribution",
            color_discrete_sequence=['#ff9999','#66b3ff','#99ff99']
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📦 Top Product Categories")
        category_data = filtered_df.groupby('Category').agg({
            'Sales': 'sum',
            'Profit': 'sum'
        }).reset_index().sort_values('Sales', ascending=True)
        
        fig = px.bar(
            category_data,
            x='Sales',
            y='Category',
            orientation='h',
            title="Category Performance",
            color='Profit',
            color_continuous_scale='RdYlBu'
        )
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    # Row 3: Correlation and detailed analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💸 Discount vs Profit Analysis")
        
        # Create bins for better visualization
        filtered_df['Discount_Bin'] = pd.cut(filtered_df['Discount'], 
                                           bins=5, 
                                           labels=['0-20%', '20-40%', '40-60%', '60-80%', '80-100%'])
        
        discount_profit = filtered_df.groupby('Discount_Bin')['Profit'].mean().reset_index()
        
        fig = px.bar(
            discount_profit,
            x='Discount_Bin',
            y='Profit',
            title="Average Profit by Discount Range",
            color='Profit',
            color_continuous_scale='RdYlGn'
        )
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        st.subheader("📊 Sales vs Profit Correlation")
        
        fig = px.scatter(
            filtered_df.sample(n=min(1000, len(filtered_df))),  # Sample for performance
            x='Sales',
            y='Profit',
            color='Category',
            size='Quantity',
            title="Sales vs Profit Relationship",
            hover_data=['Customer Name', 'Product Name']
        )
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)
    
    # Row 4: Top performers
    st.subheader("🏆 Top Performers")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🥇 Top Products", "👑 Top Customers", "🌟 Top Sub-Categories", "👨‍💼 Top Managers"])
    
    with tab1:
        top_products = filtered_df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(
            x=top_products.values,
            y=top_products.index,
            orientation='h',
            title="Top 10 Most Profitable Products",
            labels={'x': 'Profit ($)', 'y': 'Product Name'}
        )
        fig.update_layout(template="plotly_white", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        top_customers = filtered_df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(
            x=top_customers.values,
            y=top_customers.index,
            orientation='h',
            title="Top 10 Customers by Sales",
            labels={'x': 'Sales ($)', 'y': 'Customer Name'}
        )
        fig.update_layout(template="plotly_white", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        top_subcategories = filtered_df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(
            x=top_subcategories.values,
            y=top_subcategories.index,
            orientation='h',
            title="Top 10 Sub-Categories by Sales",
            labels={'x': 'Sales ($)', 'y': 'Sub-Category'}
        )
        fig.update_layout(template="plotly_white", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    with tab4:
        top_managers = filtered_df.groupby('Person')['Sales'].sum().sort_values(ascending=False).head(10)
        fig = px.bar(
            x=top_managers.values,
            y=top_managers.index,
            orientation='h',
            title="Top 10 Sales Managers",
            labels={'x': 'Sales ($)', 'y': 'Manager Name'}
        )
        fig.update_layout(template="plotly_white", height=500)
        st.plotly_chart(fig, use_container_width=True)
    
    # =====================================================
    # 📋 DATA SUMMARY TABLE
    # =====================================================
    st.subheader("📋 Detailed Data Summary")
    
    if st.checkbox("Show Raw Data"):
        st.dataframe(
            filtered_df.head(1000),
            use_container_width=True
        )
    
    # Summary statistics
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Numerical Columns Summary:**")
        numeric_cols = ['Sales', 'Profit', 'Quantity', 'Discount', 'Shipping Cost']
        st.dataframe(filtered_df[numeric_cols].describe().round(2))
    
    with col2:
        st.write("**Categorical Columns Summary:**")
        categorical_summary = pd.DataFrame({
            'Column': ['Region', 'Segment', 'Category', 'Ship Mode'],
            'Unique Values': [
                filtered_df['Region'].nunique(),
                filtered_df['Segment'].nunique(),
                filtered_df['Category'].nunique(),
                filtered_df['Ship Mode'].nunique()
            ]
        })
        st.dataframe(categorical_summary)
    
    # =====================================================
    # 📊 FOOTER
    # =====================================================
    st.markdown("---")
    st.markdown(
        f"""
        <div style='text-align: center; color: #666; font-size: 0.9rem;'>
            📊 Dashboard showing data from {filtered_df['Order Date'].min().strftime('%Y-%m-%d')} 
            to {filtered_df['Order Date'].max().strftime('%Y-%m-%d')} | 
            {len(filtered_df):,} records displayed
        </div>
        """, 
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()