# Online Classroom & Learning Platform

Bu proje, öğretmenlerin dersler oluşturabileceği, YouTube üzerinden ders videoları paylaşabileceği, kısa sınavlar hazırlayabileceği ve öğrencileri puanlama sistemiyle değerlendirebileceği **web tabanlı bir çevrimiçi öğrenme platformudur**. Bu proje, ClassDojo adlı bir uygulamadan esinlenilmiştir. Bazı ek fikirler olsa da, temel amacı ClassDojo'ya benzer. Yazılım açısından tamamen özgün kod kullanılmıştır.

Web sitesi template => elaadmin

Sqlite tablosu yapısı =>

    School
        classes id
        teacher id

    teachers
        id
        name
        surname
        password
        email

    students
        id name
        surname
        password
        email
        class id

    class
        id name