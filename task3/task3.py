import json
n=str(input())
m=str(input())
with open(n,'r') as tests_file:
    tests_data=json.load(tests_file)
with open(m,'r') as values_file:
    values_data=json.load(values_file)
report_data={}
for test_name,test_info in tests_data.items():
    total_animal_numbers = [(k,v) for dct in test_info for k, v in dct.items()]
    report_data[test_name]={}
    for key,value in total_animal_numbers:
        if key=='id':
            for values_key,values_value in values_data.items():
                valuesvalue = [v for dct in values_value for k, v in dct.items()]
                for i in range(0,len(valuesvalue)):
                    if valuesvalue[i] == value:
                        k=valuesvalue[i+1]
                        report_data[test_name][value]=k
        if key == 'values':
            total_animal_numbers1 = [(k,v) for dct in value for k, v in dct.items()]
            for key1,value1 in total_animal_numbers1:
                if key1=='id':
                    for values_key,values_value in values_data.items():
                        valuesvalue1 = [v for dct in values_value for k, v in dct.items()]
                        for i in range(0,len(valuesvalue1)):
                            if valuesvalue1[i] == value1:
                                k1=valuesvalue1[i+1]
                                report_data[test_name][value1]=k1
                if key1 == 'values':
                    total_animal_numbers2 = [(k,v) for dct in value1 for k, v in dct.items()]
                    for key2,value2 in total_animal_numbers2:
                        if key2=='id':
                            for values_key,values_value in values_data.items():
                                valuesvalue2 = [v for dct in values_value for k, v in dct.items()]
                                for i in range(0,len(valuesvalue2)):
                                    if valuesvalue2[i] == value2:
                                        k2=valuesvalue2[i+1]
                                        report_data[test_name][value2]=k2
                        if key2 == 'values':
                            total_animal_numbers3 = [(k,v) for dct in value2 for k, v in dct.items()]
                            for key3,value3 in total_animal_numbers3:
                                if key3=='id':
                                    for values_key,values_value in values_data.items():
                                        valuesvalue3 = [v for dct in values_value for k, v in dct.items()]
                                        for i in range(0,len(valuesvalue3)):
                                            if valuesvalue3[i] == value3:
                                                k3=valuesvalue3[i+1]
                                                report_data[test_name][value3]=k3
                                if key3 == 'values':
                                    total_animal_numbers4 = [(k,v) for dct in value3 for k, v in dct.items()]
                                    for key4,value4 in total_animal_numbers4:
                                        if key4=='id':
                                            for values_key,values_value in values_data.items():
                                                valuesvalue4 = [v for dct in values_value for k, v in dct.items()]
                                                for i in range(0,len(valuesvalue4)):
                                                    if valuesvalue4[i] == value4:
                                                        k4=valuesvalue4[i+1]
                                                        report_data[test_name][value4]=k4
                                        if key4 == 'values':
                                            total_animal_numbers5 = [(k,v) for dct in value4 for k, v in dct.items()]
                                            for key5,value5 in total_animal_numbers5:
                                                if key5=='id':
                                                    for values_key,values_value in values_data.items():
                                                        valuesvalue5 = [v for dct in values_value for k, v in dct.items()]
                                                        for i in range(0,len(valuesvalue5)):
                                                            if valuesvalue5[i] == value5:
                                                                k5=valuesvalue5[i+1]
                                                                report_data[test_name][value5]=k5
                                                if key5 == 'values':
                                                    total_animal_numbers6 = [(k,v) for dct in value5 for k, v in dct.items()]
                                                    for key6,value6 in total_animal_numbers6:
                                                        if key6=='id':
                                                            for values_key,values_value in values_data.items():
                                                                valuesvalue6 = [v for dct in values_value for k, v in dct.items()]
                                                                for i in range(0,len(valuesvalue6)):
                                                                    if valuesvalue6[i] == value6:
                                                                        k6=valuesvalue6[i+1]
                                                                        report_data[test_name][value6]=k6           
with open('report.json','w') as report_file:
    json.dump(report_data,report_file,indent=4)
print("Файл report.json успешно сформирован")
