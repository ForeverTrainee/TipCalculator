
def main():
    total_bill = int(input("What was the total bill? $"))
    percentage = float(input("What percentage tp you like to give? "))
    people_number = int(input("How many people to split the bill? "))
    result = (total_bill * (percentage*0.01)) / people_number
    result = round(result)
    print("Each person should pay: $",result)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   main()
