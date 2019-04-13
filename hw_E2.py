Pareto = np.random.pareto(4,23)
import seaborn as sns
sns.distplot(Pareto, label = 'Pareto распределение', color='green'), plt.legend(), plt.show()
