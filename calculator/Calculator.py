import math
from datetime import datetime
History="recent.txt"
def options():
    print(f"\nselect your choice : \n\n"
          f"1:Calculate\n"
          f"2:History\n"
          f"3:Clear\n"
          f"4:Exit\n")
def show_history():
    file=open(History,'r')
    lines=file.readlines()
    if len(lines)==0:
        print("\n No History Is Found!!!!")
    else:
        for line in reversed(lines):
             print(line.strip())
             
def clear_history():
    file=open(History,'w')
    print("\nHistory Is Cleared 🧹")
    file.close()
    
def sav_the_history(equation,result):
    file=open(History,'a')
    file.write(f"\n {datetime.now()}--->>>>>>{equation} = {str(result) }\n")
    print("\nHistory Is Saved👍")
    
def calculate(user_input):
    parts=user_input.split()
    if len(parts)!=3:
        print("\nInvalid Format (Enter eg: 8 * 8)")
        return
    num1=float(parts[0])
    op=parts[1]
    num2=float(parts[2])
    if op=="+":
        result= num1+num2
    elif op=="-":
        result= num1-num2
    elif op=="*":
        result= num1*num2
    elif op=="/":
        if num2!=0:
           result=num1/num2
        else:
            print("Error:Division by Zero🤔")
            return
    elif op=="%":
        result=num1%num2
    elif op == "**":
        result = num1 ** num2
    elif op == "//":
        result = num1 // num2
    elif op == "sqrt":
        result = math.sqrt(num1)
    else:
        print("\nInvalid Operator!!!!!!!!!")
        return
    if int(result)==result:
        result=int(result)
    print(f"result : {result}")
    sav_the_history(user_input,result)
    
    
def main():
    print("------------🧮simple calculator🧮----------------".upper())
    while True:
        options()
        option=input("\nenter the option : ").lower().strip()
        if option == "1" or option=="calculate":
            while True:
                    user_input=input("\nenter your expression (or type 'back' to return) : ").strip().lower()
                     
                    if user_input=='back':
                        break
                    calculate(user_input)
        elif option == "2" or option=="history":
            show_history()
        elif option == "3" or option=="clear":
            clear_history()
        elif option == "4" or option=="exit":
            print("Goodbye🙋‍♂️\n")
            break
        else:
            print( "\nInvalid Selection,Select Among The Choices")
if __name__=="__main__":
    main()
        