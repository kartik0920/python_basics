import os
import pandas  as pd

def load_data(data_path="data/sales.csv"):
    if not os.path.exists(data_path):
        print("path doesn't exist Create a path for it")
        return
    else:
        print(f"data Found at {data_path}")
        return pd.read_csv(data_path)


def main():
    data_path="data/sales.csv"    
    df=load_data(data_path)
    df["total"]=df["quantity"]*df["price"]
    print(df) 
    print(f"# rows:{df.shape[0]} and # columns:{df.shape[1]}")
    
    
    
    os.makedirs('output',exist_ok=True)
    output_dir="output"
    
    # json
    df.to_json(output_dir+"/sales_data.json",orient="records",indent=3)
    # csv
    df.to_csv(output_dir+"/sales_data.csv",index=False)
    print(f"Files are saved to {output_dir}")
        
    

          
if __name__== "__main__":
    main()
