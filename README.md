Bu proje Flask ile  gelirstirileren bir RestAPI sayesinde kullanicidan gelen gorevleri bir Redis kuyruguna ekler ve bu gorevler arka planda RQ ile islenir.

Projenin temel hedefi uzun surebilecek tersine cevirme, buyuk harfe cevirme ve sayi toplama gibi islemleri APi dan ayirarak sistemin Asenkron calisabilmesini saglar.

KURULUM

    1. Projeyi Klonla
        ##bash
        git clone git@github.com:Roalexx/InternTask.git
        cd InternTask

    2. Virtual Environment (venv) Kur
        ##bash
        python -m venv .venv

    3. Bagimliliklari Yukle
        ##bash
        pip install -r requirements.txt

    4. Redis kurulumu(windows Docker'siz)
        1. Bu https://github.com/tporadowski/redis/releases linkten Redis-x64-5.0.14.1.zip doyasini indir ve klasore cikart
        2. redis-server.exe dosyasini calistir
        3. Asagidaki yaziyi goruyosan calisiyor demeketir:
            * Ready to accept connections
        
    5. Flask Uygulamasini Baslat
        ##bash
        python app.py

    6. Farkli Bir Terminalde Worker'i Baslat
        pyhton worker.py

ORNEK API ISTEKLERI

    Gorev Olustur POST /task
        ##json 
        POST http://localhost:5000/tasks
        Content-Type: application/json

        {
            "task_type": "reverse_text",
            "data": "Merhaba"
        }

    Gorev Soucunu Al GET /resulsts/<task_id>
        ##http
        GET http://localhost:5000/results/<task_id>


    Bekleyen Gorevleri Goruntule GET /queue
        ##http
        GET http://localhost:5000/queue

    Tamamlanan Tum Gorevleri Goruntule GET /results
        ##http
        GET http://localhost:5000/results

KULLANIM SEKLI
    POST /task --> Gorev gonder
    GET /reuslts/<task_id> --> Sonuc al
    rq worker  --> Arka panda kuyrugu isler
    Tum gorevler task/py icinde tanimli fonksiyonlar uzerinden caisir

KULLANILAN KUTUPHANLER
    Flask - REST API icin
    redis - Redis serverlarina baglanmak icin
    rq - Kuyruk sistemi
    rq_win - rq sistemi windowsta stabil calismadigi icin eklenmeli
    

 
