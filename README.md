# 📊 Global Superstore Sales & Profitability Dashboard

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-v1.28+-red.svg)
![Plotly](https://img.shields.io/badge/plotly-v5.15+-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A comprehensive, interactive business intelligence dashboard built with Streamlit for analyzing Global Superstore sales data. This dashboard provides real-time insights into sales performance, profitability trends, and customer behavior patterns.

![DASHBOARD PREVIEW](Screenshot%202025-08-02%20184803.png)
![DASHBOARD PREVIEW](Screenshot%202025-08-02%20184803.png)


## 🌟 Features

### 📈 Interactive Analytics
- **Real-time Filtering**: Dynamic filters for date range, region, customer segment, product category, and shipping mode
- **Live KPI Updates**: Key performance indicators that update instantly based on selected filters
- **Multi-dimensional Analysis**: Comprehensive views across time, geography, products, and customers

### 🎯 Key Performance Indicators (KPIs)
- 💰 **Total Sales**: Real-time sales revenue tracking
- 💵 **Total Profit**: Profit analysis with margin calculations
- 👥 **Customer Metrics**: Total customers and order analytics
- 🛒 **Order Analytics**: Average order value and profit per order

### 📊 Advanced Visualizations
- **Time Series Analysis**: Monthly sales trends with interactive charts
- **Geographic Performance**: Regional sales and profit distribution
- **Customer Segmentation**: Pie charts showing segment-wise revenue
- **Product Analysis**: Category performance and profitability
- **Correlation Analysis**: Sales vs profit relationship with scatter plots
- **Top Performer Rankings**: Dynamic leaderboards for products, customers, and managers

## 📈 Dashboard Preview

### Main Dashboard Interface
```
📊 Sales & Profitability Dashboard
┌─────────────────────────────────────────────────────────────┐
│ 🎛️ Filters: Date Range | Region | Segment | Category | Ship │
├─────────────────────────────────────────────────────────────┤
│ 💰 Total Sales    💵 Total Profit    👥 Customers    🛒 AOV │
├─────────────────────────────────────────────────────────────┤
│ 📈 Monthly Trends              🌍 Regional Performance      │
├─────────────────────────────────────────────────────────────┤
│ 👥 Customer Segments           📦 Product Categories        │
├─────────────────────────────────────────────────────────────┤
│ 💸 Discount Analysis           📊 Sales vs Profit           │
└─────────────────────────────────────────────────────────────┘
```

## 🗃️ Dataset Information

### 📋 Dataset Overview
- **Records**: 51,295 transactions
- **Time Period**: Multi-year sales data
- **Geographic Coverage**: Global markets across multiple regions
- **Product Range**: 3 main categories with multiple sub-categories

### 🔗 Column Structure
| Column | Data Type | Description |
|--------|-----------|-------------|
| Row ID | int64 | Unique row identifier |
| Order ID | object | Unique order identifier |
| Order Date | datetime64[ns] | Date when order was placed |
| Ship Date | datetime64[ns] | Date when order was shipped |
| Ship Mode | object | Shipping method used |
| Customer ID | object | Unique customer identifier |
| Customer Name | object | Customer full name |
| Segment | object | Customer segment (Consumer, Corporate, Home Office) |
| City | object | Customer city |
| State | object | Customer state/province |
| Country | object | Customer country |
| Region | object | Geographic region |
| Product ID | object | Unique product identifier |
| Category | object | Product category |
| Sub-Category | object | Product sub-category |
| Product Name | object | Full product name |
| Sales | float64 | Sale amount in USD |
| Quantity | int64 | Quantity of items sold |
| Discount | float64 | Discount percentage applied |
| Profit | float64 | Profit amount in USD |
| Shipping Cost | float64 | Cost of shipping |
| Order Priority | object | Priority level of order |
| Market | object | Market segment |
| Person | object | Sales manager/representative |
| Order Month | period[M] | Month of order (derived) |

## 📊 Key Business Insights

### 💰 Financial Performance
- **Revenue Analysis**: Track total sales performance across different dimensions
- **Profitability Metrics**: Monitor profit margins and identify high-performing segments
- **Cost Management**: Analyze shipping costs and discount impacts on profitability

### 🎯 Customer Intelligence
- **Segmentation Analysis**: Understanding consumer, corporate, and home office behaviors
- **Geographic Trends**: Regional performance patterns and market opportunities
- **Customer Lifetime Value**: Track repeat customers and order frequency

### 📦 Product Performance
- **Category Analysis**: Identify top-performing product categories
- **Sub-category Insights**: Detailed product line performance
- **Inventory Optimization**: Product-wise sales and profit analysis

### 🚚 Operational Metrics
- **Shipping Efficiency**: Delivery time analysis and cost optimization
- **Order Priority Impact**: Performance across different priority levels
- **Sales Team Performance**: Manager-wise sales tracking

## 🚀 Installation & Setup

### Prerequisites
```bash
Python 3.8+
pip (Python package manager)
```

### 📦 Required Libraries
```bash
pip install streamlit>=1.28.0
pip install pandas>=1.5.0
pip install plotly>=5.15.0
pip install numpy>=1.21.0
```

### 🔧 Quick Start

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/global-superstore-dashboard.git
cd global-superstore-dashboard
```

2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

3. **Update Data Path**
   - Edit the `file_path` variable in `dashboard.py`
   - Point it to your CSV file location:
```python
file_path = r"your/path/to/cleanded_global_superstore.csv"
```

4. **Run the Dashboard**
```bash
streamlit run dashboard.py
```

5. **Access the Dashboard**
   - Open your browser to `http://localhost:8501`

## 📊 Dashboard Sections

### 🎛️ Filter Panel
- **📅 Date Range Selector**: Filter data by specific time periods
- **🌍 Region Filter**: Focus on specific geographic regions
- **👥 Segment Filter**: Analyze specific customer segments
- **📦 Category Filter**: Filter by product categories
- **🚚 Ship Mode Filter**: Analyze by shipping methods

### 📈 KPI Dashboard
```
┌─────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ 💰 Total Sales  │ 💵 Total Profit │ 👥 Customers    │ 🛒 Avg Order   │
│ $2,297,201      │ $286,397        │ 793             │ $229            │
│ 10,027 orders   │ 12.5% margin    │ 5,009 orders    │ $29 profit/ord  │
└─────────────────┴─────────────────┴─────────────────┴─────────────────┘
```

### 📊 Visualization Grid

#### Row 1: Time & Geography
- **📈 Monthly Sales Trend**: Interactive line chart showing sales patterns over time
- **🌍 Sales by Region**: Color-coded bar chart displaying regional performance

#### Row 2: Segments & Categories  
- **👥 Customer Segments**: Pie chart showing revenue distribution across segments
- **📦 Product Categories**: Horizontal bar chart of category performance

#### Row 3: Advanced Analytics
- **💸 Discount vs Profit**: Analysis of discount impact on profitability
- **📊 Sales vs Profit Correlation**: Scatter plot revealing relationship patterns

### 🏆 Top Performers Section
- **🥇 Top Products**: Most profitable products ranking
- **👑 Top Customers**: Highest value customers by sales
- **🌟 Top Sub-Categories**: Best performing product sub-categories
- **👨‍💼 Top Sales Managers**: Sales team performance leaderboard

## 🔍 Usage Examples

### Basic Filtering
```python
# Filter by date range
date_range = st.sidebar.date_input("Select Date Range", value=(min_date, max_date))

# Filter by region
selected_region = st.sidebar.selectbox("Select Region", regions)

# Apply filters to dataframe
filtered_df = df[(df['Order Date'].dt.date >= start_date) & 
                 (df['Order Date'].dt.date <= end_date)]
```

### KPI Calculation
```python
# Calculate key metrics
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
```

### Creating Interactive Charts
```python
# Monthly sales trend
fig = go.Figure()
fig.add_trace(go.Scatter(x=monthly_sales['Order Month'], 
                        y=monthly_sales['Sales'],
                        mode='lines+markers'))
st.plotly_chart(fig, use_container_width=True)
```

## 🎨 Customization Options

### Color Themes
- **Primary Colors**: Blue gradient theme for professional appearance
- **Accent Colors**: Viridis and RdYlBu color scales for data visualization
- **Custom CSS**: Gradient backgrounds and modern styling

### Layout Modifications
```python
# Modify column layouts
col1, col2, col3, col4 = st.columns([2, 2, 1, 1])

# Add custom styling
st.markdown("""
<style>
.metric-card {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 1rem;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
```

## 📊 Performance Optimization

### Data Handling
- **Smart Sampling**: Automatic sampling for large datasets in scatter plots
- **Efficient Filtering**: Optimized data filtering operations
- **Caching**: `@st.cache_data` decorator for improved performance

### Memory Management
```python
# Sample large datasets for performance
sample_size = min(1000, len(filtered_df))
sampled_data = filtered_df.sample(n=sample_size)
```

## 🔧 Troubleshooting

### Common Issues

1. **File Path Error**
   ```
   Error: File not found
   Solution: Update the file_path variable with correct CSV location
   ```

2. **Module Import Error**
   ```
   Error: No module named 'plotly'
   Solution: pip install plotly
   ```

3. **Date Parsing Issues**
   ```
   Error: Unable to parse dates
   Solution: Ensure date columns are in proper format (YYYY-MM-DD)
   ```

### Performance Issues
- For datasets larger than 100k rows, consider data sampling
- Use `st.cache_data` for expensive computations
- Limit concurrent filters for better responsiveness

## 📋 Requirements.txt
```
streamlit>=1.28.0
pandas>=1.5.0
plotly>=5.15.0
numpy>=1.21.0
datetime
warnings
```

## 🤝 Contributing

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test with different data sizes
- Ensure responsive design

## 📜 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- **Streamlit Team** for the amazing framework
- **Plotly** for interactive visualization capabilities
- **Pandas Community** for data manipulation tools
- **Global Superstore Dataset** for providing comprehensive business data

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/global-superstore-dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/global-superstore-dashboard/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/global-superstore-dashboard/wiki)

## 🚀 Future Enhancements

- [ ] **Machine Learning Integration**: Predictive analytics for sales forecasting
- [ ] **Real-time Data Connection**: Live database connectivity
- [ ] **Export Capabilities**: PDF and Excel report generation
- [ ] **Advanced Filters**: Custom date ranges and multi-select options
- [ ] **Mobile Optimization**: Enhanced mobile responsive design
- [ ] **User Authentication**: Role-based access control
- [ ] **Automated Reporting**: Scheduled report generation and email delivery

---

**⭐ If you found this project helpful, please give it a star on GitHub!**

**📧 Contact**: [junaidkhan99e9@gmail.com](mailto:your.email@example.com)

**🔗 Live Demo**: [https://youtu.be/qZ61me0GBZ8](https://your-demo-link.streamlit.app)
