import re
import math
#console app to print required outputs,outputs can also be verified through unit_tests
class sales_tax:
    
    def __init__(self):
        #exemption list is assumed as exact elements are not given
        self.exempted_goods={"books":1,"chocolates":1,"bars":1,"pills":1}
    
    def get_input_type(self,input_list):
        exempted_list=[]
        #As input can be max 5 to 10 words so O(inputside*words) can be controlled
        for input in input_list:
            for word in input.split():
                #dictionary search to keep search operation O(1)
                if(word.lower() in self.exempted_goods or word.lower()+"s" in self.exempted_goods):
                    #index matching to find if input is exempted from basic sales_tax
                    exempted_list.append(1)
                    break
            #else statement only runs when break doesn't execute for whole loop
            else:
                exempted_list.append(0)
        return exempted_list
    def get_output_string(self,sales_tax_percentage,input_string):
        try:
            input_price=float(re.findall("[0-9]*\.[0-9]*",input_string)[0])
            #exception handling if wrong input given
            if(input_price==None):
                return []

            # ceil rounding used as given in outputs   
            sales_tax="{0:.2f}".format(round(math.ceil(input_price*sales_tax_percentage/(0.05*100)))*0.05)
            final_price=float(sales_tax)+input_price
            output_string=[re.sub("\sat\s[0-9]*\.[0-9]*",": "+"{0:.2f}".format(final_price),input_string),sales_tax,final_price]
            return output_string
        except:
            return []



    def sales_tax_calculator(self,input_list):
        #exception exception handling with try catch
        try:
            sales_tax=0
            total=0
            #returnlist output for unittests
            return_list=[]
            input_type_list=self.get_input_type(input_list)
        
            for count in range(len(input_list)):
        
                sales_tax_percentage=0
                is_imported=re.search("imported", input_list[count])
                if(is_imported!=None):
                    sales_tax_percentage+=5
                if(input_type_list[count]==0):
                    sales_tax_percentage+=10
                output_list=self.get_output_string(sales_tax_percentage,input_list[count])
                #exception handling
                if(len(output_list)==0):
                    print("invalid Input")
                    break

                sales_tax+=float(output_list[1])
                total+=float(output_list[2])
                print(output_list[0])
                return_list.append(output_list[0])
            print("Sales Taxes: "+"{0:.2f}".format(sales_tax))
            return_list.append("Sales Taxes: "+"{0:.2f}".format(sales_tax))
            print("Total: "+"{0:.2f}".format(total))
            return_list.append("Total: "+"{0:.2f}".format(total))
            #returns to unittests
            return return_list
        except :
            print("Some Problem Occurred,Enter Input Again in required format")
            
        
sales_object=sales_tax();
#inputs for console outputs
#input1=sales_object.sales_tax_calculator(["1 book at 12.49","1 music CD at 14.99","1 chocolate bar at 0.85"])
#input2=sales_object.sales_tax_calculator(["1 imported box of chocolates at 10.00","1 imported bottle of perfume at 47.50"])
#input1=sales_object.sales_tax_calculator(["1 imported bottle of perfume at 27.99","1 bottle of perfume at 18.99","1 packet of headache pills at 9.75","1 box of imported chocolates at 11.25"])





