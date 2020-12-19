import matplotlib.pyplot as plt


def boxplot(df):
    boxplot = df.boxplot(column=['Train', 'Dental Implant', 'Diabetes' , 'Heart disease','Blood pressure','Cancer','Bone','Covid'])
    plt.show()