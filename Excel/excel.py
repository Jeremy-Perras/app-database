import xlwings as xw
import pandas as pd


if __name__ == "__main__":
    xw.Book("/Users/jeremyperras/Desktop/csv/Excel/excel.xlsm").set_mock_caller()
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    for i in range(1, 33):
        name = "0000000" + str(i)
        if (len(name) > 8):
            name = name.replace('0', '', 1)
        data = pd.read_csv(
            f"/Users/jeremyperras/Desktop/csv/database/{name}.csv")
        wb.sheets.add(name=name)
        xw.view(data, sheet=xw.sheets.active)
