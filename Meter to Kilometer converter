from tkinter import *


def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)

def miles_to_km():
        user_input = label_4.get()
        int_input = float(user_input)
        final_km = int_input * 1.60934  # Conversion factor from miles to kilometers
        print(final_km)
        placeholder.config(text=final_km)




#window
window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=300, height=200)
window.config(padx=20, pady=20)

#label for is equal
label_1 = Label(text= 'is equal to ', font=('Arial', 24))
label_1.grid(column=1,row=1)

#label for km
label_2 = Label(text= 'km', font=('Arial', 24))
label_2.grid(column=3,row=1)

#label for miles
label_3 = Label(text= 'Miles', font=('Arial', 24))
label_3.grid(column=3,row=0)


#label for calculation output
label_4 = Entry(width=5)
label_4.grid(column=2,row=0)

#create button
button = Button(text='Convert', command=miles_to_km)
button.grid(column=2,row=2)



placeholder = Label(text='0')
placeholder.grid(column=2,row=1)








window.mainloop()
    
