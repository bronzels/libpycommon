# -*- coding: utf-8 -*-
import plotly as py
import os
import plotly.graph_objs as go
import plotly.figure_factory as ff
from bs4 import BeautifulSoup,Tag
import pandas as pd
import numpy as np
from sklearn.metrics import precision_recall_fscore_support,get_scorer,confusion_matrix
class Classification_metrics():
    def __init__(self,y_true,y_pred):
        self.y_true=[int(_) for _ in y_true]
        self.y_pred=[int(_) for _ in y_pred]
        self.maxflag=max(self.y_true+self.y_pred)+1

    def get_prfs_score(self):
        prfs = precision_recall_fscore_support(self.y_true,self.y_pred)
        result = {}
        for i, _ in enumerate(zip(*prfs)):
            result[i] = _
        df=pd.DataFrame(result)
        df.index='precision_recall_fscore_support'.split('_')
        return df
    def get_confusion_matrix(self):
        return confusion_matrix(self.y_true,self.y_pred)
    def draw_html_bar(self,file,flag_names=None,title='标题',start=0.0,end=1.0):
        prfs_df=self.get_prfs_score()
        if flag_names:
            assert len(flag_names)==self.maxflag
        else:
            flag_names=list(range(prfs_df.shape[1]))
        trace = [go.Bar(
            x=flag_names,
            y=[prfs_df[i][key] for i in range(self.maxflag)],
            name=key,
            text=[round(prfs_df[i][key],3) for i in range(self.maxflag)],textposition="auto")
                for _,key in zip(range(3),prfs_df.index.tolist()[:3])]
        layout = go.Layout(
            title=title,
            yaxis=dict(
                range=[start, end]
            ))
        fig= go.Figure(data=trace, layout=layout)
        self.dump_file(file,fig)


    def draw_html_matrix(self,file,flag_names=None,title='标题',only_errors=True,mask_tuples=None):
        conf_mat=self.get_confusion_matrix()
        if only_errors:
            for i in range(len(conf_mat)):
                conf_mat[i][i]=0
        if mask_tuples:
            for r,c in mask_tuples:
                conf_mat[r][c] = 0

        if not flag_names:
            flag_names=list(range(len(conf_mat)))
        fig = ff.create_annotated_heatmap(conf_mat,
                                          x=flag_names,
                                          y=flag_names,
                                         colorscale='geyser')

        fig = fig.update_layout(title=title)

        self.dump_file(file, fig)
    @classmethod
    def dump_file(cls,file,fig):
        if os.path.exists(file):
            soup = BeautifulSoup(open(file, encoding='utf8'),'html.parser')
            soup.append(BeautifulSoup(fig.to_html(),'html.parser').div)
        else:
            soup=BeautifulSoup(fig.to_html(),'html.parser')

        with open(file, 'w', encoding='utf8') as f:
            f.write(soup.prettify())

if __name__ == '__main__':
    cm=Classification_metrics(np.random.randint(0, 10, 1000),np.random.randint(0, 10, 1000))
    cm.draw_html_bar('report.html')
    cm.draw_html_matrix('report.html')
    cm.draw_html_matrix('report.html',mask_tuples=[(1,1)],only_errors=True)