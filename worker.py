from redis import Redis
from rq import Queue
from rq_win import WindowsWorker  # 🔥 RQ-Win'in ana sınıfı bu
from tasks import reverse_text, uppercase, sum_numbers

redis_conn = Redis()
queue = Queue("default", connection=redis_conn)

if __name__ == '__main__':
    worker = WindowsWorker([queue], connection=redis_conn)
    worker.work()
