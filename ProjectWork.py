import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk







from random import *
# Functions for Log In / SignUp / Admin








def LogIn() :
    WelcomeLabel.destroy()
    WelcomeLabel.destroy()



    WelcomeLabel1.destroy()
    WelcomeLabel1.destroy()


    WelcomeLabel2.destroy()
    WelcomeLabel2.destroy()





    Accounts = {}
    # Variables
    PriceRegular = DoubleVar()
    PriceRegular.set(0.59)

    PriceRegular2 = DoubleVar()
    PriceRegular2.set(1.18)

    PriceRegular3 = DoubleVar()
    PriceRegular3.set(1.37)

    PriceRegular4 = DoubleVar()
    PriceRegular4.set(0.472)

    PriceRegular5 = DoubleVar()
    PriceRegular5.set(0.384)

    #-----------------------------
    with open("Accounts.txt" ) as file:
        lines = file.read().splitlines()
    for i in lines :
        key,value = i.split(', ')
        Accounts.update({key:value})
    print(Accounts)
    def FindUser() :
        AccountFile = open('Accounts.txt' , "r").read().splitlines()
        #Functions for Calculation


        if Label_EnterLog.get() in Accounts :
            NewCheckDict = {Label_EnterLog.get() : Accounts[Label_EnterLog.get()]}
            AcountPasses = NewCheckDict.values()
            print(NewCheckDict)
            if Label_EnterLogPass.get() in AcountPasses:
                del NewCheckDict[Label_EnterLog.get()]
                LITER = IntVar()
                WindowMain.geometry('750x750')
                frameMainWindow = Frame(WindowMain, bd='10', bg="#494c59")
                frameMainWindow.place(relwidth=1, relheight=1, relx=0.5, anchor='n')

                def LiterOrMoney() :
                    if LITER.get() == 1 :
                        MoneyEntry.delete(0, END)
                        LiterEntry.config(state=NORMAL)
                        MoneyEntry.config(state=DISABLED )

                    elif LITER.get() == 2 :
                        LiterEntry.delete(0, END)
                        LiterEntry.config(state=DISABLED )
                        MoneyEntry.config(state=NORMAL )



                frameGasoline = Frame(frameMainWindow, bd='10', bg="#4834d4" , highlightthickness=3 , highlightbackground="#34ace0")
                frameGasoline.place(relheight=0.6, relwidth=0.4, relx=0.05, rely=0.06)

                LabelWelcome = Label(frameMainWindow, text=f"Welcome {Label_EnterLog.get()}", bd='10', bg="#494c59" , fg="white" , font=("Arial",13,"bold"))
                LabelWelcome.place(relx=0.4,rely=0.001 ,relwidth=0.2 )

                LabelGasoline = Label(frameGasoline, bd="10", bg="#4834d4", fg="white", font=("Arial", 20),
                                      text="Gasoline Station")
                LabelGasoline.place(relwidth=1, rely=0.01)

                Gasolines = {}

                # Starts here
                # Addint to Dict
                with open("Gasolines.txt") as file:
                    lines = file.read().splitlines()
                    print(lines)
                for i in lines:
                    key, value = i.split(', ')
                    Gasolines.update({key: value})

                print(Gasolines)



                def Change(event):
                    GasolinePriceEntry.config(state=NORMAL)
                    GasolinePriceEntry.delete(0,END)
                    GasolinePriceEntry.insert(0 , Gasolines[GasolineListBox.get()])
                    GasolinePriceEntry.config(state="readonly")
                    print(Gasolines[GasolineListBox.get()])
                GasolineListBox = ttk.Combobox(frameGasoline, values=list(Gasolines.keys()), width=13 , state="readonly" )
                GasolinesLabel = Label(frameMainWindow , text="Petrol : ", bg="#4834d4", fg="white", font=('Arial', 15))
                GasolinesLabel.place(rely=0.15, relx=0.1)
                GasolineListBox.place(rely=0.15, relx=0.4)
                GasolineListBox.bind('<<ComboboxSelected>>', Change)



                GasolinePrice = Label(frameMainWindow ,text="Price : ", bg="#4834d4", fg="white", font=('Arial', 15))
                GasolinePrice.place(rely=0.2, relx=0.1)
                DefaultString = StringVar()
                DefaultString.set("0.59")
                GasolinePriceEntry = Entry(frameGasoline, fg="black" , textvariable=DefaultString)
                GasolinePriceEntry.place(rely=0.24, relx=0.4, relheight=0.065)
                GasolinePriceEntry.config(state=DISABLED)



                AznLabel = Label(frameGasoline, text="AZN", font=('Arial', 13), bg="#4834d4", fg="white")
                AznLabel.place(rely=0.24, relx=0.89)

                Liter = Radiobutton(frameGasoline, text="Liter : ", activebackground="#4834d4", bg="#4834d4",
                                    font=('Arial', 15), variable=LITER, value=1  , command= LiterOrMoney)
                Money = Radiobutton(frameGasoline, text="Money : ", activebackground="#4834d4", bg="#4834d4",
                                    font=("Arial", 15), variable=LITER, value=2 , command= LiterOrMoney)

                Liter.place(rely=0.4, relx=0.01)
                Money.place(rely=0.5, relx=0.01)

                DefaultLiterString = StringVar()
                DefaultLiterString.set("0")

                DefaultMoneyString = StringVar()
                DefaultMoneyString.set("0")

                LiterEntry = Entry(frameGasoline, textvariable=DefaultLiterString,  state= DISABLED)
                LiterEntry.place(rely=0.41, relx=0.4, relheight=0.065)
                MoneyEntry = Entry(frameGasoline,textvariable=DefaultMoneyString, state= DISABLED )
                MoneyEntry.place(rely=0.51, relx=0.4, relheight=0.065 )

                SubbFrameForGas = Frame(frameGasoline, bd=10, highlightbackground="#4bcffa", highlightthickness=3,
                                        bg="#4834d4")
                SubbFrameForGas.place(relwidth=0.85, relheight=0.3, rely=0.7, relx=0.1)
                LabelAllPrice = Label(SubbFrameForGas, text="Total", bg="#4834d4", fg="white",
                                      font=('Arial', 20, "bold"))
                LabelAllPrice.place(anchor=NW)

                SummPriceValue = Label(SubbFrameForGas, text="0", bg="#4834d4", fg="white",
                                       font=("Arial", 20, "bold"), highlightthickness=3,
                                       highlightbackground="#4bcffa")
                SummPriceValue.place(rely=0.45, relx=0.1)

                SummLabel = Label(SubbFrameForGas , text="AZN" , bg="#4834d4" , fg="white" , font=('Arial' , 20 , "bold"))
                SummLabel.place(rely=0.45 , relx=0.6)





                # Cafe Frame
                HOTDOG = IntVar()
                FRIES = IntVar()
                QAMBURGER = IntVar()
                COLA = IntVar()

                def CafeCheckBoxes() :
                    if HOTDOG.get() == 1:
                        Hot_Dog_Entry_Count.config(state=NORMAL )

                    else :
                        Hot_Dog_Entry_Count.delete(0, END)
                        Hot_Dog_Entry_Count.config(state=DISABLED)

                    if FRIES.get() == 1:

                        Fries_Entry_Count.config(state=NORMAL)

                    else:
                        Fries_Entry_Count.delete(0, END)
                        Fries_Entry_Count.config(state=DISABLED )

                    if QAMBURGER.get() == 1:

                        Qamburger_Entry_Count.config(state=NORMAL)
                    else:
                        Qamburger_Entry_Count.delete(0, END)
                        Qamburger_Entry_Count.config(state=DISABLED)

                    if COLA.get() == 1 :

                        Cola_Entry_Count.config(state=NORMAL)

                    else:
                        Cola_Entry_Count.delete(0, END)
                        Cola_Entry_Count.config(state=DISABLED)
                    if Hot_Dog_Entry_Count.get() == "":
                        Hot_Dog_Entry_Count.config(state=NORMAL)
                        Hot_Dog_Entry_Count.insert(0, "0")
                        Hot_Dog_Entry_Count.config(state=DISABLED)
                    if Fries_Entry_Count.get() == "":
                        Fries_Entry_Count.config(state=NORMAL)
                        Fries_Entry_Count.insert(0, "0")
                        Fries_Entry_Count.config(state=DISABLED)
                    if Cola_Entry_Count.get() == "":
                        Cola_Entry_Count.config(state=NORMAL)
                        Cola_Entry_Count.insert(0, "0")
                        Cola_Entry_Count.config(state=DISABLED)
                    if Qamburger_Entry_Count.get() == "":
                        Qamburger_Entry_Count.config(state=NORMAL)
                        Qamburger_Entry_Count.insert(0, "0")
                        Qamburger_Entry_Count.config(state=DISABLED)



                Prices={}
                with open("Products.txt") as file:
                    lines = file.read().splitlines()
                for i in lines:
                    key, value = i.split(', ')
                    Prices.update({key: value})
                print(Prices)

                HotDogCountDefault = 1
                FriesCountDefault = 1
                ColaCountDefault = 1
                QamburgerCountDefault = 1

                frameCafe = Frame(frameMainWindow, bd="10", bg="#4834d4", highlightthickness=3 , highlightbackground="#34ace0")
                frameCafe.place(relwidth=0.4, relheight=0.6, rely=0.06, relx=0.55)

                CafeLabel = Label(frameCafe, text="Mini Cafe", anchor=N, bg="#4834d4", fg="white",
                                  font=('Arial', 20))
                CafeLabel.place(relx=0.25, rely=0.02)
                # Hot Dog Main
                Hot_Dog_CheckButton = Checkbutton(frameCafe, activebackground="#4834d4", text="Hot-Dog",
                                                  bg="#4834d4", font=('Arial', 15) , variable=HOTDOG , command=CafeCheckBoxes)
                Hot_Dog_CheckButton.place(rely=0.2, relx=0.01)

                Values = list(Prices.values())
                print(Values[0])

                Hot_Dog_Entry_Price = Entry(frameCafe, state= "readonly" )
                Hot_Dog_Entry_Price.config(state = NORMAL)
                Hot_Dog_Entry_Price.insert(0, Values[0])
                Hot_Dog_Entry_Price.config(state="readonly")
                Hot_Dog_Entry_Price.place(rely=0.23, relx=0.45, relwidth=0.2, relheight=0.05)

                Hot_Dog_Entry_Count = Entry(frameCafe, state=DISABLED)
                Hot_Dog_Entry_Count.place(rely=0.23, relx=0.7, relwidth=0.2, relheight=0.05)
                # Fries Main

                Fries_CheckButton = Checkbutton(frameCafe, activebackground="#4834d4", text="Fries",
                                                bg="#4834d4", font=('Arial', 15) , variable=FRIES , command=CafeCheckBoxes)
                Fries_CheckButton.place(rely=0.3, relx=0.01)


                Fries_Price_Entry = Entry(frameCafe,  state="readonly")
                Fries_Price_Entry.place(rely=0.33, relx=0.45, relwidth=0.2, relheight=0.05)
                Fries_Price_Entry.config(state = NORMAL)
                Fries_Price_Entry.insert(0, Values[1])
                Fries_Price_Entry.config(state="readonly")
                Fries_Entry_Count = Entry(frameCafe, state=DISABLED)
                Fries_Entry_Count.place(rely=0.33, relx=0.7, relwidth=0.2, relheight=0.05)

                # Cola Main

                Cola_CheckButton = Checkbutton(frameCafe, activebackground="#4834d4", text="Cola", bg="#4834d4",
                                               font=('Arial', 15) , variable= COLA, command=CafeCheckBoxes)
                Cola_CheckButton.place(rely=0.4, relx=0.01)


                Cola_Price_Entry = Entry(frameCafe,  state="readonly")
                Cola_Price_Entry.place(rely=0.43, relx=0.45, relwidth=0.2, relheight=0.05)
                Cola_Price_Entry.config(state=NORMAL)
                Cola_Price_Entry.insert(0,Values[2])
                Cola_Price_Entry.config(state="readonly")
                Cola_Entry_Count = Entry(frameCafe,  state=DISABLED)
                Cola_Entry_Count.place(rely=0.43, relx=0.7, relwidth=0.2, relheight=0.05)

                # Qamburger Main

                Qamburger_CheckButton = Checkbutton(frameCafe, activebackground="#4834d4", text="Qamburger",
                                                    bg="#4834d4", font=('Arial', 15) , variable=QAMBURGER, command=CafeCheckBoxes)
                Qamburger_CheckButton.place(rely=0.5, relx=0.01)


                Qamburger_Price_Entry = Entry(frameCafe,  state="readonly")
                Qamburger_Price_Entry.place(rely=0.53, relx=0.5, relwidth=0.2, relheight=0.05)
                Qamburger_Price_Entry.config(state=NORMAL)
                Qamburger_Price_Entry.insert(0, Values[3])
                Qamburger_Price_Entry.config(state="readonly")
                Qamburger_Entry_Count = Entry(frameCafe,  state=DISABLED)
                Qamburger_Entry_Count.place(rely=0.53, relx=0.75, relwidth=0.2, relheight=0.05)

                if Hot_Dog_Entry_Count.get() == "":
                    Hot_Dog_Entry_Count.config(state=NORMAL)
                    Hot_Dog_Entry_Count.insert(0, "0")
                    Hot_Dog_Entry_Count.config(state=DISABLED)
                if Fries_Entry_Count.get() == "":
                    Fries_Entry_Count.config(state=NORMAL)
                    Fries_Entry_Count.insert(0, "0")
                    Fries_Entry_Count.config(state=DISABLED)
                if Cola_Entry_Count.get() == "":
                    Cola_Entry_Count.config(state=NORMAL)
                    Cola_Entry_Count.insert(0, "0")
                    Cola_Entry_Count.config(state=DISABLED)
                if Qamburger_Entry_Count.get() == "":
                    Qamburger_Entry_Count.config(state=NORMAL)
                    Qamburger_Entry_Count.insert(0, "0")
                    Qamburger_Entry_Count.config(state=DISABLED)



                # All Money Main
                def CalculateButton() :




                    # Gasoline Calculation
                    if LITER.get() == 1 :
                        if GasolineListBox.get() == "Regular 92":
                            SumOfGasoline = float(LiterEntry.get()) * PriceRegular.get()
                            MoneyEntry.config(state=NORMAL)
                            SummLabel.config(text = "AZN")
                            SummPriceValue.config(text=f"{SumOfGasoline:.1f}")
                        elif GasolineListBox.get() == "Super 95":
                            SumOfGasoline = float(LiterEntry.get()) * PriceRegular2.get()
                            SummPriceValue.config(text=f"{SumOfGasoline:.1f}")
                            SummLabel.config(text="AZN")
                        elif GasolineListBox.get() == "Premium 98":
                            SumOfGasoline = float(LiterEntry.get()) * PriceRegular3.get()
                            SummPriceValue.config(text=f"{SumOfGasoline:.1f}")
                            SummLabel.config(text="AZN")
                        elif GasolineListBox.get() == "Diesel":
                            SumOfGasoline = float(LiterEntry.get()) * PriceRegular4.get()
                            SummLabel.config(text="AZN")
                            SummPriceValue.config(text=f"{SumOfGasoline:.1f}")
                        elif GasolineListBox.get() == "LPG":
                            SumOfGasoline = float(LiterEntry.get()) * PriceRegular5.get()
                            SummLabel.config(text="AZN")
                            SummPriceValue.config(text=f"{SumOfGasoline:.1f}")
                    elif LITER.get() == 2 :
                        if GasolineListBox.get() == "Regular 92":
                            SumOfGass = int(MoneyEntry.get()) / PriceRegular.get()
                            SummLabel.config(text="Liters")
                            SummPriceValue.config(text=f"{SumOfGass:.1f}")
                        elif GasolineListBox.get() == "Super 95":
                            SumOfGass = int(MoneyEntry.get()) / PriceRegular2.get()
                            SummPriceValue.config(text=f"{SumOfGass:.1f}")
                            SummLabel.config(text="Liters")
                        elif GasolineListBox.get() == "Premium 98":
                            SumOfGass = int(MoneyEntry.get()) / PriceRegular3.get()
                            SummLabel.config(text="Liters")
                            SummPriceValue.config(text=f"{SumOfGass:.1f}")
                        elif GasolineListBox.get() == "Diesel":
                            SumOfGass = int(MoneyEntry.get()) / PriceRegular4.get()
                            SummLabel.config(text="Liters")
                            SummPriceValue.config(text=f"{SumOfGass:.1f}")
                        elif GasolineListBox.get() == "LPG":
                            SumOfGass = int(MoneyEntry.get()) / PriceRegular5.get()
                            SummLabel.config(text="Liters")
                            SummPriceValue.config(text=f"{SumOfGass:.1f}")

                    # Cafe Calculations

                    SumCafeUp = (float(HotDogCountDefault * Hot_Dog_Entry_Count.get()) * float(Hot_Dog_Entry_Price.get())) + (
                                float(FriesCountDefault * Fries_Entry_Count.get()) * float(Fries_Price_Entry.get())) + (
                                    float(ColaCountDefault * Cola_Entry_Count.get()) * float(Cola_Price_Entry.get())) + (
                                        float( QamburgerCountDefault * Qamburger_Entry_Count.get()) * float(Qamburger_Price_Entry.get()))
                    SummPriceValueCafe.config(text = f"{SumCafeUp:.1f}")

                    # Summ All UP

                    SumAllUp = SumCafeUp + float(SummPriceValue.cget("text"))
                    CalculateLabel1.config(text=f"{SumAllUp:.1f}")


                    ReceiptWindow = Tk()
                    ReceiptWindow.geometry("500x700")
                    ReceiptWindow.resizable(False,False)
                    ReceiptWindow.title("Receipt")
                    ReceiptWindow.config(bg="#c8d6e5")



                    LabelReceipt = Label(ReceiptWindow , text="Receipt", bg="#c8d6e5" , fg="black" , font=("Arial" , 20 , "bold"))
                    LabelReceipt.place(rely=0.001,relx =0.4)




                    FrameMainReceipt = Frame(ReceiptWindow,bd="10",bg="#576574")
                    FrameMainReceipt.place(relheight=0.9, relwidth=0.9, relx=0.05, rely=0.05)





                    CashierName = Label(FrameMainReceipt ,text=f"Cashier Name : {Label_EnterLog.get()}" , bg="#576574" , fg="white" , font=("Arial" , 15 , "bold"))
                    CashierName.place(relx=0.01 , rely=0.01)
                    CashierName = Label(FrameMainReceipt ,text="Omar™" , bg="#576574" , fg="white" , font=("Arial" , 15 , "bold"))
                    CashierName.place(relx=0.8 , rely=0.01)

                    FoodFrame = Frame(FrameMainReceipt , bd="10" , bg="#2d3436")
                    FoodFrame.place(relx=0.1,rely=0.1 , relheight=0.5 , relwidth=0.8)



                    ProductLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text="Product" , font=('Arial', 12 , "bold") , fg="white")
                    ProductLabel.place(relx=0.01 , rely=0.2)
                    PriceLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text="Price" , font=('Arial', 12 , "bold") , fg="white")
                    PriceLabel.place(relx=0.35 , rely=0.2 ,relwidth=0.25)
                    CountLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text="Count" , font=('Arial', 12 , "bold") , fg="white")
                    CountLabel.place(relx=0.7 , rely=0.2)
                    # Hot Dog




                    HotDogLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text="Hot Dog" , font=('Arial', 12 , "bold") , fg="white")
                    HotDogLabel.place(relx=0.01 , rely=0.3)
                    HotDogPriceLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text=Hot_Dog_Entry_Price.get() , font=('Arial', 12 , "bold") , fg="white")
                    HotDogPriceLabel.place(relx=0.35 , rely=0.3,relwidth=0.25)
                    HotDogCountLabel = Label(FoodFrame , bd="10" , bg="#2d3436" , text=Hot_Dog_Entry_Count.get() , font=('Arial', 12 , "bold") , fg="white")
                    HotDogCountLabel.place(relx=0.75 , rely=0.3)

                    # Fries


                    FriesLabel = Label(FoodFrame, bd="10", bg="#2d3436", text="Fries", font=('Arial', 12, "bold"),
                                        fg="white")
                    FriesLabel.place(relx=0.01, rely=0.4)
                    FriesPriceLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Fries_Price_Entry.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    FriesPriceLabel.place(relx=0.35, rely=0.4, relwidth=0.25)
                    FriesCountLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Fries_Entry_Count.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    FriesCountLabel.place(relx=0.75, rely=0.4)

                    # Cola


                    ColaLabel = Label(FoodFrame, bd="10", bg="#2d3436", text="Cola", font=('Arial', 12, "bold"),
                                        fg="white")
                    ColaLabel.place(relx=0.01, rely=0.5)
                    ColaPriceLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Cola_Price_Entry.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    ColaPriceLabel.place(relx=0.35, rely=0.5, relwidth=0.25)
                    ColaCountLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Cola_Entry_Count.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    ColaCountLabel.place(relx=0.75, rely=0.5)

                    # Qamburger

                    QamburgerLabel = Label(FoodFrame, bd="10", bg="#2d3436", text="Qamburger", font=('Arial', 12, "bold"),
                                        fg="white")
                    QamburgerLabel.place(relx=0.01, rely=0.6)
                    QamburgerPriceLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Qamburger_Price_Entry.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    QamburgerPriceLabel.place(relx=0.35, rely=0.6, relwidth=0.25)
                    QamburgerCountLabel = Label(FoodFrame, bd="10", bg="#2d3436", text=Qamburger_Entry_Count.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    QamburgerCountLabel.place(relx=0.75, rely=0.6)

                    # TotalLabel
                    TotalLabel = Label(FoodFrame, bd="10", bg="#2d3436", text="Total : ",
                                       font=('Arial', 12, "bold"), fg="white")
                    TotalLabel.place(relx=0.01, rely=0.8)

                    TotalLabelPrice = Label(FoodFrame, bd="10", bg="#2d3436", text=SummPriceValueCafe.cget("text"),
                                             font=('Arial', 12, "bold"), fg="white")
                    TotalLabelPrice.place(relx=0.75, rely=0.8)
                    MenuCafe = Label(FoodFrame, bd="10", bg="#2d3436", text="Cafe Menu",
                                             font=('Arial', 20, "bold"), fg="white")
                    MenuCafe.place(relx=0.1, rely=0.01 , relwidth=0.7)

                    GasolineFrame = Frame(FrameMainReceipt, bd="10", bg="#2d3436")
                    GasolineFrame.place(relx=0.1, rely=0.65, relheight=0.2, relwidth=0.8)

                    GasolineTypeL = Label(GasolineFrame, bd="10", bg="#2d3436", text="Gasoline type",
                                              font=('Arial', 12, "bold"), fg="white")
                    GasolineTypeL.place(rely=0.01, relx=0.01)
                    GasolineLitersL = Label(GasolineFrame, bd="10", bg="#2d3436", text="Liters",
                                              font=('Arial', 12, "bold"), fg="white")
                    GasolineLitersL.place(rely=0.01, relx=0.45)
                    GasolineManatL = Label(GasolineFrame, bd="10", bg="#2d3436", text="Total",
                                              font=('Arial', 12, "bold"), fg="white")
                    GasolineManatL.place(rely=0.01, relx=0.75)

                    GasolineTypeLabel = Label(GasolineFrame, bd="10", bg="#2d3436", text=GasolineListBox.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    GasolineTypeLabel.place(rely=0.3,relx=0.01)

                    GasolineLitersLabel = Label(GasolineFrame, bd="10", bg="#2d3436", text=LiterEntry.get(),
                                             font=('Arial', 12, "bold"), fg="white")
                    GasolineLitersLabel.place(rely=0.3,relx=0.45)
                    GasolineManatLabel = Label(GasolineFrame, bd="10", bg="#2d3436", text=SummPriceValue.cget("text"),
                                               font=('Arial', 12, "bold"), fg="white")
                    GasolineManatLabel.place(rely=0.3, relx=0.75)

                    if LITER.get() == 1 :
                        GasolineLitersL.config(text="Liters")
                        GasolineLitersLabel.config(text=LiterEntry.get())
                    elif LITER.get()==2 :
                        GasolineLitersL.config(text="Manat")
                        GasolineLitersLabel.config(text=MoneyEntry.get())





                    TotalLabel = Label(FrameMainReceipt , text=f"Total is : {CalculateLabel1.cget('text')} AZN", bg="#576574" , fg="white", font=("Arial" , 15 , "bold"))
                    TotalLabel.place(relx=0.01 , rely=0.9)

                    Receipt = {"Name":Label_EnterLog.get() , "HotDog" : [HotDogPriceLabel.cget("text") ,HotDogCountLabel.cget("text")]
                        , "Fries" : [FriesPriceLabel.cget("text") ,FriesCountLabel.cget("text")] ,
                               "Cola" : [ColaPriceLabel.cget("text") ,ColaCountLabel.cget("text")] ,
                               "Qamburger" : [QamburgerPriceLabel.cget("text") ,QamburgerCountLabel.cget("text")] ,
                               GasolineListBox.get() : [GasolineLitersL.cget("text") , SummPriceValue.cget("text")]}

                    ReceiptFile = open('Receipt.txt', 'w')
                    for key, value in Receipt.items():
                        ReceiptFile.write(f'{key}, {value}\n')
                    print(ReceiptFile)


                    def ExitReceipt() :
                        ReceiptWindow.destroy()
                    ExitButtonReceipt = Button(FrameMainReceipt , text="Exit" ,activebackground="#686de0",
                                         bg="#686de0", fg="white", font=('Arial', 15, "bold")  , command=ExitReceipt)
                    ExitButtonReceipt.place(relx=0.75 , rely=0.9 , relwidth=0.25 , relheight=0.09)


                def DeleteAll():
                    LITER.set(0)
                    LiterEntry.delete(0 , END)
                    MoneyEntry.delete(0,END)
                    SummPriceValue.config(text = "0")

                    #Cafe

                    Hot_Dog_Entry_Count.delete(0, END)
                    Fries_Entry_Count.delete(0,END)
                    Qamburger_Entry_Count.delete(0,END)
                    Cola_Entry_Count.delete(0,END)
                    SummPriceValueCafe.config(text="0")

                    HOTDOG.set(0)
                    COLA.set(0)
                    QAMBURGER.set(0)
                    FRIES.set(0)

                    # All

                    CalculateLabel1.config(text="0")

                SubbFrameForCafe = Frame(frameCafe, bd=10, highlightbackground="#0be881", highlightthickness=3,
                                         bg="#4834d4")
                SubbFrameForCafe.place(relwidth=0.85, relheight=0.3, rely=0.7, relx=0.1)
                LabelAllPriceCafe = Label(SubbFrameForCafe, text="Total", bg="#4834d4", fg="white",
                                          font=('Arial', 20, "bold"))
                LabelAllPriceCafe.place(anchor=NW)

                SummPriceValueCafe = Label(SubbFrameForCafe, text="0", bg="#4834d4", fg="white",
                                           font=("Arial", 20, "bold"), highlightthickness=3,
                                           highlightbackground="#0be881")
                SummPriceValueCafe.place(rely=0.45, relx=0.1)
                SummPriceValueCafeLabel = Label(SubbFrameForCafe, text="AZN", font=('Arial', 20 , "bold"), bg='#4834d4',
                                                fg='white')
                SummPriceValueCafeLabel.place(rely=0.5, relx=0.7)

                frameSumUpCafe = Frame(frameMainWindow, bd='10', bg="#4834d4", highlightthickness=3 , highlightbackground="#34ace0")
                frameSumUpCafe.place(relwidth=0.9, relheight=0.25, rely=0.7, relx=0.05)

                LabelSumUp = Label(frameSumUpCafe, text="All price", bg="#4834d4", fg="white",
                                   font=('Arial', 15, "bold"))
                LabelSumUp.place(rely=0.01, relx=0.01)

                CalculateButton = Button(frameSumUpCafe, text="Calculate", activebackground="#686de0",
                                         bg="#686de0", fg="white", font=('Arial', 15, "bold") , command= CalculateButton)
                CalculateButton.place(rely=0.4, relx=0.1)
                CalculateButton = Button(frameSumUpCafe, text="Delete All", activebackground="#686de0",
                                         bg="#686de0", fg="white", font=('Arial', 15, "bold") , command=DeleteAll)
                CalculateButton.place(rely=0.4, relx=0.3)

                CalculateLabel1 = Label(frameSumUpCafe, text="0", bg="#686de0", fg="white",
                                        font=('Arial', 15, "bold"))
                CalculateLabel1.place(rely=0.35, relx=0.5, relheight=0.4, relwidth=0.2)
                CalculateLabel2 = Label(frameSumUpCafe, text="AZN", bg="#4834d4", fg="white",
                                        font=('Arial', 15, "bold"))
                CalculateLabel2.place(rely=0.35, relx=0.75, relheight=0.4, relwidth=0.09)

                def ExitButton():
                    frameMainWindow.destroy()
                    Label_EnterLog.delete(0,END)
                    Label_EnterLogPass.delete(0,END)

                ExitButton = Button(frameMainWindow,text="Exit" , activebackground="#686de0",
                                         bg="#686de0", fg="white", font=('Arial', 10, "bold"),command=ExitButton)
                ExitButton.place(relx=0.8 , rely=0.97 , relwidth=0.2)
        else:
            Message = messagebox.showerror(title="Error" , message="Login or Password incorrect! ")

    frame = Frame(WindowMain, bd='10')
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')
    Label_Title = Label(frame, text='Log In', font=16)
    Label_Title.place(relwidth=1, relheight=0.1)

    Label_Login = Label(frame, text='Login :')
    Label_Login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    Label_PasswordLogin = Label(frame, text="Password : ")
    Label_PasswordLogin.place(rely=0.4, relwidth=0.35, relheight=0.1)

    Label_EnterLog = Entry(frame)
    Label_EnterLog.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
    Label_EnterLogPass = Entry(frame, show='*')
    Label_EnterLogPass.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

    ButtonSignUp = Button(frame, text="Log In" , command=FindUser)
    ButtonSignUp.place(relx=0.3, rely=0.6, relheight=0.15, relwidth=0.5)
def Admin() :
    WelcomeLabel.destroy()
    WelcomeLabel.destroy()
    WelcomeLabel1.destroy()
    WelcomeLabel1.destroy()
    WelcomeLabel2.destroy()
    WelcomeLabel2.destroy()
    def AdminLogIn():

        def AddGasoline() :
            if ComboBoxForPick.get() == "Gasoline" :
                NewGasolines = {}
                with open("Gasolines.txt") as file:
                    lines = file.read().splitlines()
                for i in lines:
                    key, value = i.split(', ')
                    NewGasolines.update({key: value})
                print(NewGasolines)

                if EntryForName.get() in NewGasolines :
                    Message = messagebox.showerror(title="Error" , message="Gasoline already exists")
                else:
                    NewGasolines.update({EntryForName.get(): EntryForPassword.get()})
                    GasolineFile = open('Gasolines.txt', 'w')
                    for key, value in NewGasolines.items():
                        GasolineFile.write(f'{key}, {value}\n')
                    Message = messagebox.showinfo(title="Success", message="Gas has been added!")
                    print(NewGasolines)




            elif ComboBoxForPick.get() == "Cashier" :
                Accounts = {}
                # reading files
                with open("Accounts.txt") as file:
                    lines = file.read().splitlines()
                for i in lines:
                    key, value = i.split(', ')
                    Accounts.update({key: value})
                print(Accounts)
                if  EntryForName.get() in Accounts :
                    Message = messagebox.showerror(title="Eror" , message="Account already exist")
                else:
                    Accounts[EntryForName.get()] = EntryForPassword.get()
                    # Adding to file
                    AccountsFile = open('Accounts.txt', 'a')
                    for key, value in Accounts.items():
                        AccountsFile.write(f'{key}, {value}\n')
                    MessageBox = messagebox.showinfo(title="Account Created", message="Account has been created")
            else:
                MessageBox = messagebox.showinfo(title="Account Created", message="Account has been created")




        def RemoveGasoline() :
            if ComboBoxForPick.get() == "Gasoline" :
                with open("Gasolines.txt") as file:
                    lines = file.read().splitlines()
                for i in lines:
                    key, value = i.split(', ')
                    AllGas.update({key: value})

                print(AllGas)
                if EntryForName.get() not in AllGas :
                    Message = messagebox.showerror(title="Error" , message="Gasoline not found")
                else:
                    AllGas.pop(EntryForName.get())
                    print(AllGas)

                    GasolineFile = open('Gasolines.txt', 'w')
                    for key, value in AllGas.items():
                        GasolineFile.write(f'{key}, {value}\n')
                    messagebox.showinfo(title="Success", message="Gasoline has been removed")

            if ComboBoxForPick.get() == "Cashier" :
                Accs= {}
                with open("Accounts.txt") as file:
                    lines = file.read().splitlines()
                for i in lines:
                    key, value = i.split(', ')
                    Accs.update({key: value})


                print(Accs)
                if EntryForName.get() not in Accs :
                    Message = messagebox.showerror(title="Error" , message="Account not found")
                else:
                    Accs.pop(EntryForName.get())
                    print(AllGas)
                    AccsFiles = open('Accounts.txt', 'w')
                    for key, value in Accs.items():
                        AccsFiles.write(f'{key}, {value}\n')
                    messagebox.showinfo(title="Success", message="Gas has been removed")

        def UpdateHotDogPrice():
            with open("Products.txt") as file:
                lines = file.read().splitlines()
            for i in lines:
                key, value = i.split(', ')
                Prices.update({key: value})

            if HotDogsEntry.get() != "":
                Prices["Hot Dog"] = HotDogsEntry.get()
                ProductFile = open('Products.txt', 'w')
                for key, value in Prices.items():
                    ProductFile.write(f'{key}, {value}\n')
                messagebox.showinfo(title="Success", message="Successfully changed!")
            else:
                Message = messagebox.showerror(title="Error", message="No Value Given")

            print(Prices)


        def UpdateFriesPrice():
            with open("Products.txt") as file:
                lines = file.read().splitlines()
            for i in lines:
                key, value = i.split(', ')
                Prices.update({key: value})

            if FriesEntry.get() != "":
                Prices["Fries"] = FriesEntry.get()
                ProductFile = open('Products.txt', 'w')
                for key, value in Prices.items():
                    ProductFile.write(f'{key}, {value}\n')
                messagebox.showinfo(title="Success", message="Successfully changed!")
            else:
                Message = messagebox.showerror(title="Error", message="No Value Given")

            print(Prices)


        def UpdateColaPrice():
            with open("Products.txt") as file:
                lines = file.read().splitlines()
            for i in lines:
                key, value = i.split(', ')
                Prices.update({key: value})

            if ColaEntry.get() != "":
                Prices["Cola"] = ColaEntry.get()
                ProductFile = open('Products.txt', 'w')
                for key, value in Prices.items():
                    ProductFile.write(f'{key}, {value}\n')
                messagebox.showinfo(title="Success", message="Successfully changed!")
            else:
                Message = messagebox.showerror(title="Error", message="No Value Given")

            print(Prices)


        def UpdateQamburgerPrice():
            with open("Products.txt") as file:
                lines = file.read().splitlines()
            for i in lines:
                key, value = i.split(', ')
                Prices.update({key: value})
            if QamburgerEntry.get() != "" :
                 Prices["Qamburger"] = QamburgerEntry.get()
                 ProductFile = open('Products.txt', 'w')
                 for key, value in Prices.items():
                     ProductFile.write(f'{key}, {value}\n')
                 messagebox.showinfo(title="Success", message="Successfully changed!")
            else:
                Message = messagebox.showerror(title="Error" , message="No Value Given")

            print(Prices)



        def ResetButton():
            with open("Products.txt") as file:
                lines = file.read().splitlines()
            for i in lines:
                key, value = i.split(', ')
                Prices.update({key: value})

            Prices["Hot Dog"] = 4
            Prices["Qamburger"] = 5.4
            Prices["Fries"] = 7.2
            Prices["Cola"] = 4.4

            print(Prices)

            ProductFile = open('Products.txt', 'w')
            for key, value in Prices.items():
                ProductFile.write(f'{key}, {value}\n')
            messagebox.showinfo(title="Success", message="Successfully changed!")

        def BackButton():
            frameMainWindow.destroy()
            Label_EnterLog.delete(0 , END)
            Label_EnterLogPass.delete(0,END)


        if Label_EnterLog.get() == 'Omar' and Label_EnterLogPass.get() == '1' :

            def ChangeLabels(event):
                if ComboBoxForPick.get() == "Cashier" :
                    LabelName.config(text= "Login")
                    LabelPrice.config(text="Password")
                elif ComboBoxForPick.get() == "Gasoline" :
                    LabelName.config(text="Gasoline")
                    LabelPrice.config(text="Price")

            AllGas = {}
            Prices = {}
            frameMainWindow = Frame(WindowMain, bd='10', bg="#494c59")
            frameMainWindow.place(relwidth=1, relheight=1, relx=0.5, anchor='n')

            LabelWelcome = Label(frameMainWindow , bd='10' , bg="#494c59" , text=f"Welcome {Label_EnterLog.get()}" , font=("Arial" , 15 , "bold") , fg="white")
            LabelWelcome.place(anchor="n", relx=0.5)


            frameForAddGasoline = Frame(frameMainWindow , bd="10" , bg="#4834d4")
            frameForAddGasoline.place(relx=0.01 , rely=0.069 , relheight=0.4 , relwidth=0.99)

            LabelForAdd = Label(frameForAddGasoline, bg="#4834d4" , text = "Change Gasoline/Create User" , font=('Arial', 15 , 'bold') , fg="white" )
            LabelForAdd.place(relx = 0.23 , rely=0.01 )

            LabelName = Label(frameForAddGasoline , bg="#4834d4" , text= "Name" , font=('Arial', 13 , 'bold') , fg="white")
            LabelName.place(relx=0.01 , rely=0.3)

            EntryForName = Entry(frameForAddGasoline )
            EntryForName.place(rely=0.3 , relx=0.2 , relheight=0.15 , relwidth=0.3)


            LabelPrice = Label(frameForAddGasoline , bg="#4834d4" , text= "Password" , font=('Arial', 13 , 'bold') , fg="white")
            LabelPrice.place(relx=0.01 , rely=0.6)

            EntryForPassword = Entry(frameForAddGasoline)
            EntryForPassword.place(rely=0.6 , relx=0.2 , relheight=0.15 , relwidth=0.3)


            AddGasolineButton = Button(frameForAddGasoline ,text="Add" , font=('Arial' ,10  , "bold") , command=AddGasoline)
            AddGasolineButton.place(rely=0.3 , relx=0.7 , relheight=0.15 , relwidth=0.3)
            AddGasolineButton = Button(frameForAddGasoline ,text="Remove" , font=('Arial' ,10  , "bold") , command=RemoveGasoline)
            AddGasolineButton.place(rely=0.5 , relx=0.7, relheight=0.15 , relwidth=0.3)
            Pick = ["Cashier" , "Gasoline"]
            ComboBoxForPick = ttk.Combobox(frameForAddGasoline, values=Pick , width=10)
            ComboBoxForPick.current(0)
            ComboBoxForPick.bind("<<ComboboxSelected>>", ChangeLabels)
            ComboBoxForPick.place(rely=0.7 , relx=0.7 , relheight=0.15 , relwidth=0.3)




            frameforFoodPrice = Frame(frameMainWindow, bd="10" , bg="#4834d4")
            frameforFoodPrice.place(relx=0.01 , rely=0.5 , relheight=0.4 , relwidth=0.99)

            FoodPriceLabelMain = Label(frameforFoodPrice , text="Change Food Price" , font=('Arial' , 16 , "bold") , bg="#4834d4" ,fg="white")
            FoodPriceLabelMain.place(rely=0.01 , relx=0.28)

            HotDogsLabel = Label(frameforFoodPrice , text="Hot Dog Price : " , font=('Arial' , 13 , "bold") , bg="#4834d4" , fg="white")
            HotDogsLabel.place(relx=0.01 , rely=0.2)

            HotDogsEntry = Entry(frameforFoodPrice)
            HotDogsEntry.place(relx=0.3 , rely=0.22 , relheight=0.1)

            HotDogsButton = Button(frameforFoodPrice , text="Change" , font=("Arial" , 8 , "bold") , command=UpdateHotDogPrice)
            HotDogsButton.place(relx=0.6 , rely=0.22 , relheight=0.1)

            FriesLabel = Label(frameforFoodPrice , text="Fries Price : " , font=('Arial' , 13 , "bold") , bg="#4834d4" , fg="white")
            FriesLabel.place(relx=0.01 , rely=0.4)


            FriesEntry = Entry(frameforFoodPrice)
            FriesEntry.place(relx=0.3, rely=0.42, relheight=0.1)

            FriesButton = Button(frameforFoodPrice , text="Change" , font=("Arial" , 8 , "bold") , command=UpdateFriesPrice)
            FriesButton.place(relx=0.6 , rely=0.42 , relheight=0.1)

            QamburgerLabel = Label(frameforFoodPrice , text="Qamburger Price : " , font=('Arial' , 13 , "bold") , bg="#4834d4" , fg="white")
            QamburgerLabel.place(relx=0.01 , rely=0.6)

            QamburgerEntry = Entry(frameforFoodPrice)
            QamburgerEntry.place(relx=0.35, rely=0.62, relheight=0.1)

            QamburgerButton = Button(frameforFoodPrice , text="Change" , font=("Arial" , 8 , "bold") , command= UpdateQamburgerPrice)
            QamburgerButton.place(relx=0.65 , rely=0.62 , relheight=0.1)

            ColaLabel = Label(frameforFoodPrice , text="Cola Price : " , font=('Arial' , 13 , "bold") , bg="#4834d4" , fg="white")
            ColaLabel.place(relx=0.01 , rely=0.8)

            ColaEntry = Entry(frameforFoodPrice)
            ColaEntry.place(relx=0.3, rely=0.82, relheight=0.1)

            ColaButton = Button(frameforFoodPrice , text="Change" , font=("Arial" , 8 , "bold") , command=UpdateColaPrice)
            ColaButton.place(relx=0.6 , rely=0.82 , relheight=0.1)

            ResetButton = Button(frameforFoodPrice , text="RESET" , font=("Arial" , 8 , "bold") , command=ResetButton)
            ResetButton.place(relx=0.8 , rely=0.35 , relheight=0.5 , relwidth=0.2)

            BackButton = Button(frameMainWindow , text="Back" ,activebackground="#686de0",
                                         bg="#686de0", fg="white", font=('Arial', 15, "bold")  , command=BackButton)
            BackButton.place(rely=0.95 , relx=0.7 , relwidth=0.3)
        else:
            Message =  messagebox.showerror(title="Error" , message="Something went wrong!")



    frame = Frame(WindowMain, bd='10')
    frame.place(relx=0.5, rely=0.2, relwidth=0.7, relheight=0.6, anchor='n')
    Label_Title = Label(frame, text='Admin', font=16)
    Label_Title.place(relwidth=1, relheight=0.1)

    Label_Login = Label(frame, text='Login :')
    Label_Login.place(rely=0.2, relwidth=0.35, relheight=0.1)

    Label_PasswordLogin = Label(frame, text="Password : ")
    Label_PasswordLogin.place(rely=0.4, relwidth=0.35, relheight=0.1)

    Label_EnterLog = Entry(frame)
    Label_EnterLog.place(relx=0.4, rely=0.2, relheight=0.1, relwidth=0.55)
    Label_EnterLogPass = Entry(frame, show='*')
    Label_EnterLogPass.place(relx=0.4, rely=0.4, relheight=0.1, relwidth=0.55)

    ButtonSignUp = Button(frame, text="Log In" , command=AdminLogIn)
    ButtonSignUp.place(relx=0.3, rely=0.6, relheight=0.15, relwidth=0.5)




WindowMain = Tk()
WindowMain.resizable(False,False)
WindowMain.title("Main")
WindowMain.geometry('750x750')
WindowMain.config(bg="#494c59")

WelcomeLabel = Label(text="Welcome!" , font=("Arial" , 50 , "bold") , bg ="#494c59"  , fg = "white" )
WelcomeLabel.place(rely=0.34 , relx=0.25 , relwidth=0.45)
WelcomeLabel1 = Label(text="Press one of the buttons above" , font=("Arial" , 35 , "bold") , bg ="#494c59"  , fg = "white" )
WelcomeLabel1.place(rely=0.54 , relx=0.04)
WelcomeLabel2 = Label(text="to start!" , font=("Arial" , 35 , "bold") , bg ="#494c59"  , fg = "white" )
WelcomeLabel2.place(rely=0.64 , relx=0.35)


SignUp_Button = Button(text="Cashier" , bg='gold' , command=LogIn  , font=("Arial",15 , "bold"))
SignUp_Button.place(relx = 0.1 , rely = 0.1 , relwidth=0.3 ,relheight=0.07 )
SignUp_Button = Button(text="Admin" , bg='gold' , command=Admin ,  font=("Arial",15 , "bold"))
SignUp_Button.place(relx = 0.6, rely = 0.1 , relwidth=0.3 , relheight=0.07)

CreditsLabel = Label(text="Made by Omar™ " , font=("Arial" , 20 , "bold") , bg ="#494c59"  , fg = "white")
CreditsLabel.place(rely=0.95 , relx=0.7)
WindowMain.mainloop()