from cmath import sqrt
import tkinter as tk
from sympy import *

LARGE_FONT_STYLE = ("Times New Roman", 20)
SMALL_FONT_STYLE = ("Times New Roman", 16)
DIGITS_FONT_STYLE = ("Times New Roman", 24, "bold")
DEFAULT_FONT_STYLE = ("Times New Roman", 15)
LABEL_FONT_STYLE = ("Times New Roman", 15)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1,1), 8: (1,2), 9: (1,3),
            4: (2,1), 5: (2,2), 6: (2,3),
            1: (3,1), 2: (3,2), 3: (3,3),
            0: (4,2), '.': (4,1),  ',': (4,3)
            }
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_special_buttons()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_cartesian_to_cylindrical_button()
        self.create_cartesian_to_spherical_button()
        self.create_cylindrical_to_cartesian_button()
        self.create_cylindrical_to_spherical_button()
        self.create_spherical_to_cylindrical_button()
        self.create_spherical_to_cartesian_button()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame,text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=2, sticky=tk.NSEW)

    def cartesian_to_cylindrical(self):
        car = self.current_expression.split(",")
        x = int(car[0])
        y = int(car[1])
        z = car[2]
        r = ((x**2) + (y**2))**(1/2)
        phi = atan(y/x)*57.2958
        self.current_expression ="Cartesian To Cylindrical\n"\
                                  +"x,y,z:\t"+self.current_expression + "\n\u03C1,\u03B8,z:\t"\
                                  + str(round(r,2))+", "+ str(round(phi,2))+ "\u00B0, "+z+"\n"
        self.update_label()

    def cartesian_to_spherical(self):
        car = self.current_expression.split(",")
        x = int(car[0])
        y = int(car[1])
        z = int(car[2])
        r = ((x**2) + (y**2) + (z**2))**(1/2)
        phi = atan(y/x)*57.2958
        theta = acos(z/r)*57.2958
        self.current_expression = "Cartesian to Spherical\n"\
                                  +"x,y,z:\t"+self.current_expression + \
                                  "\nr,\u03C1,\u03C6:\t"+str(round(r,2))+ \
                                  ", "+str(round(phi,2))+ "\u00B0, "+ str(round(theta,2))[:5]+"\u00B0\n"
        self.update_label()

    def create_cartesian_to_cylindrical_button(self):
        button = tk.Button(self.buttons_frame, text="Cartesian to\ncylindrical", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE,
                           borderwidth=0, command=self.cartesian_to_cylindrical)
        button.grid(row=1, column=4, sticky=tk.NSEW)

    def create_cartesian_to_spherical_button(self):
        button = tk.Button(self.buttons_frame, text="Cartesian to\nspherical", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE,
                           borderwidth=0, command=self.cartesian_to_spherical)
        button.grid(row=2, column=4, sticky=tk.NSEW)

    def cylindrical_to_cartesian(self):
        cyl = self.current_expression.split(",")
        self.current_expression = cyl[0]+", "+cyl[1]+"\u00B0, "+cyl[2]
        r = int(cyl[0])
        phi = int(cyl[1])*0.0174533
        z = int(cyl[2])
        x = r*cos(phi)
        y = r*sin(phi)
        self.current_expression = "Cylindrical to Cartesian\n" + \
                                  "\u03C1,\u03B8,z:\t"+ self.current_expression+\
                                  "\nx,y,z:\t"+str(round(x,2))+ \
                                  ", "+ str(round(y,2))+ ", "+ str(round(z, 2))+"\n"
        self.update_label()

    def create_cylindrical_to_cartesian_button(self):
        button = tk.Button(self.buttons_frame, text="Cylindrical to\ncartesian", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE,
                            borderwidth=0, command=self.cylindrical_to_cartesian)
        button.grid(row=3, column=4, sticky=tk.NSEW)
        
    def cylindrical_to_spherical(self):
        cyl = self.current_expression.split(",")
        self.current_expression = cyl[0]+", "+cyl[1]+"\u00B0, "+cyl[2]
        rho = int(cyl[0])
        theta = int(cyl[1])
        z = int(cyl[2])
        r = ((rho**2)+(z**2))**(1/2)
        phi = atan(rho/z)*57.2958
        self.current_expression ="Cylindrical to Spherical\n"+\
                                  "\u03C1,\u03B8,z:\t"+ self.current_expression+\
                                  "\nr,\u03C1,\u03C6:\t"+str(round(r,2))+ \
                                  ", "+str(round(theta,2))+ "\u00B0, "+ str(round(phi,2))[:5]+"\u00B0\n"
##                                str(round(r,2))+ ", "+ str(round(theta,2))+ ", "+ str(round(phi,2))
        self.update_label()

    def create_cylindrical_to_spherical_button(self):
        button = tk.Button(self.buttons_frame, text="Cylindrical to\nspherical", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE,
                            borderwidth=0, command=self.cylindrical_to_spherical)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def spherical_to_cylindrical(self):
        spe = self.current_expression.split(",")
        self.current_expression = spe[0]+", "+spe[1]+"\u00B0, "+spe[2]+"\u00B0"
        r = int(spe[0])
        theta = int(spe[1])
        phi = int(spe[2])*0.0174533
        rho = r*sin(phi)
        z = r*cos(phi)
        self.current_expression = "Spherical to Cylindrical\n"+\
                                  "r,\u03C1,\u03C6:\t"+self.current_expression+\
                                  "\n\u03C1,\u03B8,z:\t" +\
                                  str(round(rho,2))+ ", "+ str(round(theta,2))+"\u00B0, "+ str(round(z,2))+"\n"
        self.update_label()

    def create_spherical_to_cylindrical_button(self):
        button = tk.Button(self.buttons_frame, text="Spherical to\nCylindrical", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE, 
                            borderwidth=0, command=self.spherical_to_cylindrical)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def spherical_to_cartesian(self):
        spe = self.current_expression.split(",")
        self.current_expression = spe[0]+", "+spe[1]+"\u00B0, "+spe[2]+"\u00B0"
        r = int(spe[0])
        theta = int(spe[1])*0.01745
        phi = int(spe[2])*0.01745
        x = r*sin(phi)*cos(theta)
        y = r*sin(phi)*sin(theta)
        z = r*cos(phi)
        self.current_expression = "Spherical to Cartesian\n"+\
                                  "r,\u03C1,\u03C6:\t"+self.current_expression+\
                                  "\nx,y,z:\t"+\
                                str(round(x,2))+ ", "+ str(round(y,2))+ ", "+ str(round(z,2))+"\n"
        self.update_label()

    def create_spherical_to_cartesian_button(self):
        button = tk.Button(self.buttons_frame, text="Spherical to\nCartesian", bg=OFF_WHITE, fg=LABEL_COLOR, font=LABEL_FONT_STYLE,
                            borderwidth=0, command=self.spherical_to_cartesian)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
    









        
