import datetime
import random
import time
from tkinter import *
from tkinter import messagebox, ttk

import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Medical Care System")
        self.root.geometry("1540x800+0+0")

        self.NameTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberTablets = StringVar()
        self.Lot = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.SideEffect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.DrivingUsingMachine = StringVar()
        self.HowToUseMedication = StringVar()
        self.PatientId = StringVar()
        self.PatientNHSNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        self.canvas = Canvas(self.root, width=1540, height=120)
        self.canvas.pack(fill=X)

        self.gradient(self.canvas, "#1E3A8A", "#00AEEF")

        lbltitle = Label(
            self.canvas,
            text="🏥 ADVANCED MEDICAL CARE SYSTEM 🏥",
            fg="white",
            bg="#1E3A8A",
            font=("Times New Roman", 55, "bold"),
            padx=20,
            pady=10,
        )
        lbltitle.place(relx=0.5, rely=0.5, anchor=CENTER)

    def gradient(self, canvas, color1, color2):
        """Creates a gradient background effect"""
        for i in range(1540):
            r = int(
                (1 - i / 1540) * int(color1[1:3], 16)
                + (i / 1540) * int(color2[1:3], 16)
            )
            g = int(
                (1 - i / 1540) * int(color1[3:5], 16)
                + (i / 1540) * int(color2[3:5], 16)
            )
            b = int(
                (1 - i / 1540) * int(color1[5:7], 16)
                + (i / 1540) * int(color2[5:7], 16)
            )
            hex_color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(i, 0, i, 120, fill=hex_color, width=1)

            ############################ DataFrame #########################
            DataFrame = Frame(self.root, bd=20, relief=RIDGE)
            DataFrame.place(x=0, y=130, width=1530, height=400)
            DataFrameLeft = LabelFrame(
                DataFrame,
                bd=10,
                relief=RIDGE,
                padx=10,
                text="Patient Information",
                font=("arial", 12, "bold"),
            )
            DataFrameLeft.place(x=0, y=5, width=980, height=350)

            DataFrameRight = LabelFrame(
                DataFrame,
                bd=10,
                relief=RIDGE,
                padx=10,
                text="Prescription",
                font=("arial", 12, "bold"),
            )
            DataFrameRight.place(x=990, y=5, width=495, height=350)

            ############################ Button Frame #########################
            ButtonFrame = Frame(self.root, bd=10, relief=RIDGE)
            ButtonFrame.place(x=0, y=530, width=1530, height=70)

            ############################## Details Frame #########################
            DetailsFrame = Frame(self.root, bd=10, relief=RIDGE)
            DetailsFrame.place(x=0, y=600, width=1530, height=190)

            ############################## Data Frame Left #########################
            lblNameTablet = Label(
                DataFrameLeft,
                text="Name Of Tablets:",
                font=("Arial", 12, "bold"),
                padx=2,
                pady=6,
            )
            lblNameTablet.grid(row=0, column=0, sticky=W)

            comNameTablet = ttk.Combobox(
                DataFrameLeft,
                textvariable=self.NameTablets,
                font=("Arial", 12, "bold"),
                width=33,
            )


            comNameTablet.grid(row=0, column=1, padx=2, pady=6)

            lblref = Label(
                DataFrameLeft,
                textvariable=self.ref,
                font=("arial", 12, "bold"),
                text="Reference No:",
                padx=2,
                pady=6,
            )
            lblref.grid(row=1, column=0, sticky=W)
            txtref = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtref.grid(row=1, column=1)

            lblDose = Label(
                DataFrameLeft,
                font=("arial", 12, "bold"),
                text="Dose:",
                padx=2,
                pady=6,
            )
            lblDose.grid(row=2, column=0, sticky=W)
            txtDose = Entry(
                DataFrameLeft,
                textvariable=self.Dose,
                font=("arial", 13, "bold"),
                width=25,
            )
            txtDose.grid(row=2, column=1)

            lblNoOfTablets = Label(
                DataFrameLeft,
                textvariable=self.NumberTablets,
                font=("arial", 12, "bold"),
                text="No Of Tablets:",
                padx=2,
                pady=6,
            )
            lblNoOfTablets.grid(row=3, column=0, sticky=W)
            txtNoOfTablets = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtNoOfTablets.grid(row=3, column=1)

            lblLot = Label(
                DataFrameLeft,
                font=("arial", 12, "bold"),
                text="Lot:",
                padx=2,
                pady=6,
            )
            lblLot.grid(row=4, column=0, sticky=W)
            txtLot = Entry(
                DataFrameLeft,
                textvariable=self.Lot,
                font=("arial", 13, "bold"),
                width=25,
            )
            txtLot.grid(row=4, column=1)

            lblIssueDate = Label(
                DataFrameLeft,
                textvariable=self.IssueDate,
                font=("arial", 12, "bold"),
                text="Issue Date:",
                padx=2,
                pady=6,
            )
            lblIssueDate.grid(row=5, column=0, sticky=W)
            txtIssueDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtIssueDate.grid(row=5, column=1)

            lblExpDate = Label(
                DataFrameLeft,
                textvariable=self.ExpDate,
                font=("arial", 12, "bold"),
                text="Exp Date:",
                padx=2,
                pady=6,
            )
            lblExpDate.grid(row=6, column=0, sticky=W)
            txtExpDate = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtExpDate.grid(row=6, column=1)

            lblDailyDose = Label(
                DataFrameLeft,
                textvariable=self.DailyDose,
                font=("arial", 12, "bold"),
                text="Daily Dose:",
                padx=2,
                pady=6,
            )
            lblDailyDose.grid(row=7, column=0, sticky=W)
            txtDailyDose = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtDailyDose.grid(row=7, column=1)

            lblSideEffect = Label(
                DataFrameLeft,
                textvariable=self.SideEffect,
                font=("arial", 12, "bold"),
                text="Side Effect:",
                padx=2,
                pady=6,
            )
            lblSideEffect.grid(row=8, column=0, sticky=W)
            txtSideEffect = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtSideEffect.grid(row=8, column=1)

            lblFurtherInfo = Label(
                DataFrameLeft,
                textvariable=self.FurtherInformation,
                font=("arial", 12, "bold"),
                text="Futher Info:",
                padx=2,
                pady=6,
            )
            lblFurtherInfo.grid(row=9, column=0, sticky=W)
            txtFurtherInfo = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtFurtherInfo.grid(row=9, column=1)

            lblBP = Label(
                DataFrameLeft,
                font=("arial", 12, "bold"),
                text="Blood Pressure:",
                padx=50,
            )
            lblBP.grid(row=0, column=2, sticky=W)
            txtBP = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtBP.grid(row=0, column=3)

            lblStorage = Label(
                DataFrameLeft,
                textvariable=self.StorageAdvice,
                font=("arial", 12, "bold"),
                text="Storage:",
                padx=50,
            )
            lblStorage.grid(row=1, column=2, sticky=W)
            txtStorage = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtStorage.grid(row=1, column=3)

            lblMedicine = Label(
                DataFrameLeft,
                textvariable=self.DrivingUsingMachine,
                font=("arial", 12, "bold"),
                text="Medicine:",
                padx=50,
            )
            lblMedicine.grid(row=2, column=2, sticky=W)
            txtMedicine = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtMedicine.grid(row=2, column=3)

            lblPatientID = Label(
                DataFrameLeft,
                textvariable=self.PatientId,
                font=("arial", 12, "bold"),
                text="Patient ID:",
                padx=50,
            )
            lblPatientID.grid(row=3, column=2, sticky=W)
            txtPatientID = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtPatientID.grid(row=3, column=3)

            lblNHS = Label(
                DataFrameLeft,
                textvariable=self.PatientNHSNumber,
                font=("arial", 12, "bold"),
                text="NHS ID:",
                padx=50,
            )
            lblNHS.grid(row=4, column=2, sticky=W)
            txtNHS = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtNHS.grid(row=4, column=3)

            lblPatientName = Label(
                DataFrameLeft,
                textvariable=self.PatientName,
                font=("arial", 12, "bold"),
                text="Patient Name:",
                padx=50,
            )
            lblPatientName.grid(row=5, column=2, sticky=W)
            txtPatientName = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtPatientName.grid(row=5, column=3)

            lblDOB = Label(
                DataFrameLeft,
                textvariable=self.DateOfBirth,
                font=("arial", 12, "bold"),
                text="Date Of Birth:",
                padx=50,
            )
            lblDOB.grid(row=6, column=2, sticky=W)
            txtDOB = Entry(DataFrameLeft, font=("arial", 13, "bold"), width=25)
            txtDOB.grid(row=6, column=3)

            lblPatientAddress = Label(
                DataFrameLeft,
                textvariable=self.PatientAddress,
                font=("arial", 12, "bold"),
                text="Patient Address:",
                padx=50,
            )
            lblPatientAddress.grid(row=7, column=2, sticky=W)
            txtPatientAddress = Entry(
                DataFrameLeft, font=("arial", 13, "bold"), width=25
            )
            txtPatientAddress.grid(row=7, column=3)

            ############################## Data Frame Right #########################
            self.txtPrescription = Text(
                DataFrameRight,
                font=("arial", 12, "bold"),
                width=63,
                height=21,
                padx=2,
                pady=6,
            )
            self.txtPrescription.grid(row=0, column=0, sticky=W)

            ############################## Buttons #########################
            btnPrescription = Button(
                ButtonFrame,
                text="Prescription",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnPrescription.grid(row=0, column=0)

            btnPrescriptionData = Button(
                ButtonFrame,
                text="Prescription Data",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnPrescriptionData.grid(row=0, column=1)

            btnUpdate = Button(
                ButtonFrame,
                command=self.update_data,
                text="Update",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnUpdate.grid(row=0, column=2)

            btnDelete = Button(
                ButtonFrame,
                text="Delete",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnDelete.grid(row=0, column=3)

            btnClear = Button(
                ButtonFrame,
                text="Clear",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnClear.grid(row=0, column=4)

            btnExit = Button(
                ButtonFrame,
                text="Exit",
                bg="green",
                fg="white",
                font=("arial", 12, "bold"),
                width=23,
                padx=2,
                pady=6,
            )
            btnExit.grid(row=0, column=5)

            ############################## Buttons #########################
            scroll_x = ttk.Scrollbar(DetailsFrame, orient=HORIZONTAL)
            scroll_y = ttk.Scrollbar(DetailsFrame, orient=VERTICAL)
            self.hospital_table = ttk.Treeview(
                DetailsFrame,
                columns=(
                    "Name Of Tablets",
                    "Reference No",
                    "Dose",
                    "No Of Tablets",
                    "Lot",
                    "Issue Date",
                    "Exp Date",
                    "Daily Dose",
                    "Storage",
                    "NID",
                    "Patient Name",
                    "DOB",
                    "Patient Address",
                ),
                xscrollcommand=scroll_x.set,
                yscrollcommand=scroll_y.set,
            )
            scroll_x.pack(side=BOTTOM, fill=X)
            scroll_y.pack(side=RIGHT, fill=Y)

            scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
            scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

            self.hospital_table.heading("Name Of Tablets", text="Name Of Tablets")
            self.hospital_table.heading("Reference No", text="Reference No")
            self.hospital_table.heading("Dose", text="Dose")
            self.hospital_table.heading("No Of Tablets", text="No Of Tablets")
            self.hospital_table.heading("Lot", text="Lot")
            self.hospital_table.heading("Issue Date", text="Issue Date")
            self.hospital_table.heading("Exp Date", text="Exp Date")
            self.hospital_table.heading("Daily Dose", text="Daily Dose")
            self.hospital_table.heading("Storage", text="Storage")
            self.hospital_table.heading("NID", text="NID")
            self.hospital_table.heading("Patient Name", text="Patient Name")
            self.hospital_table.heading("DOB", text="DOB")
            self.hospital_table.heading("Patient Address", text="Patient Address")
            self.hospital_table["show"] = "headings"
            self.hospital_table.pack(fill=BOTH, expand=True)
            self.hospital_table.column("Name Of Tablets", width=100)
            self.hospital_table.column("Reference No", width=100)
            self.hospital_table.column("Dose", width=100)
            self.hospital_table.column("No Of Tablets", width=100)
            self.hospital_table.column("Lot", width=100)
            self.hospital_table.column("Issue Date", width=100)
            self.hospital_table.column("Exp Date", width=100)
            self.hospital_table.column("Daily Dose", width=100)
            self.hospital_table.column("Storage", width=100)
            self.hospital_table.column("NID", width=100)
            self.hospital_table.column("Patient Name", width=100)
            self.hospital_table.column("DOB", width=100)
            self.hospital_table.column("Patient Address", width=100)

            self.fetch_data()
            self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)

            ############################## Functionality Declaration  #########################
            def iPrescriptionData(self):
                if self.NameTablets.get() == "" or self.ref.get() == "":
                    messagebox.showerror("Error", "All fields are required")
                else:
                    conn = mysql.connector.connect(
                        host="localhost",
                        username="root",
                        password="root",
                        database="Mydata",
                    )
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        "insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                        (
                            self.NameTablets.get(),
                            self.ref.get(),
                            self.Dose.get(),
                            self.NumberOfTablets.get(),
                            self.Lot.get(),
                            self.IssueDate.get(),
                            self.ExpDate.get(),
                            self.DailyDose.get(),
                            self.StorageAdvice.get(),
                            self.NhcNumber.get(),
                            self.PName.get(),
                            self.DOB.get(),
                            self.PatientAddress.get(),
                        ),
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Record has been inserted")

            def update(self):
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="Mydata",
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE hospital SET Name_of_Tablets=%s, Dose=%s, Number_of_tablets=%s, Lot=%s, IssuedDate=%s, ExpDate=%s, DailyDose=%s, Storage=%s, NHC=%s, Patient_Name=%s, DOB=%s, Patient_Address=%s WHERE Ref.=%s",
                )

            def fetch_data(self):
                conn = mysql.connector.connect(
                    host="localhost",
                    username="root",
                    password="root",
                    database="Mydata",
                )
                my_cursor = conn.cursor()
                my_cursor.execute("select * from hospital")
                rows = my_cursor.fetchall()
                if len(rows) != 0:
                    self.hospital_table.delete(*self.hospital_table.get_children())
                    for i in rows:
                        self.hospital_table.insert("", END, values=i)
                    conn.commit()
                conn.close()

            def get_cursor(self, event=""):
                cursor_row = self.hospital_table.focus()
                content = self.hospital_table.item(cursor_row)
                row = content["values"]
                self.NameTablets.set(row[0])
                self.ref.set(row[1])
                self.Dose.set(row[2])
                self.NumberOfTablets.set(row[3])
                self.Lot.set(row[4])
                self.IssueDate.set(row[5])
                self.ExpDate.set(row[6])
                self.DailyDose.set(row[7])
                self.StorageAdvice.set(row[8])
                self.NhcNumber.set(row[9])
                self.PatientName.set(row[10])
                self.DateOfBirth.set(row[11])
                self.PatientAddress.set(row[12])

            def iPrescription(self):
                self.txtPrescription.insert(END, "Name of Tablets:\t\t\t" + self.NameTablets.get() + "\n")
                self.txtPrescription.insert(END, "Reference No:\t\t\t" + self.ref.get() + "\n")
                self.txtPrescription.insert(END, "Dose:\t\t\t\t" + self.Dose.get() + "\n")
                self.txtPrescription.insert(END, "Number of Tablets:\t\t" + self.NumberOfTablets.get() + "\n")
                self.txtPrescription.insert(END, "Lot:\t\t\t\t" + self.Lot.get() + "\n")
                self.txtPrescription.insert(END, "Issue Date:\t\t\t" + self.IssueDate.get() + "\n")
                self.txtPrescription.insert(END, "Exp Date:\t\t\t" + self.ExpDate.get() + "\n")
                

root = Tk()
ob = Hospital(root)
root.mainloop()
