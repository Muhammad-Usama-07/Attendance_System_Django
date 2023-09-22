from django.shortcuts import render
import plotly.express as px

def dashboard(request):
    # Data for the bar chart
    data = {'Category': ['A', 'B', 'C', 'D'],
            'Value': [10, 20, 15, 25]}

    # Create a Plotly figure
    fig = px.bar(data, x='Category', y='Value', title='Sample Bar Chart')

    # Convert the figure to HTML
    plot_div = fig.to_html(full_html=False)
    return render(request, 'dashboard.html', context={'plot_div': plot_div})

def courses(request):
    return render(request, 'courses.html')

def notes(request):
    return render(request, 'notes.html')

def performance(request):
    return render(request, 'performance.html')
