import seaborn as sns
import matplotlib.pyplot as plt

def plot_chart_all(dataset):
  figure, axis = plt.subplots(4, 4, figsize=(16, 16))

  sns.histplot(data=dataset, x='Age', kde=True, ax=axis[0, 0])
  sns.histplot(data=dataset, x='Age at menarche', kde=True, ax=axis[0, 1])
  sns.histplot(data=dataset, x='Age at first delivery', kde=True, ax=axis[0, 2])
  sns.histplot(data=dataset, x='Duration of disease onset', kde=True, ax=axis[0, 3])

  sns.histplot(data=dataset, x='Lesions', kde=True, ax=axis[1, 0])
  sns.histplot(data=dataset, x='Number of metastatic lymph nodes', kde=True, ax=axis[1, 1])
  sns.histplot(data=dataset, x='Family history', kde=True, ax=axis[1, 2])
  sns.histplot(data=dataset, x='Ki-67 index', kde=True, ax=axis[1, 3])

  sns.histplot(data=dataset, x='HR', kde=True, ax=axis[2, 0])
  sns.histplot(data=dataset, x='HER-2', kde=True, ax=axis[2, 1])
  sns.histplot(data=dataset, x='Tumor size cm', kde=True, ax=axis[2, 2])
  sns.histplot(data=dataset, x='Tumor staging', kde=True, ax=axis[2, 3])


  sns.histplot(data=dataset, x='Histological grade', kde=True, ax=axis[3, 0])
  sns.histplot(data=dataset, x='DFS/month', kde=True, ax=axis[3, 1])
  sns.histplot(data=dataset, x='DFS', kde=True, ax=axis[3, 2])
  sns.histplot(data=dataset, x='OS/month', kde=True, ax=axis[3, 3])

  figure.suptitle('Data Distribution')

def plot_chart_numerical(dataset):
  figure, axis = plt.subplots(4, 4, figsize=(16, 16))

  sns.boxplot(data=dataset, x='Age', ax=axis[0, 0])
  sns.boxplot(data=dataset, x='Age at menarche', ax=axis[0, 1])
  sns.boxplot(data=dataset, x='Age at first delivery', ax=axis[0, 2])
  sns.boxplot(data=dataset, x='Duration of disease onset', ax=axis[0, 3])

  sns.boxplot(data=dataset, x='Lesions', ax=axis[1, 0])
  sns.boxplot(data=dataset, x='Number of metastatic lymph nodes', ax=axis[1, 1])
  sns.boxplot(data=dataset, x='Family history', ax=axis[1, 2])
  sns.boxplot(data=dataset, x='Ki-67 index', ax=axis[1, 3])

  sns.boxplot(data=dataset, x='HR', ax=axis[2, 0])
  sns.boxplot(data=dataset, x='HER-2', ax=axis[2, 1])
  sns.boxplot(data=dataset, x='Tumor size cm', ax=axis[2, 2])
  sns.boxplot(data=dataset, x='Tumor staging', ax=axis[2, 3])

  sns.boxplot(data=dataset, x='Histological grade', ax=axis[3, 0])
  sns.boxplot(data=dataset, x='DFS/month', ax=axis[3, 1])
  sns.boxplot(data=dataset, x='DFS', ax=axis[3, 2])
  sns.boxplot(data=dataset, x='OS/month', ax=axis[3, 3])

  figure.suptitle('Data Distribution (Box Plot)')
