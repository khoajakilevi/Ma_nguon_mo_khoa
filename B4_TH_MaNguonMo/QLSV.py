from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

root = Tk()
root.title("Hệ thống quản lý sinh viên")
root.geometry("1200x800")

# # Kết nối tới db
# conn = sqlite3.connect('Student_book.db')
# c = conn.cursor()

# #Tao bang de luu tru
# c.execute('''
#     CREATE TABLE students(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         first_name text,
#         last_name text,
#         class_id text,
#         yearEnrolled interger,
#         average_score interger
#     )
# '''
# )

def them():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('Student_book.db')
    c = conn.cursor()
    #lấy dữ liệu đã nhập
    name_value = f_name.get()
    lastname_value = l_name.get()
    class_id_value = class_id.get()
    yearEnrolled_value = yearEnrolled.get()
    average_score_value = average_score.get()
    #thực hiện câu lệnh thêm
    c.execute('''
        INSERT INTO 
        students (first_name, last_name, class_id, yearEnrolled, average_score)
        VALUES 
        (:name, :last_name, :class_id,:yearEnrolled, :average_score)
    ''',{
        'name' : name_value,
        'last_name' : lastname_value,
        'class_id': class_id_value,
        'yearEnrolled': yearEnrolled_value,
        'average_score': average_score_value
      }
    )
    conn.commit()
    conn.close()

    # Reset form
    f_name.delete(0, END)
    l_name.delete(0, END)
    class_id.delete(0, END)
    yearEnrolled.delete(0, END)
    average_score.delete(0, END)


    # Hien thi lai du lieu
    truy_van()
def xoa():
    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('Student_book.db')
    c = conn.cursor()
    #lấy dữ liệu đã nhập
    f_id_delete = delete_box.get()
    
    #kiểm tra xem ID có tồn tại trong cơ sở dữ liệu
    c.execute(''' 
        SELECT id FROM students
        WHERE id = :id
    ''', {'id': f_id_delete})
    records = c.fetchall()
    if not records:
        #nếu không có trong danh sách thì xuất hiện thông báo không tìm thấy
        messagebox.showinfo("Thông báo", "không tìm thấy bản ghi bạn cần tìm, mời nhập lại")
    else:
        c.execute('''
            DELETE FROM students
            WHERE id = :id
        ''', {'id' : f_id_delete})
        conn.commit()
 
        # Hiên thi thong bao
        messagebox.showinfo("Thông báo", "Đã xóa!")
    delete_box.delete(0,END)
    conn.close()
    # Hiển thị lại dữ liệu
    truy_van()

def truy_van():
    # Xóa đi các dữ liệu trong TreeView
    for row in tree.get_children():
        tree.delete(row)

    # Kết nối và lấy dữ liệu
    conn = sqlite3.connect('Student_book.db')
    c = conn.cursor()
    c.execute("SELECT * FROM students")
    records = c.fetchall()

    # Hien thi du lieu
    for r in records:
        tree.insert("", END, values=(r[0], r[1], r[2], r[3], r[4], r[5]))

    # Ngat ket noi
    conn.close()
def chinh_sua():
    global editor
    editor = Tk()
    editor.title('Cập nhật bản ghi')
    editor.geometry("400x300")
    #truy cập dữ liệu SQLite
    conn = sqlite3.connect('Student_book.db')
    c = conn.cursor()
    record_id = delete_box.get()
    c.execute("SELECT * FROM students WHERE id=:id", {'id':record_id})
    records = c.fetchall()

    global f_id_editor, f_name_editor, l_name_editor, class_id_editor, yearEnrolled_editor, average_score_editor
    #Khung nhập dữ liệu
    f_id_editor = Entry(editor, width=30)
    f_id_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20)
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1)
    class_id_editor = Entry(editor, width=30)
    class_id_editor.grid(row=3, column=1)
    yearEnrolled_editor = Entry(editor, width=30)
    yearEnrolled_editor.grid(row=4, column=1)
    average_score_editor = Entry(editor, width=30)
    average_score_editor.grid(row=5, column=1)

    #nhãn dán
    f_id_label = Label(editor, text="ID")
    f_id_label.grid(row=0, column=0, pady=(10, 0))
    f_name_label = Label(editor, text="Họ")
    f_name_label.grid(row=1, column=0)
    l_name_label = Label(editor, text="Tên")
    l_name_label.grid(row=2, column=0)
    class_id_label = Label(editor, text="Mã Lớp")
    class_id_label.grid(row=3, column=0)
    yearEnrolled_label = Label(editor, text="Năm nhập học")
    yearEnrolled_label.grid(row=4, column=0)
    average_score_label = Label(editor, text="Điểm trung bình")
    average_score_label.grid(row=5, column=0)

    for record in records:
        f_id_editor.insert(0, record[0])
        f_name_editor.insert(0, record[1])
        l_name_editor.insert(0, record[2])
        class_id_editor.insert(0, record[3])
        yearEnrolled_editor.insert(0, record[4])
        average_score_editor.insert(0, record[5])

    edit_btn = Button(editor, text="Lưu bản ghi", command=cap_nhat)
    edit_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

