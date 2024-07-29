for i in range(2,21):
     with open(f"Table/Multiplication_table_of {i}.txt",'w')as f: #Table is use to for the creation of new folder
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
        