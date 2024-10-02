import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
def load_data():
    data_day = pd.read_csv("..\\data\\day.csv")
    data_hour = pd.read_csv("..\\data\\hour.csv")
    return data_day, data_hour

# Plot Boxplot: Penyewaan Berdasarkan Musim
def plot_season(data_day):
    plt.figure(figsize=(9, 5))
    sns.boxplot(x='season', y='cnt', data=data_day, color="Cyan")
    plt.title('Distribusi Jumlah Penyewaan Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Jumlah Penyewaan Sepeda')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Dingin', 'Semi', 'Panas', 'Gugur'])
    st.pyplot(plt)

# Plot Line: Tren Penyewaan Sepeda per Jam Selama satu Hari
def plot_hourly_trend(data_hour):
    plt.figure(figsize=(9, 5))
    sns.lineplot(x='hr', y='cnt', data=data_hour, estimator='mean', marker='o', color='green')
    plt.title('Tren Penyewaan Sepeda per Jam')
    plt.xlabel('Jam Selama satu Hari')
    plt.ylabel('Total Penyewaan')
    st.pyplot(plt)

# Plot pie chart: Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan
def plot_piechart(data_day):
    workingday_data = data_day.groupby('workingday')['cnt'].mean()
    labels = ['Akhir Pekan', 'Hari Kerja']

    plt.figure(figsize=(7, 7))
    plt.pie(workingday_data, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff3300','#00BDF2'])
    plt.title('Persentase Penyewaan Sepeda Antara Hari Kerja dan Akhir Pekan')
    plt.axis('equal')
    st.pyplot(plt)


# Main function to run the dashboard
def main():
    st.title('Dashboard Penyewaan Sepeda')
    
    # Load the data
    data_day, data_hour = load_data()
    
    # Sidebar options for the user
    st.sidebar.header('Pilih Visualisasi Data')
    plot_option = st.sidebar.selectbox(
        'Choose a plot',
        ['Penyewaan Berdasarkan Musim', 'Akhir Pekan vs Hari Kerja', 'Tren Penyewaan Selama Sehari']
    )

    # Display the selected plot
    if plot_option == 'Penyewaan Berdasarkan Musim':
        plot_season(data_day)
    elif plot_option == 'Akhir Pekan vs Hari Kerja':
        plot_piechart(data_day)
    elif plot_option == 'Tren Penyewaan Selama Sehari':
        plot_hourly_trend(data_hour)

if __name__ == '__main__':
    main()