def cap_nhat():
    conn = sqlite3.connect('Student_book.db')
    c = conn.cursor()
    record_id = f_id_editor.get()

    c.execute("""UPDATE students SET
           first_name = :first,
           last_name = :last,
           class_id = :class_id,
           yearEnrolled = :yearEnrolled,
           average_score = :average_score
           WHERE id = :id""",
              {
                  'first': f_name_editor.get(),
                  'last': l_name_editor.get(),
                  'class_id': class_id_editor.get(),
                  'yearEnrolled': yearEnrolled_editor.get(),
                  'average_score': average_score_editor.get(),
                  'id': record_id
              })

    conn.commit()
    conn.close()
    editor.destroy()

    # Cập nhật lại danh sách bản ghi sau khi chỉnh sửa
    truy_van()

def chon(event):
    # Lấy thông tin bản ghi được chọn
    ID_object = tree.focus() #lấy ID của hàng (đây là ID của hệ thống không phải ID của mình)
    ID_value = tree.item(ID_object, 'values')# lấy tất cả giá trị của hàng dựa vào ID của hàng gồm: ID của mình, Họ , Tên, TP
    
    # Cập nhật ID của bản ghi vào delete_box
    if ID_value:
        delete_box.delete(0, END) #tạo lại form
        delete_box.insert(0, ID_value[0])  # ID nằm ở đầu vì mình thiết kế vậy chứ không có bắt buộc





# Khung cho các ô nhập liệu
input_frame = Frame(root)
input_frame.pack(pady=10)

# Các ô nhập liệu cho cửa sổ chính
f_name = Entry(input_frame, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
l_name = Entry(input_frame, width=30)
l_name.grid(row=1, column=1)
class_id = Entry(input_frame, width=30)
class_id.grid(row=2, column=1)
yearEnrolled = Entry(input_frame, width=30)
yearEnrolled.grid(row=3, column=1)
average_score = Entry(input_frame, width=30)
average_score.grid(row=4, column=1)


# Các nhãn
f_name_label = Label(input_frame, text="Họ")
f_name_label.grid(row=0, column=0, pady=(10, 0))
l_name_label = Label(input_frame, text="Tên")
l_name_label.grid(row=1, column=0)
class_id_label = Label(input_frame, text="Mã lớp")
class_id_label.grid(row=2, column=0)
yearEnrolled_label = Label(input_frame, text="Năm nhập học")
yearEnrolled_label.grid(row=3, column=0)
average_score_label = Label(input_frame, text="Điểm trung bình")
average_score_label.grid(row=4, column=0)

# Khung cho các nút chức năng
button_frame = Frame(root)
button_frame.pack(pady=10)

# Các nút chức năng
submit_btn = Button(button_frame, text="Thêm bản ghi", command=them)
submit_btn.grid(row=0, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
query_btn = Button(button_frame, text="Hiển thị bản ghi", command=truy_van)
query_btn.grid(row=1, column=0, columnspan=2, pady=10, padx=10, ipadx=137)
delete_box_label = Label(button_frame, text="Chọn ID để xóa")
delete_box_label.grid(row=2, column=0, pady=5)
delete_box = Entry(button_frame, width=30)
delete_box.grid(row=2, column=1, pady=5)
delete_btn = Button(button_frame, text="Xóa bản ghi", command=xoa)
delete_btn.grid(row=3, column=0, columnspan=2, pady=10, padx=10, ipadx=136)
edit_btn = Button(button_frame, text="Chỉnh sửa bản ghi", command=chinh_sua)
edit_btn.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=125)

# Khung cho Treeview
tree_frame = Frame(root)
tree_frame.pack(pady=10)

# Treeview để hiển thị bản ghi
columns = ("ID", "Họ", "Tên", "Mã lớp", "Năm nhập học", "Điểm trung bình")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=15)
tree.pack()

# Gọi hàm này khi người dùng chọn bản ghi trong Treeview
tree.bind("<<TreeviewSelect>>", chon)

# Định nghĩa tiêu đề cho các cột
for col in columns:
    tree.heading(col, text=col)

# Gọi hàm truy vấn để hiển thị bản ghi khi khởi động
truy_van()

root.mainloop()