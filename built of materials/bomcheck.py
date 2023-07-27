import pandas as pd


def bomcheck():
    #, open('C:\\Users\\htet.ma\\Documents\\Production\\TJF-Q170V\\BOM\\TJF-Q170V BOM.xlsx') as ft:
    pd.options.display.max_rows=99999
    df = pd.read_csv('C:\\Users\\htet.ma\\Desktop\\htet.csv')
    SeeCode = df.label_code.str.extract('(\d+)[a-zA-Z]\d+')
    dp = pd.read_excel('C:\\Users\\htet.ma\\OneDrive - Olympus\\Documents\\Production\\TJF-Q170V\\BOM\\TJF-Q170V BOM.xlsx',sheet_name="S-BOM")
    MatCode = dp.columns.str.extract('(\d+)[a-zA-Z]\d+')


    df.loc[:, 'htet_work'] = False

    for index, row in SeeCode.iterrows():
        itemcode = row.iloc[0]
        is_same_code = MatCode.loc[:,0] == itemcode
        is_same_part = df.loc[index].iloc[2] == dp.iloc[:,1]
        #print(is_same_code, is_same_code.shape, df.columns, dp.columns.shape)
        # print(dp.loc[dp.index[is_same_part], dp.columns[is_same_code]].shape)
        dp.loc[dp.index[is_same_part], dp.columns[is_same_code]] = 1
        #print(type(is_same_code))
        if is_same_code.any() and (not is_same_part.any()):
            df.loc[index, 'htet_work'] = True

    #print(dp)
    dp.to_csv('C:\\Users\\htet.ma\\OneDrive - Olympus\\Documents\\Production\\TJF-Q170V\\BOM\\TJF-Q170V BOM.csv')
    df.to_csv('C:\\Users\\htet.ma\\OneDrive - Olympus\\Documents\\Production\\TJF-Q170V\\BOM\\work.csv')

def main():
    bomcheck()


if __name__ == '__main__':
    main()
