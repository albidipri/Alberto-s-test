Hi Github community,
I am still pretty new to it and as my first project at Hyper Isalnd I wanted to create a program that shows if I go to the Casino and play Roulette with infinite money and I apply the martingale system will I be able to win and quit my studies?
The answer is NO unfortunately, at the end the Casino will win.
If you use my code you can choose how much money you have available for 365 days and in each day you play/spin 50 times and the starting bet is 1.
every time you win the bet goes back to its original value (1), if you loose you will double up it in the next spin (for example -1,-2,-4,-8,-16,-32,-64,-128...).
It is also possibile to te exports the result to a excel file.

If you are using pycham, to do so, you need to create a new Excel file where your pycharm file is created and name it "data casino" (for example)
and make sure you have the packages XlsxWriter and excel-export on your Pycharm, then on top of the coding you will need to:


import pandas as pd




At the bottom of coding you will need to add:


data = pd.DataFrame({'winnings': [winning_list]})
datatoexcel = pd.ExcelWriter("data casino.xlsx", engine='xlsxwriter')
data.to_excel(datatoexcel, sheet_name="Sheet1")
datatoexcel.save()


