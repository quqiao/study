import xlrd

class Excel:
    def __init__(self):  
        self.workbook = None  
        self.worksheet=None
    def open_excel(self,file):
        try:
            self.workbook = xlrd.open_workbook(file)
            self.select_worksheet_by_index(0)
        except Exception,e:
            print str(e)
            
    
    def select_worksheet_by_name(self,name=u'Sheet1'):
        self.worksheet=self.workbook.sheet_by_name(name)
        
    def select_worksheet_by_index(self,index):
        self.worksheet=self.workbook.sheet_by_index(index)
        
    def get_row_values(self,index):
        if index<self.worksheet.nrows:
            return self.worksheet.row_values(index)
        else:
            return None
        
    def get_col_values(self,index):
        if index<self.worksheet.ncols:
            return self.worksheet.col_values(index)
        else:
            return None

    def get_value(self,row,col):
        try:
            return self.worksheet.row_values(row)[col]
        except Exception,e:
            print None
