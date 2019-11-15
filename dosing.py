import pandas
import plotly.graph_objects as go
import sys

def pie_chart():
    # pie chart
    df_registry = pandas.read_csv('t2_registry 20190619.csv')
    df_registry = df_registry[df_registry['SVPERF'].isin(['Y'])]
    df_registry = df_registry[df_registry['VISCODE'].map(lambda x: 'bl' not in x)]
    count = {}
    for value in df_registry['VISCODE']:
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    labels = []
    values = []
    for value in count:
        labels.append(value)
        values.append(count[value])
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hovertemplate='Viscode: <b>%{label}</b><br>Count: <b>%{value} (%{percent})</b>')])
    fig.show()

def csv():
    df_registry = pandas.read_csv('t2_registry 20190619.csv')
    df_ec = pandas.read_csv('t2_ec 20190619.csv')
    merged = df_ec.merge(df_registry, how='left', on=['RID', 'VISCODE'])
    viscode_filter = sys.argv[1]
    svdose_filter = sys.argv[2]
    ecs_filter_out = sys.argv[3]
    merged = merged[merged['VISCODE'] == viscode_filter]
    merged = merged[merged['SVDOSE'] == svdose_filter]
    merged = merged[merged['ECSDSTXT'] != ecs_filter_out]
    merged.to_csv(path_or_buf='results.csv', index=False, columns=['ID_x', 'RID', 'USERID_x', 'VISCODE', 'SVDOSE', 'ECSDSTXT'], header=['ID', 'RID', 'USERID', 'VISCODE', 'SVDOSE', 'ECSDSTXT'])

if __name__ == '__main__':
    pie_chart()
    csv()
