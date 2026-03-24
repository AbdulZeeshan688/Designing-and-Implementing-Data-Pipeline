import sqlite3

# bas database se kaam karne ke liye yeh import kiya

# -------------------------------------------
# yeh poora function hai jo sab kuch karta hai
# login bhi, result bhi, sab kuch yahan hai
# -------------------------------------------
def login_and_get_credits():

    # pehle user se naam aur birthday lo
    # birthday hi password hai hamare system mein
    print("====== Student Portal ======")
    username = input("INSERT THE USERNAME ")
    password = input("INSERT THE PASSWORD (BIRTHDAY): ")

    # database kholo
    # schools.db wahi file hai jisme sab students ka data pada hai
    conn = sqlite3.connect('schools.db')
    cursor = conn.cursor()

    # ab check karo ke yeh banda actually exist karta hai ya nahi
    # ? isliye use kiya taake koi hacker SQL se tamper na kar sake
    # yeh ek safe tarika hai values pass karne ka
    login_query = """
        SELECT id, name FROM Students 
        WHERE name = ? AND birthday = ?
    """
    cursor.execute(login_query, (username, password))
    user = cursor.fetchone()
    # agar banda mila toh user mein data hoga
    # agar nahi mila toh None aayega

    # agar login sahi tha
    if user:

        # user[0] matlab pehli cheez jo mili yaani id
        # user[1] matlab doosri cheez yaani naam
        student_id = user[0]
        student_name = user[1]

        print(f"\n YOU ARE LOGGED IN, WELCOME {student_name}")

        # ab is student ke saare courses dhundo
        # teen tables hain jo ek doosre se judi hain
        # Students → creditst → Course
        # LEFT JOIN isliye ke agar koi course nahi hai tab bhi error na aaye
        credits_query = """
            SELECT Course.name, creditst.credits, creditst.grade, creditst.date
            FROM Students
            LEFT JOIN creditst ON creditst.id_student = Students.id
            LEFT JOIN Course ON creditst.id_course = Course.id
            WHERE Students.id = ?
        """
        cursor.execute(credits_query, (student_id,))
        rows = cursor.fetchall()
        # fetchall matlab sab rows ek saath le aao list mein

        # ab results print karo agar kuch mila
        if rows and rows[0][0] is not None:
            # rows[0][0] check kiya taake pata chale ke course naam actually hai
            # sirf empty row toh nahi aayi
            print("\nYOUR COURSES ARE:")
            print("---------------------------")

            for row in rows:
                # har row mein 4 cheezein hain
                # course ka naam, credits, grade aur date
                course_name, credits, grade, date = row
                print(f"course: {course_name} | grade: {grade} | credits: {credits} | date: {date}")

            print("---------------------------")

        else:
            # matlab koi course abhi tak enroll nahi hua
            print("\nNO COURSES TILL NOW ")

    else:
        # matlab naam ya birthday galat thi
        print("\nLOGIN FAILED, PLEASE CHECK YOUR NAME OR BIRTHDAY")

    # database band karo
    # yeh important hai warna connection open rehta hai
    conn.close()


# program yahan se start hota hai
# seedha function call kar diya
login_and_get_credits()