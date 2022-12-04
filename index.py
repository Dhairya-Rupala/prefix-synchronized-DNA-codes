from tkinter import *
from tkinter import messagebox
import tkinter.font as font
import tkinter.scrolledtext as scrolledtext
global window


def create_ascii_list(message):
    ascii_list = []
    for i in message:
        ascii_list.append(ord(i))
    return ascii_list


def generate_text_from_ascii(ascii_list):
    text = []
    for i in ascii_list:
        text.append(chr(i))
    return text


class Mywindow:
    def __init__(self, window):
        titleFont = font.Font(family='Helvetica', size=25, weight='bold')
        subtitleFont = font.Font(family='Arial', size=12, weight='bold')
        labelFont = font.Font(family='Arial', size=10)
        self.taskFlag, self.msg, self.address_sequence, self.l = 0, None, None, None
        self.label_title = Label(
            window, text='DNA Storage and Security', font=titleFont)
        self.label_subtitle = Label(
            window, text='Prefix Synchronized Codes', font=subtitleFont)
        self.label_mentor = Label(
            window, text='Mentor: Dr. Manish K. Gupta', font=labelFont)
        self.label_title.place(x=200, y=50)
        self.label_subtitle.place(x=320, y=100)
        self.label_mentor.place(x=600, y=570)

        self.label1 = Label(
            window, text='Message to encode or decode', font=labelFont)
        self.label2 = Label(
            window, text='Address Sequence', font=labelFont)
        self.label3 = Label(window, text='Value of l', font=labelFont)
        self.label4 = Label(
            window, text='Please Choose the task', font=labelFont)
        self.btn1 = Button(window, text='Execute task',
                           command=self.compute, font=labelFont)
        self.input1 = scrolledtext.ScrolledText(window, undo=True, width=30,
                                                height=3)
        self.input1['font'] = ('consolas', '12')
        self.input2 = Entry()
        self.input3 = Entry()
        task = IntVar()
        self.radio1 = Radiobutton(
            window, text="Encode", variable=task, value=0, command=lambda: self.set_task(task))
        self.radio2 = Radiobutton(
            window, text="Decode", variable=task, value=1, command=lambda: self.set_task(task))
        self.label1.place(x=210, y=175)
        self.input1.place(x=430, y=175)
        self.label2.place(x=210, y=245)
        self.input2.place(x=430, y=245)
        self.label3.place(x=210, y=275)
        self.input3.place(x=430, y=275)
        self.label4.place(x=210, y=315)
        self.radio1.place(x=430, y=315)
        self.radio2.place(x=495, y=315)
        self.btn1.place(x=210, y=375)

    def set_task(self, task):
        self.taskFlag = int(task.get())

    def compute(self):
        task = self.taskFlag
        self.msg = self.input1.get("1.0", 'end-1c')
        self.address_sequence = self.input2.get()
        self.l = self.input3.get()
        n = len(self.address_sequence)
        if task != 0 and task != 1:
            messagebox._show(
                message="Please select the task")
        elif (not self.msg or not self.address_sequence):
            self.msg = None
            self.address_sequence = None
            self.l = None
            messagebox._show(
                message="Please enter valid message or address sequence")
        elif self.l. isalpha():
            self.msg = None
            self.address_sequence = None
            self.l = None
            messagebox._show(
                message="Please enter numeric value of l")
        else:
            self.l = int(self.l)
            Smap = self.generate_smap(self.l, n, self.address_sequence)
            if task == 0:
                encoded_seqs = []
                ascii_list = create_ascii_list(self.msg)
                for i in ascii_list:
                    encoded_seq = self.Encode(
                        n, self.l, self.address_sequence, i, Smap, [0, self.l])
                    encoded_seqs.append(encoded_seq)

                encoded_output = "".join(encoded_seqs)
                if hasattr(self, "label5"):
                    self.label5.destroy()
                if hasattr(self, "outTxt"):
                    self.outTxt.destroy()

                self.label5 = Label(
                    window, text=f'Encoded Message is', font=font.Font(family='Arial', size=10))
                self.label5.place(x=210, y=425)
                self.outTxt = scrolledtext.ScrolledText(window, undo=True, width=30,
                                                        height=4)
                self.outTxt['font'] = ('consolas', '12')
                self.outTxt.insert(END, encoded_output)
                self.outTxt.place(x=430, y=425)
            else:
                decoded_seqs = []
                for i in range(0, len(self.msg), self.l):
                    current_encoded_seq = self.msg[i:i+self.l]
                    if (len(current_encoded_seq) < self.l):
                        continue
                    decoded_seq = self.Decode(
                        current_encoded_seq, self.address_sequence, Smap)
                    decoded_seqs.append(decoded_seq)

                char_list = generate_text_from_ascii(decoded_seqs)

                decoded_output = "".join(char_list)

                if hasattr(self, "label5"):
                    self.label5.destroy()
                if hasattr(self, "outTxt"):
                    self.outTxt.destroy()
                self.label5 = Label(
                    window, text='Decoded Message is', font=font.Font(family='Arial', size=10))
                self.label5.place(x=210, y=425)
                self.outTxt = scrolledtext.ScrolledText(window, undo=True, width=30,
                                                        height=4)
                self.outTxt['font'] = ('consolas', '12')
                self.outTxt.insert(END, decoded_output)
                self.outTxt.place(x=430, y=425)

    def convert_ternary(self, num):
        res = ""
        while num:
            res = str(num % 3) + res
            num = num//3
        return res

    def convert_to_decimel(self, ternary):
        power = 0
        decimel = 0
        for i in ternary[::-1]:
            bit = int(i)
            decimel = decimel+(3**power)*bit
            power += 1
        return decimel

    def DNA_map(self, num):
        num = self.convert_ternary(num)
        dna_seq = ""
        for i in num:
            if i == "0":
                dna_seq += "A"
            elif i == "1":
                dna_seq += "T"
            else:
                dna_seq += "C"
        return dna_seq

    def Inv_DNA_map(self, seq):
        ternary_seq = ""
        for i in seq:
            if i == "A":
                ternary_seq += "0"
            elif i == "T":
                ternary_seq += "1"
            else:
                ternary_seq += "2"
        return self.convert_to_decimel(ternary_seq)

    def calc_diff(self, bit):
        raw_set = "ACT"
        return raw_set.replace(bit, "")

    def generate_smap(self, l, n, address_seq):
        Smap = [1]
        for i in range(1, l):
            if i < n:
                Smap.append(3**i)
            else:
                coeff = 0
                for j in range(1, n):
                    coeff = coeff + \
                        len(self.calc_diff(address_seq[j-1]))*Smap[i-j]
                Smap.append(coeff)
        return Smap

    def Encode(self, n, l, address_seq, msg, Smap, encoded_length_tup):
        if l >= n:
            t, y = 1, msg
            while y >= (len(self.calc_diff(address_seq[t-1]))*Smap[l-t]):
                y = y-len(self.calc_diff(address_seq[t-1]))*Smap[l-t]
                t = t+1
            c = y//Smap[l-t]
            d = y % Smap[l-t]

            a_t_1 = address_seq[0:t-1]
            a_t_c_plus_1 = self.calc_diff(address_seq[t-1])
            a_t_c_plus_1 = "".join(sorted(a_t_c_plus_1))[c]
            encoded_length_tup[0] = encoded_length_tup[0] + \
                len(a_t_1+a_t_c_plus_1)
            return (a_t_1+a_t_c_plus_1 +
                    self.Encode(n, l-t, address_seq, d, Smap, encoded_length_tup))
        else:
            theta_l_y = self.DNA_map(msg)
            remain_len = encoded_length_tup[1] - \
                encoded_length_tup[0]-len(theta_l_y)
            if remain_len:
                theta_l_y = "A"*remain_len + theta_l_y
            return theta_l_y

    def Decode(self, x, a, s):
        n = len(a)
        l = len(x)
        if (l < n):
            return self.Inv_DNA_map(x)
        else:
            rightString = ""
            for u in range(1, n+1):
                rightString = rightString + x[u-1]
                temp = ""

                temp = temp + a[0:u-1]

                subtractBit = a[u-1]
                differenceSet = self.calc_diff(subtractBit)
                differenceSet = ''.join(sorted(differenceSet))

                for v in range(1, len(differenceSet)+1):
                    temp = temp + differenceSet[v-1]
                    if (temp == rightString):
                        sum = 0
                        for i in range(1, u):
                            tempbit = a[i-1]
                            tempSub = self.calc_diff(tempbit)
                            A = len(tempSub)
                            sum += A*s[l-i]
                        return sum + (v-1)*s[l-u] + self.Decode(x[u:], a, s)

                    temp = temp[:-1]


if __name__ == "__main__":
    window = Tk()
    mywindow = Mywindow(window)
    window.title('Prefix Synchronized codes')
    window.geometry("800x600+10+10")
    window.mainloop()
