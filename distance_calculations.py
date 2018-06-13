import seaborn as sns



merged_df['trip_distance'] = merged_df.apply(distance, axis=1)

merged_df.head()
distance_df = merged_df[['month','trip_distance','start_time','end_time']]

distance_df = distance_df.groupby('month').sum()
sns.barplot(distance_df.index, distance_df['trip_distance'])
plt.title('Number of Miles Per Month (2017)')
plt.ylabel('Distance in Miles')
plt.tight_layout()
plt.savefig('outputs/MilesPerMonth.png')


total_diastance = merged_df['trip_distance'].sum()
total_diastance


def distance(row):
    one = (row["latitude_x"],row["longitude_x"])
    two = (row["latitude_y"], row["longitude_y"])
    return great_circle(one, two).miles

merged_df['trip_distance'] = merged_df.apply(distance, axis=1)