import pandas as pd

df = pd.read_csv('C:/Users/gaspa/Desktop/Anime_recomendation/Datas/action.csv')
df = df.drop(df.columns[0], axis=1)

df.insert(3, 'category2', "-")
df.insert(4, 'category3', "-")
df.insert(5, 'category4', "-")
df.insert(6, 'category5', "-")
df.insert(7, 'category6', "-")
df.insert(8, 'category7', "-")
df.insert(9, 'category8', "-")
df.insert(10, 'category9', "-")
df = df.set_index('name')

df1 = pd.read_csv('C:/Users/gaspa/Desktop/Anime_recomendation/Datas/thriller.csv')
df1 = df1.drop(df1.columns[0], axis=1)
df1.insert(3, 'category2', "-")
df1.insert(4, 'category3', "-")
df1.insert(5, 'category4', "-")
df1.insert(6, 'category5', "-")
df1.insert(7, 'category6', "-")
df1.insert(8, 'category7', "-")
df1.insert(9, 'category8', "-")
df1.insert(10, 'category9', "-")

num = 0
num1 = len(df1)
for i in range(0, num1):
    objeto = df1.loc[num]
    num+=1
    if objeto[0] not in df.index:
        serie = pd.Series({  "category":objeto[1],
                             "chapters":objeto[2],
                             "category2":objeto[3],
                             "category3":objeto[4],
                             "category4":objeto[5],
                             "category5":objeto[6],
                             "category6":objeto[7],
                             "category7":objeto[8],
                             "category8":objeto[9],
                             "category9":objeto[10],
                             "watch":objeto[11]}, name=objeto[0])
        df = df.append(serie)
        #category 2
    elif df.loc[objeto[0]][2] == '-':
        df['category2'][objeto[0]] = objeto[1]    
    #Category 3
    elif df.loc[objeto[0]][3] == '-':
        df['category3'][objeto[0]] = objeto[1]
    #category 4
    elif df.loc[objeto[0]][4] == '-':
        df['category4'][objeto[0]] = objeto[1]
    #category 5
    elif df.loc[objeto[0]][5] == '-':
        df['category5'][objeto[0]] = objeto[1]        
    #category 6
    elif df.loc[objeto[0]][6] == '-':
        df['category6'][objeto[0]] = objeto[1]        
    #category 7
    elif df.loc[objeto[0]][7] == '-':
        df['category7'][objeto[0]] = objeto[1]        
    #category 8
    elif df.loc[objeto[0]][8] == '-':
        df['category8'][objeto[0]] = objeto[1]        
    #category 9
    elif df.loc[objeto[0]][9] == '-':
        df['category9'][objeto[0]] = objeto[1]            

df.to_csv('C:/Users/gaspa/Desktop/Anime_recomendation/all_animes.csv')