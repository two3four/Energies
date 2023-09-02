import plotly.graph_objects as go

# Define the data for the Sankey diagram
data = go.Sankey(
    node=dict(
        pad=15,
        thickness=15,
        line=dict(color="black", width=0.5),
        label=[
            "Current",
            "Line 5/78",
            "Quebec Waterborne Imports",
            "Other Crude Oil Pipelines",
            "Future",
            "Line 78",
            "Quebec Waterborne Imports",
            "Other Crude Oil Pipelines",
            "Nanticoke Crude by Rail",
            "Sarnia Crude by Rail",
            "Toledo Crude by Rail",
        ],
        # Position labels outside on the right
        x=[0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1.3],  # Adjust the last value to move the labels to the right
    ),
    link=dict(
        source=[0, 0, 0, 0, 4, 4, 4, 4, 4, 4],
        target=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        value=[861, 107, 165, 570, 570, 308, 165, 20, 35, 35],
        color=[
            "rgba(31,119,180,0.7)",
            "rgba(31,119,180,0.7)",
            "rgba(31,119,180,0.7)",
            "rgba(31,119,180,0.7)",
            "rgba(255,127,14,0.7)",
            "rgba(255,127,14,0.7)",
            "rgba(255,127,14,0.7)",
            "rgba(255,127,14,0.7)",
            "rgba(44,160,44,0.7)",
            "rgba(44,160,44,0.7)",
            "rgba(44,160,44,0.7)",
        ],
    ),
)

layout = go.Layout(
    title="Current vs. Future",
    margin=dict(t=30, r=20, b=20, l=20),  # Add margins to make room for labels
)

fig = go.Figure(data=[data], layout=layout)
fig.show()
