from django.shortcuts import render
from django.http import HttpResponse
from .models import University, Faculty ,Course, Teacher, Student
from django.shortcuts import get_object_or_404
from .models import Course, Teacher, Student

# Create your views here.

"""
    reveres -  reverse relationni umumiy manosi ota modeldan bollaridan turib malumotni bemalol olish
    distinct() - bu method querysetdagi takroriy elementlarni olib tashlaydi, ya'ni har bir element faqat bir marta chiqadi.
    <li> - bu HTML da ruyxat ligini bildiradigan teg
    <or> - bu ordered list yani tartiblangan ruyxat
    <ul> - bu unordered list yani tartiblanmagan ruyxat
    <hr> - bu horizontal line yani gorizontal chiziq
    <p> - bu HTML da paragrafni bildiradi
    <br> - bu HTML da yangi qatorga o'tish uchun ishlatiladi, bu yerda <br> ni ishlatishimning sababi o'qituvchilar va talabalar orasida kichik bo'shliq yaratish uchun ishlatdim
    < a href > </a> bu HTML da link yaratish
    strftime() - bu method datetime obyektini stringga aylantirish uchun ishlatiladi, bu yerda %d kun, %m oy, %Y yilni bildiradi va ularni istalgan tartibda joylashtirish mumkin
    
    get_object_or_404 - bu Django shortcut funksiyasi, u modeldan ma'lumotni olishga harakat qiladi, agar ma'lumot topilmasa 404 xato sahifasini ko'rsatadi. Bu foydalanuvchi tajribasini yaxshilaydi va saytning xavfsizligini oshiradi.
    faculty__university - bu yerda __ bu Django zanjirli filtirlash sintaksisi ana shu meni ishimni osonlashtirdi chunki student modelida university maydoni yo'q,
    u faqat facultyga bog'langan. Lekin menga  universitetdagi  hamma studentlar kerak. faculty__university (ikkita pastki chiziq) yordamida men hammasini bemalol olaman va foydalanaman

"""










def university_list(request):

    """Barcha universitetlar ro'yxatini chiqarish,
       har bir universitet nomi ustiga bosilganda uning sahifasiga o'tishini bulsa pastdagi sikl
       taminlaydi unda href deyilganda har safar nomi uzgarishi yozilgan yani har bir universitet uchun alohida link hosil qiladi
       va shu link bilan o'sha universitet sahifasiga o'tadi,
    bu sikl ni uzim qildi lekin ustoz"""


    universities = University.objects.all()
    all_universities = ""
    for un in universities:
        all_universities += (f" <li>  <a href='/universities/{un.id}/'>{un.name}</a> "
                             f"</li>")              # un.id universitetning id sini olish uchun yozdim chunki url da shunday yozilgan va o'sha id ga mos sahifaga o'tadi
                                                    # un.name bulsa usha url ni hunuk emas nomini kursatib turadi yani Masalan : Moliya yozilgan  tursa aslida url bulsa /universities/1/


    html = f"""
        <h1>University List</h1>
        <ol>{all_universities}</ol>
    """

    return HttpResponse(html)


def university_detail(request, university_id):

    """
    Agar men oddiy .get() ishlatsam va
     user mavjud bo'lmagan id raqamini (masalan, bazada yo'q universitetni , yoki umuman) qidirsa,
     saytimiz srazu xato berib, 'portlab' ketadi (Server Error 500) hehe buni hohlamaymadi hech kim
     get_object_or_404 esa ancha aqlli usul ekan: u bazadan ma'lumotni qidiradi, topolmasa saytni portlatib yubormasdan
     userga chiroyli qilib 'Bunday ma'lumot topilmadi' (404 Error) degan xabarni aytadi user qurqib ketmasin .
     Bu userni experience si va security uchun very necessary."
    """


    university = get_object_or_404(University, id=university_id)

    # strftime bilan sanani chiroyli formatda (KUN.OY.YIL) chiqardim, bui ai dan urgandim bunda day - %d, month - %m, year - %Y ni anglatadi shuni joyini almashtirib uzimga keragini oalaman
                                                                                                                        # masalan %Y.%m.%d yozsam yil.oy.kun formatida chiqadi buni ai tuliq tushuntirdi va buni import ham qilsh kerak emas
    beautiful_dat = university.created_at.strftime("%d.%m.%Y")
    faculties = Faculty.objects.filter(university=university)

    all_faculties = ""
    for fac in faculties:
        all_faculties += f"<li><a href='/faculties/{fac.id}/'>{fac.name}</a></li>"


    html = f"""
        <h1>{university.name}</h1>
        <p>Capacity: {university.capacity_students}</p>
        <p>Created at: {beautiful_dat}</p>
        <a href='/universities/{university.id}/teachers/'>View Teachers</a><br>
        <a href='universities/{university.id}/students/'>View Students</a><br>
        <h3>Faculties:</h3>
        <ul>{all_faculties}</ul>
        <p><b>Total Faculties:</b> {faculties.count()}</p>
        <hr>
        <a href='/universities/'>Back to University List</a>
    """
    return HttpResponse(html)


