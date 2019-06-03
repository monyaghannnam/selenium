import csv
import re
from selenium import webdriver

class Operation:
    
    def __init__(self,name_csv):
        self.name_csv= name_csv
        
    def read_csv(self):
        """Reading CSV Files Into a Dictionary With csv
        :Return read_csv => list of dictionariess 
        """
        csv_file = open(self.name_csv,'r')
        csv_reader = csv.DictReader(csv_file)
        return csv_reader
    
    def extract_web_data(self,csv_reader) :
        path = "chromedriver"
        driver = webdriver.Chrome(path)
        url = "https://www.bing.com/"
        i=1
        for row in csv_reader:
            driver.get(url)
            data = row['name']+" "+row['city']+" expedia"
            self.set_search_data(driver,data)
            self.get_result(driver,data,i)
            if i==6:
                break
            i+=1
           
           
        
    def set_search_data(self,driver,data):
        search_box = driver.find_element_by_xpath("//*[@id='sb_form_q']")
        search_box.send_keys(data)
        search_box.submit()
        search_icon =  driver.find_element_by_xpath("//*[@id='sb_form_go']").click()
        
    def get_result(self,driver,data,row):
        ls=[]
        flag = 0
        
        for element in driver.find_elements_by_class_name('b_algo'):
            dic={}
            all_children_by_xpath = element.find_elements_by_xpath(".//*")
    
            for child in all_children_by_xpath:
                if child.get_attribute("href") is not None:
                    if self.validate_link(child.get_attribute("href")):
                        dic['name']=child.text
                        dic['link']=child.get_attribute("href")
                        flag = 1
            if flag==1:
                for line in (element.text.splitlines( )) :
                    if line.startswith('Location: '):
                        dic['location']=line[10:]
                flag=0
                
            if len(dic)!=0:
                ls.append(dic)
       
        self.write_csv(ls,row)
            
          
    def validate_link(self,line):
        r = re.compile("^https://www.expedia.com/.*Hotel-Information$")
        if r.search(line):
            return True
        else:
            return False
        
    def write_csv(self,ls,row_num):
        i=1
        if len(ls)==0:
            with open('input.csv','r') as csvinput:
                
                with open('output.csv', 'w') as csvoutput:
                    writer = csv.writer(csvoutput, lineterminator='\n')
                    reader = csv.reader(csvinput)
                
                    all = []
                    row = next(reader)
                    if not self.check_exist(str(row),'found hotel name '+str(i)):
                        row.append('found hotel name '+str(i))
                        row.append('found hotel address '+str(i))
                        row.append('found hotel link '+str(i))
                        
                   
                    all.append(row)
                        
                    j = 1
                    for row in reader:
                        if row_num ==j:
                            row.append('hotel not found')
                            row.append('')
                            row.append('')
                          
                        j+=1    
                        all.append(row)
                            
                
                    writer.writerows(all)
                    i+=1
            self.copy_csv('output.csv','input.csv')
            
        for dic in ls:
            
            with open('input.csv','r') as csvinput:
                
                
                with open('output.csv', 'w') as csvoutput:
                    writer = csv.writer(csvoutput, lineterminator='\n')
                    reader = csv.reader(csvinput)
                
                    all = []
                    row = next(reader)
                    if not self.check_exist(str(row),'found hotel name '+str(i)):
                        row.append('found hotel name '+str(i))
                        row.append('found hotel address '+str(i))
                        row.append('found hotel link '+str(i))
                        
                   
                    all.append(row)
                        
                    j = 1
                    for row in reader:
                        if row_num ==j:
                            row.append(dic.get('name',0))
                            row.append(dic.get('location',0))
                            row.append(dic.get('link',0))
                          
                        j+=1    
                        all.append(row)
                            
                
                    writer.writerows(all)
                    i+=1
            self.copy_csv('output.csv','input.csv')
       
        
      
                    
    def copy_csv(self,in_file,out_file):
        
        with open(in_file,'r') as csvinput:
                
                with open(out_file, 'w') as csvoutput:
                    writer = csv.writer(csvoutput, lineterminator='\n')
                    reader = csv.reader(csvinput)
                
                    all = []
                    row = next(reader)
                    all.append(row)
                   
                    for row in reader:
                        all.append(row)
                            
                    writer.writerows(all)
                    
  
        
    def check_exist(self,line,exp):
        r = re.compile(exp)
        if r.search(line):
            
            return True
        else:
            return False
            
        
         
        
                
               
        
                        
    
        
        
           

            
            
        
        
        
    
    