def fetch_data():
    import tkinter as tk
    from tkinter import ttk,messagebox
    import csv
    import os
    from PIL import Image, ImageTk
    from main import record
    import time
    name_dict = {
        # Name dictionary entries...
        
        '2451-20-733-121': 'Rampuri Shiva Sai',
        '2451-20-733-122': 'Namani Chandrababu',
        '2451-20-733-123': 'Pasunuri Shreyanth',
        '2451-20-733-124': 'D.V.S.Siva Datta',
        '2451-20-733-125': 'Nune Nikhil Teja',
        '2451-20-733-127': 'B.Siddardha',
        "2451-20-733-128": 'Regu Gowthami',
        '2451-20-733-129': 'A. Partha Sai',
        '2451-20-733-130': 'Vasam Priyanka',
        '2451-20-733-131': 'Mamidi Vishnu Priya',
        '2451-20-733-132': 'D Mohammad Saquib',
        '2451-20-733-133': 'Kadaboina Rohit Kumar',
        '2451-20-733-134': 'Gangavaram Sai Teja',
        '2451-20-733-135': 'Kannemolla Santhosh Kumar',
        '2451-20-733-136': 'Seshadri Samuel',
        '2451-20-733-137': 'Jatavath Jayanth',
        '2451-20-733-138': 'Kommu Selina',
        '2451-20-733-139': 'Meharaj Fatima',
        '2451-20-733-140': 'Maroju Shiva',
        '2451-20-733-141': 'Prathyusha Chitimalla',
        '2451-20-733-142': 'Gampala Dheeraj Kumar',
        '2451-20-733-143': 'Aalla Chandrika',
        '2451-20-733-144': 'Jakku Dhruv Arjun Reddy',
        '2451-20-733-145': 'Vadde Akshay Raj',
        '2451-20-733-146': 'Kondapaka Gideon Jayaraj',
        '2451-20-733-147': 'Singam Sanjay',
        '2451-20-733-148': 'Samreddy Shiva Kumar Reddy',
        '2451-20-733-149': 'T Tarunika',
        '2451-20-733-150': 'Nalla Snehal Reddy',
        '2451-20-733-151': 'Chittaluri Ravi Teja Sonu',
        '2451-20-733-152': 'Thimirshetty Karthikeya',
        '2451-20-733-153': 'Jeniga Balu Yadav',
        '2451-20-733-154': 'Tupili Sai Nikhil',
        '2451-20-733-155': 'Aasritha Gongireddy',
        '2451-20-733-156': 'V Akanksha',
        '2451-20-733-157': 'B Shreyas',
        '2451-20-733-158': 'Mohammad Zohaib',
        '2451-20-733-159': 'Mandadi Rohit Reddy',
        '2451-20-733-160': 'B Deepika',
        '2451-20-733-161': 'Puranam Alekhya',
        '2451-20-733-162': 'Mohammed Rafae Ahmed',
        '2451-20-733-163': 'Surya Danturty',
        '2451-20-733-164': 'Vanjivakam Srimanth Teja',
        '2451-20-733-165': 'Hetalee Pravin Warad',
        '2451-20-733-166': 'Bokka Sai Mahathma Reddy',
        '2451-20-733-167': 'Dumpala Govindchakri',
        '2451-20-733-168': 'P Karan',
        '2451-20-733-169': 'Velimineti Sai Sushanth Reddy',
        '2451-20-733-170': 'Akavaram Shobitha',
        '2451-20-733-171': 'Gangoni Sushanth',
        '2451-20-733-172': 'Adluri Dikshithaa',
        '2451-20-733-173': 'Immadi Mahendra Sai Pavan',
        '2451-20-733-174': 'Bejugam Nagendra',
        '2451-20-733-175': 'Jyothi',
        '2451-20-733-176': 'Kotte Akhilesh',
        '2451-20-733-177': 'Kasanagottu Vivek',
        '2451-20-733-178': 'Kasukurthy Pranay Kumar',
        '2451-20-733-179': 'Lingam Soumith Reddy',
        '2451-20-733-180': 'Chandupatla Vikas Reddy',
        '2451-20-733-313': 'S Navya Sri',
        '2451-20-733-314': 'Mohd Asim Hussain',
        '2451-20-733-315': 'Konyala Krishna Vardhan Reddy',
        '2451-20-733-316': 'Ashwini Borra',
        '2451-20-733-317': 'Donthula Manusha',
        '2451-20-733-318': 'R Srihitha',
        '2452-20-733-018': 'Sathwik Dontha',
        'Roll Number':'Name of the Student'
    }
    
    def update_attendance():
        # Rest of the code...
        with open('Attendance.csv', 'r') as file:
            reader = csv.reader(file)
            data = list(reader)

        tree.delete(*tree.get_children())

        # Insert new data from the CSV file into the Treeview
        for i, row in enumerate(data, 1):
            tree.insert('', 'end', values=(i,) + tuple(row))

        # Get the last added name
        last_added_name = data[-1][0] if data else ''

        # Update the label with the last added name
        name_label.config(text=format_student_details(name_dict[last_added_name], last_added_name))

        # Select the last row in the Treeview
        tree.selection_set(tree.get_children()[-1])
        # Load and display the image
        image_path = 'D:/faces/{}.jpg'.format(last_added_name)
        image = Image.open(image_path)
        image = image.resize((300, 300))  # Adjust the size as per your requirements
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo,relief='solid',borderwidth=2)
        image_label.image = photo  # Keep a reference to prev
        messagebox.showinfo('information','Your Attendance is marked!\nPress key [esc] to return')
        

        # Add image
        
    def detect_file_change():
        # Rest of the code...
        modified_time = os.path.getmtime('Attendance.csv')

        if modified_time > detect_file_change.last_modified_time:
            update_attendance()  # Update the attendance in the GUI
            detect_file_change.last_modified_time = modified_time
        clock.config(text=time.strftime("Date: %d-%m-%Y\nTime: %I:%M:%S"),background='light steel blue')
        window.after(1000, detect_file_change)
    # Create the GUI window
    window = tk.Tk()
    window.title("Attendance Recording System")
    window.geometry("1500x1000")
    window['bg']='light steel blue'
    # img =Image.open('Image.jpg')
    # bg = ImageTk.PhotoImage(img)
    # label = tk.Label(window, image=bg)
    # label.place(x = 0,y = 0)
    clock = tk.Label(window, background = 'white',foreground = 'black', font = ('arial', 25, 'bold'),justify='left')
    style = ttk.Style()
    style.configure("Custom.Treeview", font=('Arial', 15))
    # Create a Treeview widget
    tree = ttk.Treeview(window, columns=('No.', 'Name', 'Time','Date'), show='headings',style='Custom.Treeview')
    # Rest of the code...

    # Create a label to display the last added name
    #name_label = tk.Label(window, text='Student Details' , font=('Arial', 30), background='#3498db', fg='white')
    # Rest of the code...
    name_label = tk.Label(window,font=('Arial', 25), background='deep sky blue', fg='black',justify='left',relief='solid',borderwidth=5)
    atten_name = tk.Label(window,text='Attendance System', font=('Arial',20),fg='black',relief='solid', borderwidth=5)
    # name_label.grid(row=2, column=0, padx=0, pady=( 20), sticky='w')
    # Create a label to display the image
    def format_student_details(name, roll_no):
        formatted_text = "Name    : {}\n".format(name)
        formatted_text += "Roll No  : {}\n".format(roll_no)
        formatted_text += "Branch  : CSE\n"
        formatted_text += "Section  : C"
        return formatted_text
    image_label = tk.Label(window, background='#34495e')
    # Rest of the code...

    # Create a button to run the hello() function
    button = tk.Button(window, text="Take Attendance", command=record,background='green2',font=('Arial',20,'bold'),fg='black',relief='solid',borderwidth=4)
    # Rest of the code...

    # Rest of the code...
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    # Grid layout configuration
    atten_name.grid(row=0, column=0,sticky='n',pady=20)
    image_label.grid(row=0, column=0, padx=2, pady=0)
    student_details_label = ttk.Label(window, text="Student Details:", font=('Arial', 15, 'bold'), padding=(10, 10),background='misty rose')
    student_details_label.grid(row=0, column=0, padx=5, pady=2, sticky='s')
    name_label.grid(row=1, column=0, padx=5,sticky='s')
    # window.grid_rowconfigure(0, weight=0)
    tree.grid(row=0, column=1, sticky='ewns')
    # tree.place(relx=0.8, rely=0.8, anchor=tk.CENTER, relwidth=0.4, relheight=0.4)
    # Set row 1 weight to 1, so it takes the remaining vertical space
    # window.grid_rowconfigure(1, weight=1)
    button.grid(row=2, column=0, padx=20, pady=20)
    clock.grid(row=3, column=0, columnspan=3, padx=100, pady=3, sticky='w')
    # tree.grid(row=0, column=1, sticky='nsew')
    # button.grid(row=2, column=0, padx=20,pady=20)
    # clock.grid(row=3, column=0, columnspan=3, padx=100, pady=3,sticky='w')
    # Rest of the code...
   
    detect_file_change.last_modified_time = os.path.getmtime('Attendance.csv')

    # Update the attendance initially
    update_attendance()

    # Start detecting file changes
    detect_file_change()

    # Start the GUI main loop
    window.mainloop()

fetch_data()