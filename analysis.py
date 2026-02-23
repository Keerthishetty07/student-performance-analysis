import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

df['total'] = df[['math score','reading score','writing score']].sum(axis=1)
# Basic exploration
print(df.head())
print("\nMissing values:\n", df.isnull().sum())
print("\nDuplicates:", df.duplicated().sum())
print("\nStatistics:\n", df.describe())

#insights
print("\nTop 5 Students by Total Score:")
print(df.sort_values('total', ascending=False).head())

# Average scores
avg_scores = df[['math score', 'reading score', 'writing score']].mean()
#visualization
avg_scores.plot(kind='bar')
plt.title("Average Scores by Subject")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

print("\nSubject with lowest average score:")
print(avg_scores.idxmin())

#correlation heatmap
plt.figure(figsize=(6,4))
sns.heatmap(df[['math score','reading score','writing score']].corr(), annot=True)
plt.title("Score Correlation Heatmap")
plt.tight_layout()
plt.show()

#gender-wise performance
gender_avg = df.groupby('gender')[['math score','reading score','writing score']].mean()
gender_avg.plot(kind='bar')
plt.title("Gender-wise Performance Comparison")
plt.ylabel("Score")
plt.tight_layout()
plt.show()

#lunch impact
lunch_avg = df.groupby('lunch')[['math score','reading score','writing score']].mean()
lunch_avg.plot(kind='bar')
plt.title("Impact of Lunch Type on Scores")
plt.ylabel("Score") 
plt.tight_layout()
plt.show()

#distribution of total scores
sns.histplot(df['total'], bins=20, kde=True)
plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()