def faculty_detail(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    courses = Course.objects.filter(faculty=faculty)

    all_courses = ""
    for course in courses:
        all_courses += f"<li><a href='/courses/{course.id}/'>{course.name}</a></li>"

    html = f"""
        <h1>{faculty.name} fakulteti</h1>
        <p><b>University:</b> {faculty.university.name}</p>
        <a href='/faculties/{faculty_id}/students/'>View Students</a><br>
        <h3>Courses:</h3>
        <ul>{all_courses}</ul>
        <p><b>Total Courses:</b> {courses.count()}</p>
        <hr>
        <a href='/universities/{faculty.university.id}/'>Back to University</a>
    """
    return HttpResponse(html)


def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    teachers = course.teachers.all()
    all_teachers = "".join([f"<li>{t.name} (Age: {t.age})</li>" for t in teachers]) or "O'qituvchilar belgilanmagan"
    students = course.students.all() # join methodi osson str ga biror nima qushish

    all_students = "".join([f"<li>{s.name}</li>" for s in students]) or "Talabalar mavjud emas" # list comprehension yordamida talabani chiroyli qilib yozish

    # or quyganim sababi esimga tushdi or operatori ikkalasidan biri true bulsa gina ishlaydi yani u xato bulsa gina ushanda bu ishlaydi
    # yani oquvchi hali qushilmagan bulsa


    html = f"""                                              
        <h1>{course.name} kursi</h1>
        <p><b>Faculty:</b> {course.faculty.name}</p>
        <p><b>University:</b> {course.faculty.university.name}</p>
        <h3>Teachers:</h3>
        <ol>{all_teachers}</ol>
        <h3>Students:</h3>
        <ol>{all_students}</ol>
        <p><b>Total Students:</b> {students.count()}</p>
        <hr>
        <a href='/faculties/{course.faculty.id}/'>Back to Faculty</a>
    """
    return HttpResponse(html)


def university_teachers(request, university_id):
    university = get_object_or_404(University, id=university_id)
    teachers = Teacher.objects.filter(courses__faculty__university=university).distinct()

    """
Bu yerda men 'zanjirli filtrlash' qilshni urgandim . 
Student modelida to'g'ridan-to'g'ri university maydoni yo'q,
u faqat facultyga bog'langan. Lekin menga  universitetdagi  hamma studentlar kerak.
faculty__university (ikkita pastki chiziq) yordamida men Djangoga: 
'Studengting fakultetiga kir, keyin o'sha fakultet qaysi universitetga tegishli ekanligini tekshir' dedim. 
Bu database ga murakkab SQL so'rovini yozmasdan, bitta qatorda uzoqdagi ma'lumotni filterlab olish imkonini beradi.
Bularni hammasini ai dan urgandim hatto distinct() ni ham ai dan urgandim chunki bu yerda bir o'qituvchi bir nechta kursga bir universitetda tegishli bo'lishi mumkin,
shuning uchun distinct() yordamida takroriy o'qituvchilarni chiqarib tashladim, bu esa natijani kamaytiradi 
    """

    teacher_list = "".join([f"<li>{t.name} (Fanlari: {t.courses.count()} ta)</li>" for t in teachers])

    html = f"""
        <h1>{university.name} o'qituvchilari</h1>
        <ul>{teacher_list or "O'qituvchilar hali yo'q"}</ul>
        <hr>
        <a href='/universities/{university_id}/'>Back</a>
    """

    return HttpResponse(html)


def faculty_students(request, faculty_id):
    faculty = get_object_or_404(Faculty, id=faculty_id)
    students = Student.objects.filter(faculty=faculty)
    student_list = "".join([f"<li>{s.name} (Yoshi: {s.age})</li>" for s in students])

    html = f"""
        <h1>{faculty.name} fakulteti talabalari</h1>
        <ul>{student_list or "Talabalar hali yo'q"}</ul>
        <hr>
        <a href='/faculties/{faculty_id}/'>Back</a>
    """

    return HttpResponse(html)


def university_students(request, university_id):

    university = get_object_or_404(University, id=university_id)
    students = Student.objects.filter(faculty__university=university)
    student_list = ""
    for s in students:
        student_list += f"<li>{s.name} (Fakultet: {s.faculty.name}, Yoshi: {s.age})</li>"
    html = f"""
        <h1>{university.name} - Barcha talabalar</h1>
        <p><b>Jami talabalar soni:</b> {students.count()}</p>
        <hr>
        <ul>
            {student_list or "Hozircha talabalar mavjud emas."}
        </ul>
        <br>
        <a href='/universities/{university_id}/'> Back to Universities</a>
    """

    return HttpResponse(html)