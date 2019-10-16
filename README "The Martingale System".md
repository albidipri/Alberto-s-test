Hi Github community,
Does the Martingale system actually works?
With this code you can choose how much money you have available, you will spin the roulette 50 times for 365 day with the starting bet is 1.
Every time you win the bet goes back to its original value (1), if you loose you will double up it in the next spin (for example -1,-2,-4,-8,-16,-32,-64,-128...).

It is also possibile to te exports the result to a excel file.

If you are using pycham, to do so, you need to create a new Excel file where your pycharm file is created and name it "data casino" (for example)
and make sure you have the packages XlsxWriter and excel-export on your Pycharm, then on top of the coding you will need to:


import pandas as pd






At the bottom of coding you will need to add:


data = pd.DataFrame({'winnings': [winning_list]})

datatoexcel = pd.ExcelWriter("data casino.xlsx", engine='xlsxwriter')

data.to_excel(datatoexcel, sheet_name="Sheet1")

datatoexcel.save()


