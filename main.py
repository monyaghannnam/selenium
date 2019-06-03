from Parser import Parser
from Operation import Operation

def main():
    
    """
    try: 
        parser = Parser()
        args = parser.get_args()
        if args.csv is None:
            print "Please fill missing argument, check --help for additional information "
            
    except:
        print "expected one argument, check --help for additional information "
    """
    
    op = Operation("input.csv")################ args.csv
    csv_reader = op.read_csv()
    
    op.extract_web_data(csv_reader)
        
    
    
    

if __name__=="__main__":
    main()
