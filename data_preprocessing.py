import pandas as pd

df=pd.read_csv('StudentPerformanceFactors.csv')
print(df.columns)
print(df.isnull().sum())



def performance_band(score):
    if score >= 85:
        return 'Distinction'
    elif score >= 70:
        return 'Merit'
    elif score >= 50:
        return 'Pass'
    else:
        return 'Fail'

def preprocess_data(df):
    df.columns = df.columns.str.lower()

    # Handle missing values
    df['teacher_quality'] = df['teacher_quality'].fillna('Unknown')
    df['parental_education_level'] = df['parental_education_level'].fillna('Unknown')
    df['distance_from_home'] = df['distance_from_home'].fillna('Unknown')

    #feature engineering
    df['pass'] = df['exam_score'].apply(lambda x: 1 if x >= 50 else 0)
    df['performance_band'] = df['exam_score'].apply(performance_band)

    return df

df = preprocess_data(df)
df.to_csv('cleaned_student_performance.csv', index=False)

